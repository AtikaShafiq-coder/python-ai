
"""Create three AI prompts for a local business owner."""

# Collect the business details to personalize each AI prompt.
business_name = input("Business name: ").strip()
business_type = input("Business type: ").strip()
city = input("City: ").strip()
customers = input("Main customers: ").strip()
monthly_budget = int(input("Monthly budget (PKR): "))

print("\n" + "=" * 45)
print(f"AI Prompt Kit for {business_name}")
print("=" * 45)

# Why: A specific audience and friendly tone make marketing content more relevant.
marketing_prompt = (
    f"Write a short Instagram post for {business_name}, "
    f"a {business_type} in {city}. "
    f"Target {customers}. Use a friendly tone and include "
    f"one clear call to action."
)

# Why: Giving the AI a role and situation helps it write an appropriate reply.
customer_service_prompt = (
    f"You are the customer service manager of {business_name}, "
    f"a {business_type} in {city}. Write a polite and helpful "
    f"reply to a customer whose order arrived late. "
    f"Apologize sincerely and offer a suitable solution."
)

# Why: Specifying the budget helps keep the suggestions realistic.
growth_prompt = (
    f"Suggest 3 low-cost AI ideas that {business_name}, "
    f"a {business_type} in {city}, can use to attract "
    f"{customers}. Keep the ideas practical and within a "
    f"monthly budget of {monthly_budget} PKR. "
    f"Explain the estimated cost and benefit of each idea. "
    f"Do not invent exact prices; label estimates clearly."
)

print("\n[1] Marketing")
print("-" * 45)
print(marketing_prompt)

print("\n[2] Customer Service")
print("-" * 45)
print(customer_service_prompt)

print("\n[3] Growth")
print("-" * 45)
print(growth_prompt)

print("\n" + "=" * 45)
print("Copy these prompts into your AI assistant.")
print("=" * 45)

