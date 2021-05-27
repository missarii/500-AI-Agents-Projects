
class SupportState(TypedDict):
    messages: Annotated[list, add_messages]
    user_input: str
    retrieved_context: str
    response: str
    escalate: bool


def retrieve_context(state: SupportState) -> SupportState:
    query = state["user_input"]
    if not hasattr(retrieve_context, "vectorstore"):
        texts = getattr(retrieve_context, "kb_texts", SAMPLE_KB)
        splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
        docs_split = splitter.create_documents(texts)
        embeddings = OpenAIEmbeddings()
        retrieve_context.vectorstore = FAISS.from_documents(docs_split, embeddings)

    docs = retrieve_context.vectorstore.similarity_search(query, k=3)
    context = "\n".join(d.page_content for d in docs)
    return {"retrieved_context": context}


def check_escalation(state: SupportState) -> SupportState:
    text = state["user_input"].lower()
    needs_escalation = any(kw in text for kw in ESCALATION_KEYWORDS)
    return {"escalate": needs_escalation}


def generate_response(state: SupportState) -> SupportState:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    conversation = state["messages"][:-1]  # exclude latest user msg

    if state.get("escalate"):
        response_text = "I understand your concern and I want to make sure this gets the attention it deserves. I'm connecting you with a senior support specialist who can resolve this directly. You'll hear back within 2 hours. Your case ID is #" + str(hash(state["user_input"]) % 100000) + "."
    else:
        messages = [
            SystemMessage(content=f"""You are a helpful customer support agent for CloudSync Pro.
Use this knowledge base context to answer accurately:
