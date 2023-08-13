from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

llm = ChatOpenAI()


def summarize_content(content):
    human_message_prompt = HumanMessagePromptTemplate(prompt=PromptTemplate(
        template="Write a summary for this article: {article}",
        input_variables=["article"],
    ))

    prompt = ChatPromptTemplate.from_messages([human_message_prompt])
    messages = prompt.format_prompt(article=content).to_messages()
    return llm(messages).content
