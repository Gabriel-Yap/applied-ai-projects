from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic(default_headers={"anthropic-version": "2023-06-01"})

def ask(prompt, temperature=None, max_tokens=300, model="claude-haiku-4-5"):
    extra = {"temperature": temperature} if temperature is not None else {}
    return client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
        extra_body=extra,
    )

if __name__ == "__main__":
    msg = ask("Explain what a token is in one sentence.")
    print(msg.content[0].text)
    print("stop reason:", msg.stop_reason)
    print("tokens in/out:", msg.usage.input_tokens, msg.usage.output_tokens)