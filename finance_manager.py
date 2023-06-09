import csv
import os
from collections import defaultdict


class PersonalFinanceManager:
    def __init__(self, file_name="personal_finance.csv"):
        self.file_name = file_name
        # Create a CSV file if it doesn't exist
        if not os.path.isfile(self.file_name):
            with open(self.file_name, mode='w') as file:
                writer = csv.writer(file)
                writer.writerow(["Type", "Category", "Amount", "Date"])

    def add_entry(self, entry_type, category, amount, date):
        # Append an entry to the CSV file
        with open(self.file_name, mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([entry_type, category, amount, date])

    def show_finance_status(self):
        # Calculate total income, total expense, and balance
        total_income = 0
        total_expense = 0
        with open(self.file_name, 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            for line in csv_reader:
                if line[0].lower() == "income":
                    total_income += float(line[2])
                elif line[0].lower() == "expense":
                    total_expense += float(line[2])
        return total_income, total_expense, total_income - total_expense

    def show_spending_insights(self):
        # Calculate spending by category
        expense_by_category = defaultdict(float)
        with open(self.file_name, 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            for line in csv_reader:
                if line[0].lower() == "expense":
                    expense_by_category[line[1]] += float(line[2])
        return expense_by_category

    def set_budget(self, category, budget):
        # Write the budget to the CSV file
        with open('budget.csv', mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([category, budget])

    def check_budget(self, category, amount):
        # Check if the expense is within the budget
        with open('budget.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == category.lower():
                    if float(row[1]) < amount:
                        return False
        return True
