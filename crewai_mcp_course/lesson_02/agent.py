# Custom Tool: Text Formatter
class TextFormatterTool(BaseTool):
    name: str = "text_formatter"
    description: str = "Format text as a numbered list. Input: comma-separated items."

    def _run(self, items: str) -> str:
        item_list = [i.strip() for i in items.split(",")]
        return "\n".join(f"{i+1}. {item}" for i, item in enumerate(item_list))


word_counter = WordCountTool()
formatter = TextFormatterTool()

# Agent 1: Researcher
researcher = Agent(
    role="Senior Researcher",
    goal="Research topics thoroughly and provide factual, well-structured information",
    backstory="PhD researcher with expertise in synthesizing complex information from multiple sources.",
    llm=llm,
    tools=[word_counter],
    verbose=True,
)

# Agent 2: Writer
writer = Agent(
    role="Technical Writer",
    goal="Transform research into clear, engaging content for technical audiences",
    backstory="Award-winning technical writer with 10 years experience in AI/ML documentation.",
    llm=llm,
    tools=[formatter],
    verbose=True,
)

# Agent 3: Editor
editor = Agent(
    role="Content Editor",
