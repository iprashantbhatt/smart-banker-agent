import os
import json
from openai import OpenAI
from duckduckgo_search import DDGS
from dotenv import load_dotenv
from colorama import Fore, Style, init

# Initialize colors and security
init(autoreset=True)
load_dotenv() # Load the API key from the hidden .env file

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("❌ API Key missing! Check your .env file.")

client = OpenAI(api_key=API_KEY)

# --- TOOLS ---
def calculate_compound_interest(principal, rate, years):
    """Calculates compound interest."""
    try:
        amount = principal * (1 + rate/100)**years
        return json.dumps({
            "total_amount": round(amount, 2), 
            "interest_earned": round(amount - principal, 2)
        })
    except Exception as e:
        return f"Error in calculation: {str(e)}"

def search_web(query):
    """Searches the web for real-time information."""
    print(f"{Fore.CYAN}   🔎 Searching the web for: '{query}'...{Style.RESET_ALL}")
    try:
        results = DDGS().text(query, max_results=1)
        if results:
            return json.dumps(results[0])
        return "No results found."
    except Exception as e:
        return f"Search failed: {str(e)}"

# --- TOOL SCHEMA ---
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_compound_interest",
            "description": "Calculates future value based on interest rate, principal, and time.",
            "parameters": {
                "type": "object",
                "properties": {
                    "principal": {"type": "number"},
                    "rate": {"type": "number"},
                    "years": {"type": "number"}
                },
                "required": ["principal", "rate", "years"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Finds current info like interest rates, bank news, or inflation data.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query"}
                },
                "required": ["query"]
            }
        }
    }
]

# --- AGENT LOGIC ---
def run_smart_banker(user_input):
    print(f"\n{Fore.GREEN}🤖 User: {user_input}{Style.RESET_ALL}")
    
    messages = [
        {"role": "system", "content": "You are a specialized Financial AI Agent. Use tools to get data or calculate numbers. Be concise."},
        {"role": "user", "content": user_input}
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto" 
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            if function_name == "calculate_compound_interest":
                print(f"{Fore.YELLOW}   🧮 Tool Selected: Calculator{Style.RESET_ALL}")
                tool_response = calculate_compound_interest(
                    function_args.get("principal"), function_args.get("rate"), function_args.get("years")
                )
            elif function_name == "search_web":
                print(f"{Fore.YELLOW}   🌐 Tool Selected: Web Search{Style.RESET_ALL}")
                tool_response = search_web(function_args.get("query"))

            messages.append(response_message)
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": str(tool_response)
            })

        final_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        print(f"{Fore.BLUE}🏦 Banker Agent: {final_response.choices[0].message.content}{Style.RESET_ALL}")
    else:
        print(f"{Fore.BLUE}🏦 Banker Agent: {response_message.content}{Style.RESET_ALL}")

if __name__ == "__main__":
    print(f"{Fore.MAGENTA}--- Smart Banker Agent Initialized ---{Style.RESET_ALL}")
    # Example interactions
    run_smart_banker("What is the current inflation rate in India?")
    run_smart_banker("Calculate the growth of 50000 INR at 8% for 10 years.")
