# 🤖 GenAI Chatbot

A simple AI-powered chatbot built using **Streamlit**, **LangChain**, and **Groq API**. It supports interactive conversations with a clean UI and Light/Dark themes.

## ✨ Features
- AI-powered responses using Groq.
- Interactive chat interface.
- Light and Dark mode.
- Conversation history and clear chat option.

## 🛠️ Tech Stack
- Python
- Streamlit
- LangChain
- Groq API

## 🚀 Run Locally

1. Clone the repository:
   ```bash
   git clone YOUR_REPOSITORY_URL
   cd YOUR_REPOSITORY_NAME
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:
   ```env
   GROQ_API_KEY=your_groq_api_key
   ```

5. Start the application:
   ```bash
   streamlit run chatbot.py
   ```

## ☁️ Deployment
Deploy the app using [Streamlit Community Cloud](https://share.streamlit.io/) and configure `GROQ_API_KEY` in the app's Secrets settings.

## 🔐 Security
Never commit your API key or `.env` file to GitHub.

## 📄 License
This project is open source and available for personal and educational use.
