from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from finance_manager import PersonalFinanceManager

class FinanceApp(QWidget):
    def __init__(self, finance_manager):
        super().__init__()

        self.finance_manager = finance_manager

        self.layout = QVBoxLayout()

        self.entry_type_input = QLineEdit()
        self.layout.addWidget(QLabel("Type (Income/Expense):"))
        self.layout.addWidget(self.entry_type_input)

        self.category_input = QLineEdit()
        self.layout.addWidget(QLabel("Category:"))
        self.layout.addWidget(self.category_input)

        self.amount_input = QLineEdit()
        self.layout.addWidget(QLabel("Amount:"))
        self.layout.addWidget(self.amount_input)

        self.date_input = QLineEdit()
        self.layout.addWidget(QLabel("Date (YYYY-MM-DD):"))
        self.layout.addWidget(self.date_input)

        self.add_entry_button = QPushButton("Add Entry")
        self.add_entry_button.clicked.connect(self.add_entry)
        self.layout.addWidget(self.add_entry_button)

        self.show_finance_status_button = QPushButton("Show Finance Status")
        self.show_finance_status_button.clicked.connect(self.show_finance_status)
        self.layout.addWidget(self.show_finance_status_button)

        self.show_spending_insights_button = QPushButton("Show Spending Insights")
        self.show_spending_insights_button.clicked.connect(self.show_spending_insights)
        self.layout.addWidget(self.show_spending_insights_button)

        self.setLayout(self.layout)

    def add_entry(self):
        try:
            self.finance_manager.add_entry(self.entry_type_input.text(), self.category_input.text(), float(self.amount_input.text()), self.date_input.text())
            QMessageBox.information(self, "Success", "Entry added successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show_finance_status(self):
        try:
            income, expense, balance = self.finance_manager.show_finance_status()
            QMessageBox.information(self, "Finance Status", f"Total Income: {income}\nTotal Expense: {expense}\nBalance: {balance}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show_spending_insights(self):
        try:
            insights = self.finance_manager.show_spending_insights()
            insights_str = "\n".join([f"{category}: {amount}" for category, amount in insights.items()])
            QMessageBox.information(self, "Spending Insights", insights_str)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication([])

    finance_manager = PersonalFinanceManager()
    gui = FinanceApp(finance_manager)
    gui.show()

    app.exec()
