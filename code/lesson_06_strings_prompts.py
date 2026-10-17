
"""Lesson 1.6: Clean user text and build an AI prompt."""

# Ask the user for their name and question.
raw_name = input("Enter your name: ")
raw_question = input("Enter your question: ")

# Why: Removing extra spaces makes user input cleaner.
name = raw_name.strip().title()
question = raw_question.strip().capitalize()

# Why: Clean text helps us inspect questions consistently.
characters = len(question)
estimated_tokens = round(characters / 4)

# Keep the question short before adding it to the prompt.
short_question = question[:150]

# Check for Python regardless of capitalization.
mentions_python = "python" in question.lower()

# Stretch: replace an unwanted word before building the prompt.
clean_question = short_question.replace("stupid", "***")

# Example price for practice only, not a real API price.
price_per_1k_tokens = 0.5
estimated_cost = estimated_tokens / 1000 * price_per_1k_tokens

# Build a multi-line prompt using an f-string.
prompt = f"""You are a helpful Python tutor.
Hello, {name}!
Answer the user's question clearly and simply.
Question: {clean_question}"""

print("=" * 40)
print(f"Name: {name}")
print(f"Cleaned question: {question}")
print(f"Characters: {characters}")
print(f"Estimated tokens: {estimated_tokens}")
print(f"Mentions Python: {mentions_python}")
print(f"Estimated practice cost: {estimated_cost:.2f} PKR")
print("=" * 40)
print("AI Prompt:")
print(prompt)
