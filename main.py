import os
import argparse
from typing import Any
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("API key not found")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def main():
    print("Hello from Bootdev-AI-agent!")

    # Parse user input
    parser = argparse.ArgumentParser(prog="AI-agent", description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    response = client.chat.completions.create(
        model="openrouter/free",

        # prompt
        #messages=args.user_prompt
        messages=[
        {"role": "user", "content": args.user_prompt}
    ]
)
    #Token usage
    if response.usage is None:
        raise RuntimeError("Failed API Request")
    else:
        prompt_tokens = response.usage.prompt_tokens 
        completion_tokens = response.usage.completion_tokens
        print(f"Prompt tokens: {prompt_tokens}\n"
              f"Response tokens: {completion_tokens}")

    # Agent response to prompt
    print("Response: ", response.choices[0].message.content)


if __name__ == "__main__":
    main()

"""
---Notes---

Because openrouter/free picks a different model on each request, you may occasionally get a model that misbehaves. 
If that happens, just retry - or swap openrouter/free for a specific free model ID (anything ending in :free, e.g. openai/gpt-oss-20b:free) from the models page.



"""