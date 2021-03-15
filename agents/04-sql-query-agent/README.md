python agent.py --db path/to/your/database.sqlite

# Single question
python agent.py --question "What is the total revenue by country?"
```

Databases open in read-only mode by default. Use `--allow-write` only with a disposable database
if you intentionally want the generated SQL agent to be able to mutate data.

## Example Questions

- "How many customers do we have in each country?"
- "What are the top 3 best-selling products?"
- "What was the total revenue last month?"
- "Which customer has spent the most?"

## Architecture

```
Natural Language → LLM (generates SQL) → SQLite → LLM (formats answer) → Response
```
