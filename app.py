import streamlit as st
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get HuggingFace API token
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Initialize HuggingFace Inference Client
client = InferenceClient(token=HUGGINGFACE_TOKEN)

# Model selection for HuggingFace - Using a model available on Serverless Inference
MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"

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

# Model selection for HuggingFace
MODEL_NAME = "meta-llama/Llama-3.2-3B-Instruct"

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

        # Create personality-based system prompt
        personality_prompts = {
            "Friendly": "You are a friendly and warm gaming AI assistant. Talk like a close friend who loves gaming. Be enthusiastic, supportive, and encouraging. Use casual language, show genuine interest, and celebrate the user's gaming achievements. Add appropriate emojis to make the conversation fun and welcoming. 😊🎮",
            "Professional": "You are a professional and rigorous gaming AI assistant. Provide accurate, well-researched advice with a formal tone. Focus on facts, statistics, and proven strategies. Be thorough and precise in your recommendations. Maintain a respectful and expert demeanor while avoiding slang or casual language. 🎯📊",
            "Humorous": "You are a humorous and entertaining gaming AI assistant. Make gaming discussions fun with jokes, witty comments, and playful banter. Use gaming memes, pop culture references, and light-hearted humor. Keep it relaxed and enjoyable while still being helpful. Don't be afraid to roast a little (playfully)! 😄🎮"
        }

        system_prompt = personality_prompts.get(st.session_state.personality, personality_prompts["Friendly"])

        # Build conversation history for HuggingFace
        messages = [
            {"role": "system", "content": system_prompt}
        ]

        # Add conversation history
        for msg in st.session_state.messages[:-1]:  # Exclude the current user message
            messages.append({"role": msg["role"], "content": msg["content"]})

        # Add current user message
        messages.append({"role": "user", "content": prompt})

        # Call HuggingFace API
        try:
            with st.spinner("🤔 Thinking..."):
                # Generate response (non-streaming for better compatibility)
                response = client.chat_completion(
                    messages=messages,
                    model=MODEL_NAME,
                    max_tokens=500,
                    stream=False
                )

                # Extract the response content
                if hasattr(response, 'choices') and len(response.choices) > 0:
                    full_response = response.choices[0].message.content
                else:
                    full_response = "Sorry, I couldn't generate a response."

            # Display final response
            message_placeholder.markdown(full_response)

        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            full_response = f"Error: {str(e)}\n\n```\n{error_details}\n```\n\nPlease make sure your HUGGINGFACE_TOKEN is set correctly in the .env file."
            message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with enhanced styling
with st.sidebar:
    # App branding
    st.markdown("""
        <div style='text-align: center; padding: 1rem 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 1.5rem;'>
            <h1 style='color: white; margin: 0; font-size: 2rem;'>🎮</h1>
            <p style='color: white; margin: 0.5rem 0 0 0; font-size: 0.9rem;'>Gaming AI Assistant</p>
        </div>
    """, unsafe_allow_html=True)

    # Personality selection
    st.markdown("### 🎭 AI Personality")

    personality_options = {
        "😊 Friendly": "Friendly",
        "👔 Professional": "Professional",
        "😄 Humorous": "Humorous"
    }

    selected_personality = st.radio(
        "Choose conversation style:",
        options=list(personality_options.keys()),
        index=list(personality_options.values()).index(st.session_state.personality),
        help="Select how the AI responds to you",
        label_visibility="collapsed"
    )

    # Update personality if changed
    new_personality = personality_options[selected_personality]
    if new_personality != st.session_state.personality:
        st.session_state.personality = new_personality
        st.success(f"✨ Changed to {new_personality} mode!")
        st.info("💡 Clear chat to apply from the start")

    # Personality descriptions in expandable section
    with st.expander("📖 Personality Details", expanded=False):
        st.markdown("""
        <style>
        .personality-card {
            padding: 0.8rem;
            border-radius: 8px;
            margin-bottom: 0.8rem;
            border-left: 4px solid;
        }
        .friendly { border-color: #48bb78; background-color: rgba(72, 187, 120, 0.1); }
        .professional { border-color: #4299e1; background-color: rgba(66, 153, 225, 0.1); }
        .humorous { border-color: #ed8936; background-color: rgba(237, 137, 54, 0.1); }
        </style>

        <div class='personality-card friendly'>
            <strong>😊 Friendly</strong><br/>
            Warm, casual, and supportive. Like chatting with a gaming buddy!
        </div>

        <div class='personality-card professional'>
            <strong>👔 Professional</strong><br/>
            Expert advice with accurate facts and proven strategies.
        </div>

        <div class='personality-card humorous'>
            <strong>😄 Humorous</strong><br/>
            Fun and entertaining with jokes, memes, and witty banter!
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # Chat controls
    st.markdown("### ⚙️ Chat Controls")

    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.session_state.chat_session = None
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

    with col2:
        message_count = len([m for m in st.session_state.messages if m["role"] == "user"])
        st.metric("💬", message_count)

    st.divider()

    # What I can help with section
    with st.expander("💡 What I Can Help With", expanded=False):
        st.markdown("""
        - 🎯 **Game Recommendations**
          Find your next favorite game

        - 💪 **Tips & Strategies**
          Level up your gameplay

        - 📖 **Lore & Stories**
          Deep dive into game worlds

        - 🏆 **Achievements**
          Complete every challenge

        - ⚔️ **Build Guides**
          Optimize your character

        - 🎮 **And much more!**
          Just ask anything gaming-related
        """)

    st.divider()

    # About section
    with st.expander("ℹ️ About This App", expanded=False):
        st.markdown("""
        **Powered By:**
        - 🤖 HuggingFace API
          `meta-llama/Llama-3.2-3B-Instruct`
        - 🎨 Streamlit
          Interactive UI framework

        **Version:** 2.0.0
        **Status:** 🟢 Online
        """)

    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #888; font-size: 0.75rem;'>
            Made with ❤️ for gamers
        </div>
    """, unsafe_allow_html=True)
