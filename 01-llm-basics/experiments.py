from ask import ask

prompt = "Give me a name for a coffee shop. Reply with just the name."

for t in [0, 1]:
    print(f"\n--- temperature {t} ---")
    for _ in range(3):
        print(ask(prompt, temperature=t, max_tokens=20).content[0].text)

print("\n--- max_tokens = 20 ---")
msg = ask("Explain how transformers work.", max_tokens=20)
print(msg.content[0].text)
print("stop reason:", msg.stop_reason)