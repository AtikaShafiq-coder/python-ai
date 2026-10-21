
"""AI front desk for Atika Beauty Salon.
Answers common questions, calculates quotes, and prepares AI prompts.
"""

BOT_NAME = "Atika Beauty Salon Desk"
DELIVERY_FEE = 200
FREE_DELIVERY_LIMIT = 3000
CLOUD_PRICE_PER_1K_TOKENS = 0.5

print("=" * 50)
print(f"{BOT_NAME}: Rules, quotes and AI-ready prompts")
print("=" * 50)
print("Ask anything, type /quote for a price, or bye to exit.")

# Why: Asking once lets the desk greet the customer by name.
customer_name = input(f"{BOT_NAME}: What is your name? ").strip().title()

if customer_name == "":
    customer_name = "Friend"

message_count = 0
answered_count = 0
unanswered_count = 0
quote_count = 0
total_quoted_value = 0
total_ai_cost = 0.0
complaint_count = 0

while True:
    message = input(f"{customer_name}: ").strip().lower()
    message_count += 1

    # Why: Complaints must be handled before ordinary FAQ rules.
    if "complaint" in message or "refund" in message or "late" in message:
        complaint_count += 1
        answered_count += 1
        print(f"{BOT_NAME}: Sorry about that. A manager will contact you.")

    elif "agent" in message or "human" in message:
        print(f"{BOT_NAME}: Connecting you to a human...")
        break

    elif message == "bye" or message == "exit":
        print(f"{BOT_NAME}: Goodbye, {customer_name}!")
        break

    elif message == "":
        print(f"{BOT_NAME}: Please type a question.")

    elif message == "/quote":
        item = input(f"{BOT_NAME}: Which item? ").strip().lower()
        quantity_text = input(f"{BOT_NAME}: How many? ").strip()

        # Why: isdigit() prevents letters from crashing int conversion.
        if not quantity_text.isdigit() or int(quantity_text) <= 0:
            print(f"{BOT_NAME}: Enter a whole-number quantity above zero.")
        else:
            quantity = int(quantity_text)

            if item == "facial":
                unit_price = 2500
            elif item == "haircut":
                unit_price = 1200
            elif item == "manicure":
                unit_price = 800
            else:
                unit_price = 0

            if unit_price == 0:
                print(f"{BOT_NAME}: Sorry, {item} is not on our service menu.")
            else:
                subtotal = unit_price * quantity

                if quantity >= 10:
                    discount = subtotal * 0.10
                else:
                    discount = 0

                discounted_total = subtotal - discount

                # Why: Delivery is checked after applying the discount.
                if discounted_total >= FREE_DELIVERY_LIMIT:
                    delivery = 0
                else:
                    delivery = DELIVERY_FEE

                quote_total = discounted_total + delivery
                quote_count += 1
                answered_count += 1
                total_quoted_value += quote_total

                print(f"{BOT_NAME}: {quantity:,} x {item} = {subtotal:,.0f} PKR")
                print(f"Discount: -{discount:,.0f} PKR")
                print(f"Delivery: {delivery:,.0f} PKR")
                print(f"Total: {quote_total:,.0f} PKR")

    elif "hour" in message or "open" in message or "time" in message:
        answered_count += 1
        print(f"{BOT_NAME}: We are open 10 AM to 8 PM, Monday to Saturday.")

    elif "where" in message or "location" in message or "address" in message:
        answered_count += 1
        print(f"{BOT_NAME}: Our example location is Main Boulevard, Lahore.")

    elif "price" in message or "cost" in message or "charges" in message:
        answered_count += 1
        print(f"{BOT_NAME}: Type /quote for a service price estimate.")

    elif message == "hi" or message == "hello" or message.startswith("salam"):
        answered_count += 1
        print(f"{BOT_NAME}: Hello, {customer_name}! How can I help you?")

    elif "booking" in message or "appointment" in message:
        answered_count += 1
        print(f"{BOT_NAME}: Please contact the salon to book an appointment.")

    else:
        unanswered_count += 1
        clean_question = message.capitalize()[:150]
        estimated_tokens = round(len(clean_question) / 4)

        # Why: Private questions use a local model with zero example cost.
        if (
            "phone" in clean_question.lower()
            or "cnic" in clean_question.lower()
            or "my address" in clean_question.lower()
        ):
            chosen_model = "llama3.2 (local, private)"
            estimated_cost = 0.0
        else:
            chosen_model = "small cloud model (cheap)"
            estimated_cost = estimated_tokens / 1000 * CLOUD_PRICE_PER_1K_TOKENS
            total_ai_cost += estimated_cost

        prompt = f"""You are the assistant of Atika Beauty Salon.
Answer {customer_name} in 2 short lines.
Question: {clean_question}"""

        print(f"{BOT_NAME}: Routed to {chosen_model} (~{estimated_tokens} tokens)")
        print(prompt)

print("=" * 50)
print("Session report")
print(f"Messages: {message_count}")
print(f"Answered by rules: {answered_count}")
print(f"Unanswered: {unanswered_count}")
print(f"Quotes: {quote_count}")
print(f"Quoted value: {total_quoted_value:,.0f} PKR")
print(f"Estimated AI cost: {total_ai_cost:.4f} PKR")
print(f"Complaints received: {complaint_count}")
print("=" * 50)
