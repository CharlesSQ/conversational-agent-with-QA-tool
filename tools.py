from langchain.tools import tool
from langchain.chains import ConversationChain
from langchain.schema import BasePromptTemplate
from prompts import CONVERSATION_PROMPT
# from pydantic import BaseModel, Field


# class ChatInput(BaseModel):
#     utterance: str = Field(description="should be the user's utterance")


# @tool(args_schema=ChatInput)

class LLMChatChain(ConversationChain):
    prompt: BasePromptTemplate = CONVERSATION_PROMPT

    def respond_to_user(self, user_input: str):
        """Respond to a user utterance."""
        print('respond_to_user')
        reponse = self.predict(input=user_input)
        print('response', reponse)
        return "Answer:" + reponse
