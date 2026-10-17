
"""Lesson 1.5: AI Model Profile Card.

Display model settings and estimate token costs.
"""

model_name: str = "gemma3:1b"
context_window: int = 32768
price_per_1k_tokens: float = 0.5  # Practice price in PKR, not a real fee
runs_locally: bool = True

# Why: Clear variable names make model settings easy to understand.
# Why: Correct data types help prevent errors in AI applications.

print("--- AI Model Profile Card ---")
print(f"Model name: {model_name} ({type(model_name)})")
print(f"Context window: {context_window} ({type(context_window)})")
print(f"Price per 1K tokens: {price_per_1k_tokens} PKR ({type(price_per_1k_tokens)})")
print(f"Runs locally: {runs_locally} ({type(runs_locally)})")

tokens_used = int(input("\nHow many tokens does one chat use? "))

cost = tokens_used / 1000 * price_per_1k_tokens

print(f"Estimated cost per chat: {round(cost, 2)} PKR")

# Stretch task: calculate the estimated monthly cost.
chats_per_day = int(input("How many chats per day? "))

monthly_cost = cost * chats_per_day * 30

print(f"Estimated monthly cost: {round(monthly_cost, 2)} PKR")
