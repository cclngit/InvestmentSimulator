import matplotlib.pyplot as plt

class InvestmentSimulator:
    def __init__(self, duration, inflation_rate, initial_salary, savings_rate):
        self.duration = duration
        self.inflation_rate = inflation_rate / 100
        self.salary_changes = [(0, initial_salary)]  # (année, salaire)
        self.salary = initial_salary
        self.savings_rate = savings_rate / 100
        self.investments = []

    def change_salary(self, year, new_salary):
        self.salary_changes.append((year, new_salary))
        self.salary_changes.sort()

    def get_salary_for_year(self, year):
        salary = self.salary_changes[0][1]
        for change_year, new_salary in self.salary_changes:
            if change_year > year:
                break
            salary = new_salary
        return salary

    def add_investment(self, name, rate, initial_amount, allocation_percentage, fees=0):
        monthly_amount = self.salary * self.savings_rate * (allocation_percentage / 100)
        self.investments.append({
            "name": name,
            "rate": rate / 100,
            "initial_amount": initial_amount,
            "monthly_amount": monthly_amount,
            "allocation_percentage": allocation_percentage / 100,
            "fees": fees / 100
        })

    def calculate_real_rate(self, nominal_rate, fees):
        real_rate = ((1 + nominal_rate) / (1 + self.inflation_rate)) - 1
        return real_rate - fees 

    def simulate_investment(self, investment):
        real_rate = self.calculate_real_rate(investment["rate"], investment["fees"])
        final_amount = investment["initial_amount"] * (1 + real_rate) ** self.duration

        for _ in range(self.duration * 12):
            final_amount += investment["monthly_amount"] * (1 + real_rate) ** (_ // 12)

        return final_amount

    def simulate(self):
        results = []

        for investment in self.investments:
            final_amount = self.simulate_investment(investment)
            results.append((investment["name"], final_amount))

        return results

    def plot_investments(self):
        total_final_amounts = [0] * (self.duration + 1)

        for investment in self.investments:
            final_amounts = []
            years = list(range(self.duration + 1))
            for year in years:
                final_amount = self.simulate_investment(investment, year)
                final_amounts.append(final_amount)
                total_final_amounts[year] += final_amount

                # Mise à jour des montants investis pour toute modification de salaire
                salary = self.get_salary_for_year(year)
                investment["monthly_amount"] = salary * self.savings_rate * investment["allocation_percentage"]

            plt.plot(years, final_amounts, label=investment["name"])

        plt.plot(years, total_final_amounts, label="Total", linestyle="--")

        plt.xlabel("Années")
        plt.ylabel("Montant Accumulé (€)")
        plt.title("Évolution des investissements au fil du temps")
        plt.legend()
        plt.show()


    def simulate_investment(self, investment, duration=None):
        if duration is None:
            duration = self.duration

        real_rate = self.calculate_real_rate(investment["rate"], investment["fees"])
        final_amount = investment["initial_amount"] * (1 + real_rate) ** duration

        for _ in range(duration * 12):
            final_amount += investment["monthly_amount"] * (1 + real_rate) ** (_ // 12)

        return final_amount


# Exemple d'utilisation
simulator = InvestmentSimulator(duration=20, inflation_rate=6, initial_salary=1500, savings_rate=50)
simulator.add_investment("Livret A", rate=3, initial_amount=1000, allocation_percentage=30)
simulator.add_investment("PEA", rate=10, initial_amount=500, allocation_percentage=40, fees=0.5)
simulator.add_investment("PEL", rate=6, initial_amount=7000, allocation_percentage=30, fees=0.7)

simulator.change_salary(2, 500)
#simulator.change_salary(10, 3500)

results = simulator.simulate()
simulator.plot_investments()