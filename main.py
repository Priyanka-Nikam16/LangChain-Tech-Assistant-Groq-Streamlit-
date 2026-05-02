import streamlit as st
from app.chain import get_chain

st.set_page_config(page_title="Tech Chatbot ",page_icon="🤖",layout="wide")
st.title(" 💡Your Tech Assistant")

chain=get_chain()


#session state initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

# Add intro only once (check if it's already in history)
if not any(msg["role"] == "assistant" and "Hi, I’m Tech Chatbot" in msg["content"] 
           for msg in st.session_state.chat_history):
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": "Hi, I’m Tech Chatbot, ask me any tech question."
    })
    
#sidebar(For user History)
st.sidebar.header(" 📝 Chat History")
user_queries=[
    msg["content"] for msg in st.session_state.chat_history if msg["role"]=="user"
]

if user_queries:
    for i,query in enumerate(user_queries,1):
        st.sidebar.write(f"{i}.{query}")
else:
    st.info("No chat history yet.")




#User input
user_input=st.text_input("💬 Ask me anything about the technical field:")

if st.button(" 🚀 Ask"):
    if user_input.strip()=="":
        st.warning(" ⚠️ Please enter valid query.")
    else:
        response=chain.invoke({"input":user_input})

        #Store USER and Assistant role
        st.session_state.chat_history.append({"role":"user","content":user_input})
        st.session_state.chat_history.append({"role":"assistant","content":response})

#Chat display    
st.subheader("📢 Conversation")

for msg in st.session_state.chat_history:
    if msg["role"]=="user":
        st.markdown( f"""
            <div style='background-color:#1e1e1e;color:#d4d4d4;
                        padding:12px;border-radius:10px;margin-bottom:8px;
                        border:1px solid #3c3c3c;'>
                <b>👩‍💻 You:</b> {msg['content']}
            </div>
            """,
            unsafe_allow_html=True, #Tells Streamlit to render the raw HTML instead of escaping it. Without this, you’d just see the HTML code printed.
       )
    else:
        st.markdown( f"""
            <div style='background-color:#2d2d30;color:#f5f5f5;
                        padding:12px;border-radius:10px;margin-bottom:8px;
                        border:1px solid #3c3c3c;'>
                <b>🤖 Assistant:</b> {msg['content']}
            </div>
            """,
            unsafe_allow_html=True,)






