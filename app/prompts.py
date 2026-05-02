from langchain_core.prompts import ChatPromptTemplate

def get_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", 
         "You are Tech Chatbot, a helpful AI assistant powered by LangChain and Groq LLMs. "
         "You strictly answer questions only if they are from the tech domain. "
         "If asked outside scope, reply with 'I don't know'. "
        ),
        ("human", "{input}")
    ])