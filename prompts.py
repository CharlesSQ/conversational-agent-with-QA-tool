from langchain.prompts.prompt import PromptTemplate

TEMPLATE_INSTRUCTIONS_1 = """You are an Assistant designed to assist with a wide range of tasks.

Choose one of the following tools to use based on the user input:

- 1. When you need to answer questions about math, send this:
    ```json
    {{"action": "Calculator",
      "action_input": "sqrt(4)"}}
    ```

- 2. When you need to respond to other user's utterances or generate the response from the other tools, send this:
    ```json
    {{"action": "Final Answer",
      "action_input": "the final answer to the original input question"}}
    ```
- 3. When you need to generate the response from the other tools, send this:
    ```json
    {{"action": "Final Answer",
      "action_input": "the response from the tool in a prhase"}}
    ```
Current conversation:
{history}
User: {input}
Assistant:

{agent_scratchpad}"""

SUFFIX = """\nRespond ONLY in JSON format!"""

TEMPLATE_INSTRUCTIONS_2 = """Complete the objective as best you can. You have access to the following tools:

{tools}

Use this format and based on your thought choose one of the secuences below:

User: the input question you must answer
Thought: you should always think about what to do step by step

1. First secuence: You need to use a tool
Thought: the thought you had to resolve the user question
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
2. Second secuence: You have the final answer to the original input question
Thought: the thought you had for taking this secuence
Final Answer: the final answer to the original input question in a prhase
3. Third secuence: I must respond to the user withouth using any tool
Thought: the thought you had for taking this secuence
Final Answer: a direct answer to the user

Begin!

Current conversation:
{history}

User: {input}
Assistant:
{agent_scratchpad}"""

CONVERSATION_TEMPLATE = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.
Current conversation:
{history}
Human: {input}
AI:"""
CONVERSATION_PROMPT = PromptTemplate(
    input_variables=["history", "input"], template=CONVERSATION_TEMPLATE)
