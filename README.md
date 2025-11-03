# 🤖 AI Gaming Assistant

> An intelligent AI-powered chatbot designed to help young gamers with instant answers, game strategies, and knowledge support across various topics.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-game-chatb0x-rowan-codecub.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Groq API](https://img.shields.io/badge/Groq-API-green.svg)](https://groq.com/)

---

## 📖 About

The **AI Gaming Assistant** is a smart chatbot built with Streamlit and powered by Groq's advanced Llama 3.3 70B language model. Designed specifically for young gamers, this assistant provides instant help with game strategies, explanations of game mechanics, homework support, and answers to general knowledge questions.

Whether you're stuck on a difficult level, need quick math help for a gaming calculation, or want to understand complex game lore, this AI assistant is here to help 24/7!

### 🎯 Why This Project?

- **Educational**: Combines gaming with learning, making knowledge acquisition fun
- **Accessible**: Simple, kid-friendly interface that's easy to navigate
- **Fast**: Powered by Groq's lightning-fast API for instant responses
- **Safe**: Context-aware responses suitable for young users

---

## ✨ Features

✅ **Real-Time Conversation** - Instant AI responses with minimal latency thanks to Groq's optimized infrastructure

✅ **Context Awareness** - Maintains conversation history for coherent, contextual responses

✅ **Gaming Knowledge Base** - Specialized in helping with popular games, strategies, and gaming concepts

✅ **Multi-Topic Support** - Assists with homework, math problems, science questions, and general knowledge

✅ **Message History** - Full conversation history with the ability to clear and restart

✅ **Clean UI/UX** - Modern, intuitive interface built with Streamlit's latest components

✅ **Cloud Deployed** - Accessible anywhere via Streamlit Cloud hosting

✅ **Customizable** - Easy to modify system prompts and behavior for different use cases

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.9+** | Core programming language |
| **Streamlit** | Web framework for building the UI |
| **Groq API** | AI inference API (Llama 3.3 70B Versatile) |
| **python-dotenv** | Environment variable management |
| **Git** | Version control |
| **Streamlit Cloud** | Cloud deployment platform |

---

## 🚀 How to Run Locally

### Prerequisites

- Python 3.9 or higher installed on your system
- A Groq API key (see [API Key Setup](#-api-key-setup) below)
- Git installed

### Step 1: Clone the Repository

```bash
git clone https://github.com/CodeCubCA/ai-chatbox-rowan-CodeCub.git
cd ai-chatbox-rowan-CodeCub
```

### Step 2: Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
# Create .env file
touch .env  # On macOS/Linux
# OR
type nul > .env  # On Windows
```

Add your Groq API key to the `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## ☁️ Deployment to Streamlit Cloud

### Option 1: Deploy via GitHub Integration

1. **Push your code to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**

3. **Sign in** with your GitHub account

4. **Click "New app"**

5. **Configure deployment:**
   - Repository: `CodeCubCA/ai-chatbox-rowan-CodeCub`
   - Branch: `main`
   - Main file path: `app.py`

6. **Add Secrets:**
   - Click "Advanced settings"
   - Add your secrets in TOML format:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```

7. **Click "Deploy"** and wait for your app to launch!

### Option 2: Deploy via Streamlit CLI

```bash
streamlit deploy app.py
```

Follow the prompts to authenticate and deploy.

---

## 🌐 Live Demo

**Try it now:** [AI Gaming Assistant Live Demo](https://ai-game-chatb0x-rowan-codecub.streamlit.app/)

> 💡 **Tip:** The first load might take a few seconds as the app wakes up from sleep mode.

---

## 📸 Screenshots

> **Note:** Add your screenshots here to showcase your application!

### Chat Interface
```
[Add screenshot of the main chat interface]
```

### Conversation Example
```
[Add screenshot showing a sample conversation]
```

### Response Generation
```
[Add screenshot showing the AI generating a response]
```

To add screenshots:
1. Take screenshots of your application
2. Create an `images` or `screenshots` folder in your repository
3. Upload the images to GitHub
4. Update this section with: `![Description](./images/screenshot.png)`

---

## 🔑 API Key Setup

### Getting Your Groq API Key

1. **Visit [Groq Console](https://console.groq.com/)**

2. **Sign up or Log in** to your Groq account

3. **Navigate to API Keys:**
   - Click on your profile icon
   - Select "API Keys" from the menu

4. **Create a new API key:**
   - Click "Create API Key"
   - Give it a descriptive name (e.g., "AI Chatbox Project")
   - Copy the generated key immediately (you won't be able to see it again!)

5. **Add to your project:**
   - **For local development:** Add to `.env` file
   - **For Streamlit Cloud:** Add to Secrets in deployment settings

### Free Tier Limits

Groq's free tier includes:
- ✅ High-speed inference
- ✅ Access to multiple models including Llama 3.3 70B
- ⚠️ Rate limits apply (check current limits on Groq's website)

---

## 🔮 Future Improvements

Here are some planned enhancements for future versions:

- [ ] **Voice Input/Output** - Add speech-to-text and text-to-speech capabilities
- [ ] **Multi-Language Support** - Support for Spanish, French, and other languages
- [ ] **Game-Specific Modes** - Dedicated modes for Minecraft, Roblox, Fortnite, etc.
- [ ] **Save Conversations** - Export chat history as PDF or text files
- [ ] **Custom Avatars** - Let users choose their assistant's personality/avatar
- [ ] **Response Rating** - Allow users to rate responses for quality improvement
- [ ] **Dark Mode** - Add a dark theme toggle for better viewing
- [ ] **Image Support** - Upload screenshots and get help based on visuals
- [ ] **Math Problem Solver** - Enhanced mathematical problem-solving with step-by-step solutions
- [ ] **Study Timer** - Integrated Pomodoro timer for study sessions

---

## 👨‍💻 Author

**Rowan**
*12-year-old Python Student & Game Developer*

- 🌐 Portfolio: [rowan.codecub.org](https://rowan.codecub.org)
- 💻 GitHub: [@CodeCubCA](https://github.com/CodeCubCA)
- 📧 Contact: [via portfolio website]

### About Me

I'm a passionate 12-year-old coder who loves building interactive projects that combine learning with fun. This AI chatbot is one of my projects exploring the intersection of artificial intelligence and gaming education.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

```
MIT License

Copyright (c) 2024 Rowan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ⭐ Show Your Support

If you found this project helpful or interesting, please consider giving it a star on GitHub! It helps others discover the project and motivates me to keep building cool stuff.

[![GitHub stars](https://img.shields.io/github/stars/CodeCubCA/ai-chatbox-rowan-CodeCub?style=social)](https://github.com/CodeCubCA/ai-chatbox-rowan-CodeCub)

---

## 🙏 Acknowledgments

- **Groq** for providing the amazing high-speed AI inference API
- **Streamlit** for the intuitive web framework
- **Meta AI** for the Llama 3.3 70B language model
- **My mentors** for guidance and support in my coding journey
- **The open-source community** for inspiration and resources

---

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Groq API Documentation](https://console.groq.com/docs)
- [Llama Model Information](https://ai.meta.com/llama/)
- [Python Official Documentation](https://docs.python.org/3/)

---

<div align="center">

**Built with ❤️ by a young developer learning to code**

*Making AI accessible and fun for kids!*

</div>
