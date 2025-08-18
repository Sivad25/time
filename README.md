Task Logger
Overview

The Task Logger is a lightweight Python tool designed to help small business owners, freelancers, and makers track the time they spend on different customers, products, and tasks. By recording task start and end times, the program automatically calculates duration and logs the data into a CSV file for easy record-keeping and future analysis.

This tool makes it easier to review daily, weekly, or monthly workloads and provides valuable insights into how time is allocated across customers and projects.

Importance

For small business owners and independent workers, time is one of the most valuable resources. Without proper tracking, it’s easy to underestimate how long certain tasks take or lose track of where the day goes. The Task Logger solves this problem by offering a simple, menu-driven interface that records tasks consistently and generates summaries by customer and date.

By having accurate time records, you can:

Improve billing accuracy.

Identify time-consuming customers or products.

Better plan and manage your schedule.

Features

Simple Interface: A menu-driven system to start tasks, view summaries, and exit.

Automatic Time Tracking: Records start and end times automatically, calculating duration in minutes.

CSV Logging: Saves all records in a CSV file (task_log.csv) for easy review or import into spreadsheets.

Daily Summary Reports: Provides a breakdown of how much time was spent per customer per day.

Lightweight & Flexible: No databases or complicated setups required.

Installation
Prerequisites

Python 3.x installed on your system.

Setup

Clone this repository or download the .py file.

Run the program with:

python task_logger.py

Usage

When running the program, you’ll see a menu:

1. Start Task  
2. Show Summary  
3. Exit  


Start Task

Enter customer name, product name, and task description.

The timer begins immediately.

Press Enter when the task is complete.

The program automatically saves the entry into task_log.csv.

Show Summary

Displays total minutes worked per customer, grouped by date.

Example Log (CSV)
Customer	Product	Task	Date	Start	End	Minutes
Alice	Wallet	Stitching	2025-08-18	14:05:00	14:35:00	30.00
Bob	Belt	Cutting	2025-08-18	15:00:00	15:20:00	20.00
Acknowledgements

This project was created to help small business owners, crafters, and freelancers stay on top of their time tracking without needing complex software.
