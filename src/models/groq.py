from groq import Groq
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("GROQ_KEY")
context = """You are an intelligent assistant designed to help users analyze and understand Olympic athletes' performance data. Use your knowledge of sports statistics, Olympic history, and data interpretation to answer questions accurately, clearly, and concisely. If a question involves specific data (e.g., athletes, medals, years, countries), respond with context based on the dataset provided in the project. If additional data is needed but not available, politely inform the user."""

def GROQ_generate(messages, model, temperature=1, top_p=1):
    client = Groq(api_key=KEY)
    return client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=1024,
        top_p=top_p,
        stop=None,
    ).choices[0].message.content

def get_response(query, model):
    messages = [{"role": "system", "content": context},
                {"role": "user", "content": query}]
    return GROQ_generate(messages, model)
