import time
import os
from config import OPENAI_API_KEY

from langchain.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, AgentOutputParser, initialize_agent
from langchain.agents.conversational_chat.prompt import FORMAT_INSTRUCTIONS
from langchain.output_parsers.json import parse_json_markdown
from langchain.schema import AgentAction, AgentFinish

# Set API key for OpenAI
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
print('API key set')

# Set OpenAI LLM and embeddings
llm_chat = ChatOpenAI(temperature=0.9, max_tokens=150,
                      model='gpt-3.5-turbo-0613', client='')

# Set conversation memory buffer
memory = ConversationBufferWindowMemory(
    memory_key="chat_history", k=5, return_messages=True, output_key="output"
)

print('Memory buffer set')
# Set tools
tools = load_tools(["llm-math"], llm=llm_chat)


class OutputParser(AgentOutputParser):
    def get_format_instructions(self) -> str:
        return FORMAT_INSTRUCTIONS

    def parse(self, text: str) -> AgentAction | AgentFinish:
        try:
            # this will work IF the text is a valid JSON with action and action_input
            response = parse_json_markdown(text)
            action, action_input = response["action"], response["action_input"]
            if action == "Final Answer":
                # this means the agent is finished so we call AgentFinish
                return AgentFinish({"output": action_input}, text)
            else:
                # otherwise the agent wants to use an action, so we call AgentAction
                return AgentAction(action, action_input, text)
        except Exception:
            # sometimes the agent will return a string that is not a valid JSON
            # often this happens when the agent is finished
            # so we just return the text as the output
            return AgentFinish({"output": text}, text)

    @property
    def _type(self) -> str:
        return "conversational_chat"


# initialize output parser for agent
parser = OutputParser()

# initialize agent
agent = initialize_agent(
    agent="chat-conversational-react-description",
    tools=tools,
    llm=llm_chat,
    verbose=True,
    early_stopping_method="generate",
    memory=memory,
    agent_kwargs={"output_parser": parser}
)

# Updating prompts

sys_msg = """Assistant is a expert JSON builder designed to assist with a wide range of tasks.

Assistant is able to respond to the User and use tools using JSON strings that contain "action" and "action_input" parameters.

All of Assistant's communication is performed using this JSON format.

Assistant can also use tools by responding to the user with tool use instructions in the same "action" and "action_input" JSON format. Tools available to Assistant are:

- "Calculator": Useful for when you need to answer questions about math.
  - To use the calculator tool, Assistant should write like so:
    ```json
    {{"action": "Calculator",
      "action_input": "sqrt(4)"}}
    ```

Here are some previous conversations between the Assistant and User:

User: Hey how are you today?
Assistant: ```json
{{"action": "Final Answer",
 "action_input": "I'm good thanks, how are you?"}}
```
User: I'm great, what is the square root of 4?
Assistant: ```json
{{"action": "Calculator",
 "action_input": "sqrt(4)"}}
```
User: 2.0
Assistant: ```json
{{"action": "Final Answer",
 "action_input": "It looks like the answer is 2!"}}
```
User: Thanks could you tell me what 4 to the power of 2 is?
Assistant: ```json
{{"action": "Calculator",
 "action_input": "4**2"}}
```
User: 16.0
Assistant: ```json
{{"action": "Final Answer",
 "action_input": "It looks like the answer is 16!"}}
```

Here is the latest conversation between Assistant and User."""

instruction = " Respond to the following in JSON with 'action' and 'action_input' values "
human_msg = instruction + "\nUser: {input}"

new_prompt = agent.agent.create_prompt(
    system_message=sys_msg,
    tools=tools
)

agent.agent.llm_chain.prompt = new_prompt


def main():
    user_prompt = input("Usuario: ")
    try:
        response = agent(user_prompt)
        print('Assistant: ' + response['output'])
    except Exception as e:
        print('It looks like you entered an invalid prompt. Please try again.')
        print(e)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(1)
