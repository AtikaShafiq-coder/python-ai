
"""Lesson 1.7: Smart Model Router."""

# Ask for the task type and clean the input.
task = input("Task (code / private / chat): ").strip().lower()

# Convert the token input to an integer for numerical comparisons.
tokens = int(input("Estimated tokens: "))

# Why: Private data should stay on the user's laptop.
# Why: Different tasks may need different models and prices.
if task == "private":
    model = "llama3.2 (local, Ollama)"
    price_per_1k_tokens = 0.0
elif task == "code":
    model = "Claude (cloud, strong at code)"
    price_per_1k_tokens = 2.0
elif task == "chat":
    model = "Small cloud model (cheap for chat)"
    price_per_1k_tokens = 0.5
else:
    model = "Small cloud model (default)"
    price_per_1k_tokens = 0.5

# Calculate the example cost.
cost = tokens / 1000 * price_per_1k_tokens

# Warn the user when the request is too long.
if tokens > 4000:
    warning = "Long request: consider shortening it."
else:
    warning = "Length is fine."

# Stretch task: check whether a free user has a long request.
paid_user = input("Is this a paid user? (yes/no): ").strip().lower()

if paid_user == "no" and tokens > 2000:
    print("Upgrade to send long requests.")

print("=" * 40)
print(f"Chosen model: {model}")
print(f"Estimated cost: {cost:.2f} (example price units)")
print(warning)
print("=" * 40)
