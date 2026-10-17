
"""Lesson 1.8: Rule-based chatbot for a beauty salon."""

BOT = "Atika Beauty Salon Bot"

print(f"{BOT}: Welcome! I can help with prices, hours, location and bookings.")
print(f"{BOT}: Type 'bye' to exit.")

# Why: Asking the name once lets the bot use it throughout the chat.
name = input(f"{BOT}: What is your name? ").strip().title()

if name == "":
    name = "friend"

print(f"{BOT}: Nice to meet you, {name}!")

count = 0
unanswered = 0
complaints = 0

# Why: Counters help the business understand customer questions.
while True:
    message = input(f"{name}: ").strip().lower()
    count += 1

    if message == "bye" or message == "exit":
        print(f"{BOT}: Goodbye, {name}! Thank you for visiting.")
        break

    elif message == "":
        print(f"{BOT}: Please type a question.")

    # Why: Handle complaints before booking so unhappy customers get help first.
    elif "complaint" in message or "refund" in message or "late" in message:
        complaints += 1
        print(f"{BOT}: Sorry about that. Connecting you to a human...")

    elif "agent" in message or "human" in message:
        print(f"{BOT}: Connecting you to a human...")
        break

    elif "hour" in message or "open" in message or "time" in message:
        print(f"{BOT}: Our example opening hours are 10 AM to 8 PM.")

    elif "price" in message or "cost" in message or "charges" in message:
        print(f"{BOT}: Please tell us which salon service you need prices for.")

    elif "where" in message or "location" in message or "address" in message:
        print(f"{BOT}: Our example location is Main Boulevard, Lahore.")

    elif "booking" in message or "appointment" in message:
        print(f"{BOT}: Please contact our salon to book an appointment.")

    # Why: Exact greeting matches avoid triggering on words like "which".
    elif message == "hi" or message == "hello" or message.startswith("salam"):
        print(f"{BOT}: Hello, {name}! How can I help you?")

    else:
        unanswered += 1
        prompt = (
            "You are a helpful beauty salon assistant. "
            f"Answer this customer question politely: {message}"
        )
        print(f"{BOT}: I don't know that answer yet.")
        print(f"AI prompt for Module 2: {prompt}")

print("=" * 40)
print(f"Chat summary: {count} messages")
print(f"Unanswered questions: {unanswered}")
print(f"Complaints received: {complaints}")
print("=" * 40)
