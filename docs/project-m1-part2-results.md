# Project M1 Part 2 — Ollama Test Results

## Test Environment

- **Project:** Atika Beauty Salon AI Front Desk
- **Model:** [Enter the actual Ollama model name]
- **Tool:** Ollama
- **Date:** [Enter the test date]

## Test 1 — General Customer Question

**Input prompt:**

[You are the front desk assistant for Atika Beauty Salon.
A customer asks: What services do you offer?
Give a polite and helpful response.]

**Actual Ollama output:**

[Hello! Thanks so much for checking in! Atika Beauty Salon offers a range 
of services to help you achieve confident and beautiful skin.  Here's a 
summary of our offerings: 

We specialize in:

*   **Skin Analysis & Treatment:** We start with a comprehensive skin 
analysis to determine your unique needs - whether it's anti-aging, 
concerns about sun damage, or just a regular skin boosting session. We 
then offer custom treatment packages tailored to your skin's texture and 
concerns.
*   **Expert Facial Treatments:** We do Facials that focus on different 
areas to remove dead skin and prepare your skin for upcoming treatments! 
These include:
    *   Classic Facial - A great starting point for everyone
    *   Microdermabrasion - Removes skin layers to unclog pores
    *   Sugar Renewal - Exfoliate and nourish to improve skin elasticity
*   **Waxing and Tinting:**  We offer both waxing services for things like 
brows, eyebrows, and lips, and professional skin tinting to match your 
favorite color and enhance your look.
*   **Manicures &Pedicuren:** Relaxing and stylish manicures, pedicures 
and French manis. 

* **Custom Treatments:** These are treatments designed just for you, using 
the latest technology.

Could you tell me a little bit about what you’re hoping to accomplish 
today or what you've been thinking about for your beauty routine? 😊]

**Observation:**

[The Ollama model provided a polite and detailed response describing Atika Beauty Salon's services. It listed facial treatments, skin analysis, waxing, tinting, manicures, and pedicures. It also asked a follow-up question to understand the customer's needs. However, some service details were not verified against the salon's actual service menu.]

**Result:** [Pass (for a polite and helpful general response).]

## Test 2 — Customer Service Scenario

**Input prompt:**

[You are the front desk assistant for Atika Beauty Salon.
A customer says: I want a refund because my appointment was late.
Respond politely and follow this business rule:
Apologize and tell the customer that a manager will contact them.]

**Actual Ollama output:**

[“Oh my goodness, I’m really sorry to hear about your appointment being 
late! That really stinks and I sincerely regret any inconvenience this has 
caused you.  I understand you’d like a refund, and absolutely I understand 
your frustration. 

Let me get a manager over to you right now to discuss this further.   
They're the people who really handle these sorts of situations. We 
appreciate you letting us know!” 😊
]

**Observation:**

[The Ollama model responded politely and showed empathy toward the customer. It acknowledged the late appointment and refund concern and offered to involve a manager. However, the response did not follow the exact business rule, which requires apologizing and telling the customer that a manager will contact them. Instead, it said that a manager would come over right now.]

**Result:** [Fail (the response did not follow the exact business rule).]

## Conclusion

The two Ollama tests were conducted to evaluate the model's responses to customer-service scenarios. The observations and results above are based on the actual outputs generated during testing.
