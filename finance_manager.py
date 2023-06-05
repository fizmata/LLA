import csv
import os
from collections import defaultdict

class PersonalFinanceManager:
    def __init__(self, file_name="personal_finance.csv"):
        self.file_name = file_name
        if not os.path.isfile(self.file_name):
            with open(self.file_name, mode='w') as file:
                writer = csv.writer(file)
                writer.writerow(["Type", "Category", "Amount", "Date"])

    def add_entry(self, entry_type, category, amount, date):
        with open(self.file_name, mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([entry_type, category, amount, date])

    def show_finance_status(self):
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
        expense_by_category = defaultdict(float)
        with open(self.file_name, 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            for line in csv_reader:
                if line[0].lower() == "expense":
                    expense_by_category[line[1]] += float(line[2])

        return expense_by_category
