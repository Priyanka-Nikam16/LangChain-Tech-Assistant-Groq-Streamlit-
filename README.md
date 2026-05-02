## LangChain-Tech-Assistant-Groq-Streamlit-


A Streamlit-based chatbot powered by LangChain and Groq LLMs, designed to answer technical domain questions.  
The chatbot uses a custom system prompt to ensure responses stay strictly within the tech domain.  
If a query falls outside scope, the assistant replies with "I don't know".

---
## 🚀 Features
- **Streamlit UI** with modern `st.chat_input` interface
- **LangChain integration** for chains, agents, and memory
- **Groq backend** for fast LLM inference
- **Custom prompt template** enforcing domain-specific responses
- **Conversation history** with `ConversationBufferMemory`
- Extendable with tools (API calls, search, calculations)

---

## ▶️ Usage
Run the Streamlit app:
- streamlit run main.py

  
Open the app in your browser at http://localhost:8501.

## 🧩 Configuration

Set your Groq API key in environment variables:
- export GROQ_API_KEY="your_api_key"
- Modify prompts.py to adjust system role or domain rules.

## 📌 Example Interaction

User: "Explain TCP three-way handshake"

Tech Assistant: "The TCP three-way handshake establishes a reliable connection using SYN, SYN-ACK, and ACK packets..."

User: "What’s the best pizza topping?"

Tech Assistant: "I don’t know."




## 📂 Project Structure

```bash
tech-chatbot-langchain-groq-streamlit/
│── app/                  # Core app logic
│   │── chain.py          # LangChain chain setup
│   │── config.py         # Configurations
│   │── llm.py            # Groq LLM integration
│   │── prompts.py        # Custom system + user prompt templates
│── .env                  # Environment variables
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
│── .venv/                # Virtual environment
│── main.py                # Sreamlit Entry point (outside app folder)

