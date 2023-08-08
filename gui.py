import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from InvestmentSimulator import InvestmentSimulator
import matplotlib.pyplot as plt

class InvestmentSimulatorGUI:
    def __init__(self):
        self.simulator = None

        self.root = tk.Tk()
        self.root.title("Investment Simulator")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

        # Create the pages in the notebook
        self.initiate_page = ttk.Frame(self.notebook)
        self.add_investment_page = ttk.Frame(self.notebook)
        self.plot_chart_page = ttk.Frame(self.notebook)

        self.notebook.add(self.initiate_page, text="Initiate")
        self.notebook.add(self.add_investment_page, text="Add Investment")
        self.notebook.add(self.plot_chart_page, text="Plot Chart")

        # Create the widgets for the initiate page
        self.duration_label = tk.Label(self.initiate_page, text="Duration (years):")
        self.duration_entry = tk.Entry(self.initiate_page)

        self.inflation_rate_label = tk.Label(self.initiate_page, text="Inflation Rate (%):")
        self.inflation_rate_entry = tk.Entry(self.initiate_page)

        self.initial_salary_label = tk.Label(self.initiate_page, text="Initial Salary ({currency}):")
        self.initial_salary_entry = tk.Entry(self.initiate_page)

        self.savings_rate_label = tk.Label(self.initiate_page, text="Savings Rate (%):")
        self.savings_rate_entry = tk.Entry(self.initiate_page)

        self.initiate_button = tk.Button(self.initiate_page, text="Initiate", command=self.initiate_simulator)

        self.duration_label.pack()
        self.duration_entry.pack()

        self.inflation_rate_label.pack()
        self.inflation_rate_entry.pack()

        self.initial_salary_label.pack()
        self.initial_salary_entry.pack()

        self.savings_rate_label.pack()
        self.savings_rate_entry.pack()

        self.initiate_button.pack()

        # Create the widgets for the add investment page
        self.investment_name_label = tk.Label(self.add_investment_page, text="Investment Name:")
        self.investment_name_entry = tk.Entry(self.add_investment_page)

        self.investment_rate_label = tk.Label(self.add_investment_page, text="Investment Rate (%):")
        self.investment_rate_entry = tk.Entry(self.add_investment_page)

        self.initial_amount_label = tk.Label(self.add_investment_page, text="Initial Amount ({currency}):")
        self.initial_amount_entry = tk.Entry(self.add_investment_page)

        self.allocation_percentage_label = tk.Label(self.add_investment_page, text="Allocation Percentage (%):")
        self.allocation_percentage_entry = tk.Entry(self.add_investment_page)

        self.fees_label = tk.Label(self.add_investment_page, text="Fees (%):")
        self.fees_entry = tk.Entry(self.add_investment_page)

        self.add_investment_button = tk.Button(self.add_investment_page, text="Add Investment", command=self.add_investment)

        self.investment_name_label.pack()
        self.investment_name_entry.pack()

        self.investment_rate_label.pack()
        self.investment_rate_entry.pack()

        self.initial_amount_label.pack()
        self.initial_amount_entry.pack()

        self.allocation_percentage_label.pack()
        self.allocation_percentage_entry.pack()

        self.fees_label.pack()
        self.fees_entry.pack()

        self.add_investment_button.pack()

        # Create the widgets for the plot chart page
        self.plot_button = tk.Button(self.plot_chart_page, text="Plot Chart", command=self.plot_chart)

        self.plot_button.pack()

        self.root.mainloop()

    def initiate_simulator(self):
        duration = int(self.duration_entry.get())
        inflation_rate = float(self.inflation_rate_entry.get())
        initial_salary = float(self.initial_salary_entry.get())
        savings_rate = float(self.savings_rate_entry.get())

        self.simulator = InvestmentSimulator(duration, inflation_rate, initial_salary, savings_rate)

    def add_investment(self):
        investment_name = self.investment_name_entry.get()
        investment_rate = float(self.investment_rate_entry.get())
        initial_amount = float(self.initial_amount_entry.get())
        allocation_percentage = float(self.allocation_percentage_entry.get())
        fees = float(self.fees_entry.get())

        if self.simulator is None:
            messagebox.showerror("Error", "Please initiate the simulator first.")
        else:
            self.simulator.add_investment(investment_name, investment_rate, initial_amount, allocation_percentage, fees)
            messagebox.showinfo("Success", "Investment has been added successfully.")

    def plot_chart(self):
        if self.simulator is None or not self.simulator.investments:
            messagebox.showerror("Error", "Please initiate the simulator and add at least one investment.")
        else:
            results = self.simulator.simulate()
            self.simulator.plot_investments()

            names = [result[0] for result in results]
            amounts = [result[1] for result in results]

            plt.bar(names, amounts)
            plt.xlabel("Investment")
            plt.ylabel("Final Amount")
            plt.title("Investment Simulation")
            plt.tight_layout()
            plt.show()


if __name__ == "__main__":
    InvestmentSimulatorGUI()