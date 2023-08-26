from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

system_prompt = """
You are a web article summary writer.
Summaries are concise and only cover the essentials.
Take the 3 most important points from the article and write 3 single sentance bullet points.

This is an example of the structure of a summary:

• AI tools like DALL-E and Midjourney are increasingly being used in creative production and have started winning awards for their output.
• AI's potential to generate new, creative content is impacting industries such as Hollywood, as seen in the writers strike.
• A recent study found that AI, like GPT-4, scored in the top percent for originality in creativity tests, challenging the notion that creativity is exclusive to humans.

Only give the summary and nothing else.
Here is the article:
{article}
"""

llm = ChatOpenAI()


def summarize_content(content):
    human_message_prompt = HumanMessagePromptTemplate(prompt=PromptTemplate(
        template=system_prompt,
        input_variables=["article"],
    ))

    prompt = ChatPromptTemplate.from_messages([human_message_prompt])
    messages = prompt.format_prompt(article=content).to_messages()
    return llm(messages).content
