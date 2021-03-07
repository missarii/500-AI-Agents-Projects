            (1,1,1,1,1299.99,'2024-04-01'),
            (2,1,2,2,59.98,'2024-04-01'),
            (3,2,3,1,49.99,'2024-04-05'),
            (4,3,4,1,599.99,'2024-04-10'),
            (5,4,1,1,1299.99,'2024-04-12'),
            (6,2,2,3,89.97,'2024-04-15');
    """)
    conn.commit()
    conn.close()


def sqlite_uri(db_path: str, read_only: bool = True) -> str:
    abs_path = os.path.abspath(db_path)
    if read_only:
        return f"sqlite:///file:{quote(abs_path)}?mode=ro&uri=true"
    return f"sqlite:///{abs_path}"


def build_agent(db_path: str, read_only: bool = True):
    db = SQLDatabase.from_uri(sqlite_uri(db_path, read_only=read_only))
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
    )
    return agent, db


def main():
    parser = argparse.ArgumentParser(description="SQL Query Agent")
