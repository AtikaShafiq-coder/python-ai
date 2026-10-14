
"""Collect business details and build a prompt for an AI assistant."""

# Personalizing the greeting makes the tool feel relevant to each user.
name = input("Your name: ").strip()

# Knowing the business type helps the AI suggest solutions for that industry.
business = input("Business type: ").strip()

# A clear problem helps the AI produce more useful and specific suggestions.
problem = input("Biggest problem: ").strip()

print(f"\nWelcome, {name}!")

prompt = (
    f"Suggest 3 AI solutions for a {business} "
    f"that struggles with {problem}."
)

print("--- Your AI Prompt ---")
print(prompt)
