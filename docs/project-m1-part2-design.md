# Project M1 Part 2 — Front Desk Design

## 1. Project Overview

The Atika Beauty Salon Front Desk is a Python-based customer support system. It uses predefined rules to identify customer intents, respond to common requests, and calculate service quotes.

## 2. Intent Table

| Customer Intent | Example Input | Expected Response |
|---|---|---|
| Greeting or general question | Hello, I need information | Handle the request according to available rules |
| Price quote | `/quote` | Ask for service and quantity, then calculate the quote |
| Complaint | I have a complaint | Apologize and inform the customer that a manager will contact them |
| Refund request | I want a refund | Apologize and provide the manager-contact response |
| Late service | My appointment is late | Apologize and provide the manager-contact response |
| Human support | I need a human agent | Display the human-support message and stop the conversation |
| Exit | `bye` or `exit` | Display a goodbye message |
| Empty input | Press Enter without typing | Ask the customer to type a question |

## 3. Business Rules

1. The system asks for the customer's name at the beginning of the conversation.
2. If the customer does not enter a name, the system uses `Friend`.
3. Customer messages are stripped of extra spaces and converted to lowercase.
4. Complaint, refund, and late-service keywords are checked before ordinary requests.
5. The system supports three example services:
   - Facial: Rs. 2,500
   - Haircut: Rs. 1,200
   - Manicure: Rs. 800
6. The quantity must be a positive whole number.
7. If the quantity is invalid, the system displays an error message.
8. A 10% discount is applied when the quantity is 10 or more.
9. If the service is not on the menu, the system displays an unavailable-service message.
10. A request for a human agent ends the conversation loop.
11. The commands `bye` and `exit` end the conversation.
12. The system maintains counters for messages, answers, unanswered requests, quotes, quoted value, AI cost, and complaints, where implemented in the program.

## 4. Test Table

| Test ID | Test Input | Expected Result |
|---|---|---|
| T01 | Enter a customer name | Name is cleaned and used in the conversation |
| T02 | Leave the customer name empty | The default name `Friend` is used |
| T03 | Enter `/quote`, `facial`, quantity `1` | Quote is Rs. 2,500 |
| T04 | Enter `/quote`, `haircut`, quantity `10` | A 10% discount is applied to the subtotal |
| T05 | Enter `/quote` and an unknown service | An unavailable-service message is displayed |
| T06 | Enter a non-numeric quantity | An invalid-quantity message is displayed |
| T07 | Enter `complaint` | An apology and manager-contact message are displayed |
| T08 | Enter `human` | A human-support message is displayed and the conversation ends |
| T09 | Enter `bye` | A goodbye message is displayed |
| T10 | Submit an empty message | The system asks for a question |

## 5. Limitations

- The service prices are examples for the assignment.
- The front desk uses predefined keyword rules rather than a fully trained AI model.
- Actual Ollama model responses and test results must be recorded separately in `project-m1-part2-results.md`.
- The program's implemented behavior should be verified by running the tests.

## 6. Screenshot

Save a screenshot of the running program as:

`docs/project-m1-part2-run.png`
