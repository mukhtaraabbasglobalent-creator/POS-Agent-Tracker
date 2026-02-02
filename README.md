# 💳 POS Agent Financial Tracker System

Financial tracking and tax-ready reporting app for POS agents and small businesses.

---

## 📌 Project Overview

The POS Agent Financial Tracker System is a fintech support application designed to help POS agents and small business owners:

- Record daily transactions
- Automatically calculate service charges
- Monitor business cash flow
- Generate reports for tax and auditing purposes

This system combines financial tracking, automation, and record keeping to improve accountability and support better financial reporting.

---

## 🎯 Purpose of the Project

- Track cash in (deposits) and cash out (withdrawals)
- Automatically calculate transaction charges
- Show daily profit
- Maintain total business money records (cash box + wallet)
- Provide a simple system to support financial reporting and tax analysis

---

## ⚙️ Core Features

### ✅ Transaction Recording
- Stores transaction type, amount, date, charges, and profit earned

### 💰 Automatic Charge Calculation
| Transaction Amount | Charge |
|-------------------|-------|
| ₦1,000 – ₦9,999   | ₦100  |
| ₦10,000 – ₦19,999 | ₦200  |

### 📊 Summaries
- Daily Summary: Total Deposits, Withdrawals, Charges, Profit, Business Money
- Monthly Summary: Same as daily, aggregated by month

### 💾 Export Reports
- Export daily or monthly transactions to CSV files for auditing or presentation

---

## 🖼 Screenshots (placeholders)

- Main Menu: `screenshots/main_menu.png`  
- Add Transaction: `screenshots/add_transaction.png`  
- Daily Summary: `screenshots/daily_summary.png`  
- Monthly Summary: `screenshots/monthly_summary.png`  
- Export Confirmation: `screenshots/export.png`  

---

## 🧩 Workflow

**Flow:** Users → Add Transaction → Database → Calculations → Summaries → Export Reports

---

## 🧩 GUI + PIN Authentication Workflow (Professional Visual Flowchart)
┌───────────────────┐
         │ Start Application │
         └───────────────────┘
                  │
                  ▼
         ┌───────────────────────┐
         │  PIN Authentication    │
         │ - Enter 4-digit PIN   │
         │ - Correct?            │
         └───────────────────────┘
           │           │
       Correct        Wrong
           │           │
           ▼           │
┌───────────────────────────────┐
│       Main POS GUI Menu        │
│ 1. Add Transaction             │
│ 2. Daily Summary               │
│ 3. Monthly Summary             │
│ 4. Export Daily Report         │
│ 5. Export Monthly Report       │
│ 6. Exit                        │
└───────────────────────────────┘
                  │
                  ▼
         ┌───────────────────┐
         │  Add Transaction  │
         │ - Input Type      │
         │ - Amount          │
         │ - Cash Box/Wallet │
         │ - Description     │
         │ - Calculate Profit│
         └───────────────────┘
                  │
                  ▼
         ┌───────────────────┐
         │  Update Database  │
         └───────────────────┘
                  │
                  ▼
         ┌────────────────────────┐
         │ Show Summary / Export  │
         │        Reports         │
         └────────────────────────┘
                  │
                  ▼
         ┌───────────────────┐
         │ Exit Application  │
         └───────────────────┘

---

### ✅ Key Points

- **Secure Access:** PIN authentication ensures only authorized users access the system.  
- **GUI Interface:** Users interact with buttons and input fields.  
- **Automatic Calculations:** Charges and profits are calculated automatically.  
- **Daily & Monthly Summaries:** View business totals instantly.  
- **Export Reports:** Save CSV files for auditing or tax purposes.  

---

## 📄 Sample Reports

- `Daily_Report_YYYY-MM-DD.csv`  
- `Monthly_Report_YYYY-MM.csv`  
Uploaded in `sample_reports` folder for reference.

---

## 🎬 Demo Video

Watch the app in action:  
`demo/POS_Tracker_Demo.mp4` *(replace with your actual video file or link)*

---

## 💻 How to Run

1. Clone the repo
