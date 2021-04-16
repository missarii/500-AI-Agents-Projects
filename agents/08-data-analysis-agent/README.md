
# Your own data
python agent.py --file your_data.csv --allow-dangerous-code

# Single question
python agent.py --file sales.csv --question "What is the monthly revenue trend?" --allow-dangerous-code
```

## Safety Note

This demo uses LangChain's pandas agent, which executes model-generated Python code.
Use `--allow-dangerous-code` only with trusted prompts and non-sensitive local data.

## Example Questions

- "What is the total revenue by product?"
- "Which region performs best?"
- "Show the correlation between quantity and revenue"
- "What are the top 5 selling products?"
