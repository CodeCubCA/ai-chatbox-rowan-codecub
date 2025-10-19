[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/a2pucUEo)

# 🎮 Gaming AI Chat Assistant

A gaming-themed AI chatbot built with Streamlit and powered by Groq's llama-3.3-70b-versatile model.

## Features

- 🎮 Gaming-focused AI assistant
- 💬 Real-time streaming responses
- 🎨 Clean and intuitive interface
- 📝 Chat history management
- 🔒 Secure API key handling

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   - Copy `.env.example` to `.env`
   - Get your Groq API key from https://console.groq.com/keys
   - Add your API key to `.env`:
     ```
     GROQ_API_KEY=your_actual_api_key_here
     ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage

- Type your gaming-related questions in the chat input
- Get instant AI-powered responses about games, strategies, tips, and more
- Use the "Clear Chat History" button to start a fresh conversation

## Technologies

- **Streamlit**: Web interface framework
- **Groq API**: AI model provider (llama-3.3-70b-versatile)
- **Python-dotenv**: Environment variable management

## License

MIT
