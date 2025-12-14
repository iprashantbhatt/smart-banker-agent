# 🏦 Smart Banker AI Agent

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/AI-OpenAI_GPT--4o-green?style=for-the-badge&logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/Status-Prototype-orange?style=for-the-badge)

> **Bridging Finance & Technology.**
> An autonomous AI agent capable of researching real-time financial data and performing complex investment calculations.

---

## 🌟 Features

* **🧠 Intelligent Routing:** The agent "thinks" before acting. It decides whether to chat, calculate, or research.
* **🌐 Real-Time Web Search:** Uses DuckDuckGo to fetch current interest rates, inflation data, and market news.
* **🧮 Financial Calculator:** Built-in Python tools for precise Compound Interest calculations (no LLM math errors).
* **🔒 Secure Architecture:** Uses environment variables to protect API keys.

---

## 🛠️ Technology Stack

* **Language:** Python
* **LLM Engine:** OpenAI GPT-4o-mini
* **Search Tool:** DuckDuckGo Search API
* **Function Calling:** OpenAI Tools API

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
https://github.com/iprashantbhatt/smart-banker-agent
2. Install dependencies
Bash

pip install -r requirements.txt
3. Setup Security
Create a .env file in the root folder and add your API key:

Bash

OPENAI_API_KEY=your_sk_key_here
4. Run the Agent
Bash

python src/agent.py
📸 Example Usage
User: "What is the current home loan rate for SBI, and if I take a 50 Lakh loan at that rate for 20 years, what is the interest?"

Agent Action:

Searches Web -> Finds SBI Home Loan Rate (~8.50%).

Calls Calculator -> Computes compound interest on 50L @ 8.5%.

Final Answer -> "The current rate is 8.50%. The total interest payable would be..."

👨‍💻 Author
Prashant Bhatt Banker | Tech Enthusiast | AI Explorer

LinkedIn | GitHub


---

### **Step 3: Push to GitHub**

Now, run these commands in your terminal to put it all online:

```bash
git init
git add .
git commit -m "Initial commit: Smart Banker Agent with Tools"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/smart-banker-agent.git
git push -u origin main
