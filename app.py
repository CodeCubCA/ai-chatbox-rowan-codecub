import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key from environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page configuration
st.set_page_config(
    page_title="My Gaming AI Assistant",
    page_icon="🎮",
    layout="centered"
)

# Title and description
st.title("🎮 My Gaming AI Assistant")
st.markdown("""
Welcome to **My Gaming AI Assistant**! 🎯

I'm your personal AI companion designed to help you with everything gaming-related. Whether you need:
- 🕹️ Game recommendations tailored to your preferences
- 💡 Expert strategies and tips to level up your gameplay
- 📖 Deep dives into game lore and storylines
- ⚔️ Build guides and character optimization
- 🏆 Achievement and trophy hunting advice

Just ask me anything, and let's explore the gaming world together!
""")

# Initialize personality in session state
if "personality" not in st.session_state:
    st.session_state.personality = "Friendly"

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add a welcome message from the assistant
    welcome_messages = {
        "Friendly": "Hey there, friend! 🎮 I'm so excited to chat with you about games! What's on your mind today? Need some tips, want to discuss your favorite game, or looking for something new to play? I'm all ears! 😊",
        "Professional": "Greetings! 🎮 I am your professional gaming AI assistant. I'm here to provide you with accurate, well-researched gaming advice, strategies, and recommendations. How may I assist you today?",
        "Humorous": "Yo, what's up gamer! 🎮 Ready to talk about games and have some laughs? I promise I won't rage quit on you (unlike that last boss fight, am I right? 😄). Hit me with your questions!"
    }
    st.session_state.messages.append({
        "role": "assistant",
        "content": welcome_messages.get(st.session_state.personality, welcome_messages["Friendly"])
    })

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything about gaming..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Create messages array for API call with personality-based system prompt
        personality_prompts = {
            "Friendly": "You are a friendly and warm gaming AI assistant. Talk like a close friend who loves gaming. Be enthusiastic, supportive, and encouraging. Use casual language, show genuine interest, and celebrate the user's gaming achievements. Add appropriate emojis to make the conversation fun and welcoming. 😊🎮",
            "Professional": "You are a professional and rigorous gaming AI assistant. Provide accurate, well-researched advice with a formal tone. Focus on facts, statistics, and proven strategies. Be thorough and precise in your recommendations. Maintain a respectful and expert demeanor while avoiding slang or casual language. 🎯📊",
            "Humorous": "You are a humorous and entertaining gaming AI assistant. Make gaming discussions fun with jokes, witty comments, and playful banter. Use gaming memes, pop culture references, and light-hearted humor. Keep it relaxed and enjoyable while still being helpful. Don't be afraid to roast a little (playfully)! 😄🎮"
        }

        api_messages = [
            {
                "role": "system",
                "content": personality_prompts.get(st.session_state.personality, personality_prompts["Friendly"])
            }
        ]

        # Add chat history to API messages
        for msg in st.session_state.messages:
            api_messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        # Call Groq API with streaming
        try:
            stream = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=api_messages,
                temperature=0.7,
                max_tokens=1024,
                stream=True
            )

            # Stream the response
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")

            # Display final response
            message_placeholder.markdown(full_response)

        except Exception as e:
            full_response = f"Error: {str(e)}\n\nPlease make sure your GROQ_API_KEY is set correctly in the .env file."
            message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with personality selection and additional info
with st.sidebar:
    st.header("⚙️ Settings")

    # Personality selection with emoji icons
    st.subheader("🎭 AI Personality")
    personality_options = {
        "😊 Friendly": "Friendly",
        "👔 Professional": "Professional",
        "😄 Humorous": "Humorous"
    }

    selected_personality = st.radio(
        "Choose how I should talk to you:",
        options=list(personality_options.keys()),
        index=list(personality_options.values()).index(st.session_state.personality),
        help="Select the AI's conversation style"
    )

    # Update personality if changed
    new_personality = personality_options[selected_personality]
    if new_personality != st.session_state.personality:
        st.session_state.personality = new_personality
        st.success(f"Personality changed to {new_personality}! 🎉")
        st.info("Clear chat history to see the new personality in action from the start!")

    st.markdown("---")

    # Personality descriptions
    st.subheader("📝 Personality Guide")
    st.markdown("""
    **😊 Friendly**
    Warm and friendly, chat like friends. Casual, supportive, and enthusiastic!

    **👔 Professional**
    Rigorous and professional. Accurate advice with expert knowledge.

    **😄 Humorous**
    Relaxed and humorous. Fun conversations with jokes and memes!
    """)

    st.markdown("---")

    st.header("ℹ️ About")
    st.markdown("""
    This is a gaming-focused AI chatbot powered by:
    - **Groq API** (llama-3.3-70b-versatile)
    - **Streamlit** for the interface

    Ask me about:
    - 🎯 Game recommendations
    - 💡 Gaming tips & strategies
    - 📖 Game lore & stories
    - 🏆 Achievement guides
    - ⚔️ Build optimization
    - And much more! 🎮
    """)

    st.markdown("---")

    # Clear chat button with emoji
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        welcome_messages = {
            "Friendly": "Hey there, friend! 🎮 I'm so excited to chat with you about games! What's on your mind today? Need some tips, want to discuss your favorite game, or looking for something new to play? I'm all ears! 😊",
            "Professional": "Greetings! 🎮 I am your professional gaming AI assistant. I'm here to provide you with accurate, well-researched gaming advice, strategies, and recommendations. How may I assist you today?",
            "Humorous": "Yo, what's up gamer! 🎮 Ready to talk about games and have some laughs? I promise I won't rage quit on you (unlike that last boss fight, am I right? 😄). Hit me with your questions!"
        }
        st.session_state.messages.append({
            "role": "assistant",
            "content": welcome_messages.get(st.session_state.personality, welcome_messages["Friendly"])
        })
        st.rerun()
