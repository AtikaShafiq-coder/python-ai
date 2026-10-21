
# Python for AI

**Student:** Atika Shafiq

**Course:** Python for AI

## My AI Goal

My goal is to become an AI/ML Engineer and build practical AI solutions for real-world business problems.

## How to Run

Run the main program:

```bash
uv run main.py
```

Run the introduction task:

```bash
uv run code/lesson_01_intro.py
```

## Lessons Completed

- Lesson 1.1: Your AI Career Intro
- Lesson 1.2: Toolkit Proof
- Lesson 1.3: Client-Ready Repo
- Lesson 1.4: Business Prompt Builder
- Lesson 1.5: Variables and Data Types
- Lesson 1.6: Working with Text (Strings)
- Lesson 1.7: Operators and Making Decisions
- Lesson 1.8: Mini Project — Rule-Based Chatbot


## Module 1 Project: AI Prompt Kit

A Python tool that turns a local business's details into
3 ready-to-use AI prompts for marketing, customer service,
and business growth.

**Run:**

```bash
uv run code/project_m1_prompt_kit.py
```

![Prompt Kit running](docs/project-m1-run.png)

**Who would pay for this:** Local small business owners who
want to use AI for their daily business tasks but do not
know how to write effective prompts.


### Lesson 1.5: Variables and Data Types

![Lesson 1.5 Output](docs/lesson-05-output.png)

### Lesson 1.6: Working with Text (Strings)

![Lesson 1.6 Output](docs/lesson-06-output.png)

### Lesson 1.7: Operators and Making Decisions

![Lesson 1.7 Output](docs/lesson-07-output.png)


## Lesson 1.8: Business Helper Bot

**Business:** Atika Beauty Salon

| Intent | Keywords | Reply |
|---|---|---|
| Complaint | complaint, refund, late | Connect to a human |
| Opening hours | hours, open, time | Open 10 AM to 8 PM |
| Prices | price, cost, charges | Ask about a service |
| Location | location, address, where | Main Boulevard, Lahore |
| Booking | booking, appointment | Contact us to book |
| Greeting | hi, hello, salam | Friendly greeting |
| Exit | bye, exit | Goodbye and summary |
| Other | No matching keyword | Show an AI prompt |

### Lesson 1.8: Chatbot Output

![Lesson 1.8 Output](docs/lesson-08-output.png)

# Python for AI — Module 1

**Course:** Python for AI  
**Module:** Python Basics for GenAI and Agentic AI  
**Checkpoint:** 2 — Code Tasks (Lessons 1.5 to 1.8)  
**Updated:** October 2026

## Project Overview

This repository contains Python practice tasks from Module 1. These tasks cover variables, strings, prompt building, conditional statements, model routing, and a rule-based chatbot.

The purpose is to understand basic Python concepts and apply them to simple AI-related tasks.

## Project Structure

```text
python-ai/
├── README.md
├── code/
│   ├── lesson_05_variables.py
│   ├── lesson_06_strings_prompts.py
│   ├── lesson_07_conditions.py
│   └── lesson_08_mini_chatbot.py
└── docs/
```

## Task 1.6: Prompt Cleaner

**File:** `code/lesson_06_strings_prompts.py`

### Objective

Clean the user's name and question, measure the question, and build a prompt for an AI tutor.

### Features

- Cleans the name using `.strip().title()`.
- Cleans the question using `.strip().capitalize()`.
- Counts characters using `len()`.
- Estimates tokens by dividing characters by 4 and rounding.
- Checks for the word "python" regardless of capitalization.
- Limits the question to 150 characters.
- Replaces the word "stupid" with `***`.
- Calculates an example cost to two decimal places.
- Builds and prints a multiline f-string prompt.

### Run

```bash
uv run code/lesson_06_strings_prompts.py
```

## Task 1.7: Smart Model Router

**File:** `code/lesson_07_conditions.py`

### Objective

Choose a suitable model based on the task type and estimate the request cost.

### Features

- Accepts `code`, `private`, or `chat` as task types.
- Cleans task input using `.strip().lower()`.
- Routes private tasks to a local model.
- Routes coding tasks to a cloud model suited to coding.
- Routes chat tasks to a low-cost cloud model.
- Calculates an example request cost.
- Warns when a request exceeds 4,000 tokens.
- Checks whether a free user has a request exceeding 2,000 tokens.

### Run

```bash
uv run code/lesson_07_conditions.py
```

**Note:** Model prices are practice examples, not verified current API prices.

## Task 1.8: Beauty Salon Chatbot

**File:** `code/lesson_08_mini_chatbot.py`

### Objective

Create a rule-based chatbot for a beauty salon that answers common questions and tracks unanswered questions and complaints.

### Intent Design Table

| Intent | Keywords to look for | Reply |
|---|---|---|
| Opening hours | hour, open, time | Our example opening hours are 10 AM to 8 PM. |
| Service prices | price, cost, charges | Please tell us which salon service you need prices for. |
| Salon location | where, location, address | Our example location is Main Boulevard, Lahore. |
| Appointments | booking, appointment | Please contact our salon to book an appointment. |
| Greeting | hi, hello, salam | Hello! How can I help you? |
| Complaint | complaint, refund, late | Sorry about that. Connecting you to a human... |
| Human handover | agent, human | Connecting you to a human... |
| Exit | bye, exit | Goodbye! Thank you for visiting. |
| Unknown question | Other unmatched messages | Display an AI prompt for Module 2 and count the unanswered question. |

### Features

- Welcomes customers to the salon.
- Asks for the customer's name once before the chat loop.
- Uses `while True` to handle repeated messages.
- Cleans messages using `.strip().lower()`.
- Handles complaints and human handover before ordinary questions.
- Answers common salon questions using keyword matching.
- Counts messages, unanswered questions, and complaints.
- Prints a prompt for an AI assistant when a question is not recognized.
- Ends the conversation with `bye` or `exit`, or when human handover is requested.
- Prints a chat summary when the loop ends.

### Run

```bash
uv run code/lesson_08_mini_chatbot.py
```

## Concepts Practised

- Variables and Python data types
- User input and output
- String methods and slicing
- F-strings and multiline strings
- Type conversion and basic calculations
- `if`, `elif`, and `else`
- Boolean conditions and logical operators
- `while` loops and `break`
- Counters and conditional keyword matching
- Basic prompt engineering
- Git and GitHub version control

## Testing

Before submitting, run each script and test its required inputs.

```bash
uv run code/lesson_06_strings_prompts.py
uv run code/lesson_07_conditions.py
uv run code/lesson_08_mini_chatbot.py
```

For the chatbot, test greetings, opening hours, prices, location, appointments, complaints, human handover, unknown questions, empty input, and exit commands.

## Notes

- Example prices and salon details are for practice only.
- The chatbot uses predefined rules; it does not call a real AI API.
- The AI prompt displayed by the chatbot is prepared for future development in Module 2.
- Each task should have its own clear Git commit message.

---

## Project M1 — Part 2: AI Front Desk

### Overview

This part extends the previous Python tasks into a front-desk system for Atika Beauty Salon. It handles customer requests, service quotes, complaints, and human-support requests using predefined business rules.

### Features

- Greets customers by name.
- Processes customer messages.
- Calculates service quotes.
- Applies a 10% discount for quantities of 10 or more.
- Handles complaints and refund requests.
- Supports requests for a human representative.
- Validates service quantities.

### Run the Program

Run the following command from the repository root:

```bash
uv run code/project_m1_front_desk.py
```

### Part 2 Files

- `code/project_m1_front_desk.py` — Front-desk Python program.
- `docs/project-m1-part2-design.md` — Intent table, business rules, and test table.
- `docs/project-m1-part2-results.md` — Results of two actual Ollama tests.
- `docs/project-m1-part2-run.png` — Screenshot of the running program.

### Example Service Prices

| Service | Example Price |
|---|---:|
| Facial | Rs. 2,500 |
| Haircut | Rs. 1,200 |
| Manicure | Rs. 800 |

*These prices are examples for the assignment.*

