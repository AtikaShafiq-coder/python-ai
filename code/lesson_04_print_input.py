
"""TASK:04 Collect business details and build a prompt for an AI assistant."""

# Ask for the user's name to make the greeting more personal.
name = input("Your name: ").strip()

# Get the type of business the user wants help with.
business = input("Business type: ").strip()

# Ask about the main problem the business is facing.
problem = input("Biggest problem: ").strip()

print(f"\nWelcome, {name}!")

# Create a prompt based on the business details provided by the user.
prompt = (
    f"Suggest 3 AI solutions for a {business} "
    f"that struggles with {problem}."
)

# Display the final prompt for the user.
print("--- Your AI Prompt ---")
print(prompt)
