# Module 1, Checkpoint 2: Quick Checks
**Course:** Python for AI  
**Module:** 1 — Python Basics for GenAI and Agentic AI  
**Lessons:** 1.5 to 1.8  
**Student:** Atika

---

## Lesson 1.5: Variables and Data Types

### MCQ Answers

| Question | Correct Option | Answer |
|---|---|---|
| Q1 | b | float |
| Q2 | b | 7 |
| Q3 | c | `user_name_2` |
| Q4 | b | True |
| Q5 | b | `input()` returns text, which cannot be directly added to a number. |

### Q6: Predict the Output

**Code:**

```python
price = 2.5
qty = "4"
total = price * int(qty)
print(total)
```

**Predicted Output:**

```text
10.0
```

**Explanation:** `int(qty)` converts the string `"4"` into the integer `4`. Multiplying `2.5` by `4` gives `10.0`.

---

## Lesson 1.6: Working with Text (Strings)

### MCQ Answers

| Question | Correct Option | Answer |
|---|---|---|
| Q1 | b | `"Sweet"` |
| Q2 | b | `"r"` |
| Q3 | b | `.strip().title()` |
| Q4 | b | `lahore` |
| Q5 | b | `"sugar-free" in message.lower()` |

### Q6: Predict the Output

**Code:**

```python
bill = 98765.4321
chats = 2500000
print(f"{bill:.1f} PKR for {chats:,} chats")
```

**Predicted Output:**

```text
98765.4 PKR for 2,500,000 chats
```

**Explanation:** `.1f` formats the bill to one decimal place, while `:,` adds commas to separate thousands.

---

## Lesson 1.7: Operators and Making Decisions

### MCQ Answers

| Question | Correct Option | Answer |
|---|---|---|
| Q1 | b | 5 |
| Q2 | b | 3 |
| Q3 | b | `if plan != "free":` |
| Q4 | b | The condition is True because `"Karachi"` is a non-empty string. |
| Q5 | a | Medium |

### Q6: Predict the Output

**Code:**

```python
is_paid = False
tokens = 2500

if not is_paid and tokens > 2000:
    print("Upgrade")
elif tokens > 2000:
    print("Long request")
else:
    print("OK")
```

**Predicted Output:**

```text
Upgrade
```

**Explanation:** `not is_paid` evaluates to True, and `tokens > 2000` is also True. Therefore, the first branch executes.

---

## Lesson 1.8: Mini Project — Rule-Based Chatbot

### MCQ Answers

| Question | Correct Option | Answer |
|---|---|---|
| Q1 | b | The bot says goodbye, then asks for the next message again. |
| Q2 | b | The message was not cleaned using `.strip().lower()`. |
| Q3 | b | The complaint rule fires because `"late"` appears inside `"chocolate"`. |
| Q4 | a | The price reply prints; the refund rule should come first. |
| Q5 | b | Initialize `count = 0` once before the loop. |

### Q6: Predict the Output

**User Inputs:**

```text
HOURS?
where are you
  Bye
```

**Predicted Output:**

```text
Open 9 to 5
3 messages, 1 unanswered
```

**Explanation:**

1. `HOURS?` is converted to lowercase, so the hours rule matches.
2. `where are you` matches no rule, so the unanswered counter increases to 1.
3. `Bye` is stripped and converted to `bye`, ending the loop.
4. The total message count is 3.

---

## Final Summary

| Lesson | MCQs Correct | Q6 Completed |
|---|---|---|
| Lesson 1.5 | 5 answers | Yes |
| Lesson 1.6 | 5 answers | Yes |
| Lesson 1.7 | 5 answers | Yes |
| Lesson 1.8 | 5 answers | Yes |

**Total:** 24 questions — 20 MCQs and 4 output-prediction questions.

