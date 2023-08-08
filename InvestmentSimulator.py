import matplotlib.pyplot as plt

class InvestmentSimulator:
    def __init__(self, duration, inflation_rate, initial_salary, savings_rate, currency="€"):
        """ This class simulates the evolution of investments over time.

        Args:
            duration (int): The duration of the simulation in years.
            inflation_rate (float): The inflation rate in percent.
            initial_salary (float): The initial salary in euros/usd.
            savings_rate (float): The percentage of the salary that is saved each month.
            currency (str): The currency of the simulation.
        """
        self.duration = duration
        self.inflation_rate = inflation_rate / 100
        self.salary_changes = [(0, initial_salary)] 
        self.salary = initial_salary
        self.savings_rate = savings_rate / 100
        self.investments = []
        self.currency = currency

    def change_salary(self, year, new_salary):
        """ Change the salary at a given year.
        
        Args:
            year (int): The year at which the salary is changed.
            new_salary (float): The new salary in euros/usd.
        """
        self.salary_changes.append((year, new_salary))
        self.salary_changes.sort()

    def get_salary_for_year(self, year):
        """ Get the salary for a given year.
        
        Args:
            year (int): The year for which the salary is requested.
        """
        salary = self.salary_changes[0][1]
        for change_year, new_salary in self.salary_changes:
            if change_year > year:
                break
            salary = new_salary
        return salary

    def add_investment(self, name, rate, initial_amount, allocation_percentage, fees=0):
        """ Add an investment to the simulation.
        
        Args:
            name (str): The name of the investment.
            rate (float): The nominal rate of the investment in percent.
            initial_amount (float): The initial amount invested in euros/usd.
            allocation_percentage (float): The percentage of the salary that is invested each month.
            fees (float): The fees of the investment in percent.
        """
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
        """ Calculate the real rate of an investment.
        
        Args:
            nominal_rate (float): The nominal rate of the investment in percent.
            fees (float): The fees of the investment in percent.
        """
        real_rate = ((1 + nominal_rate) / (1 + self.inflation_rate)) - 1
        return real_rate - fees 

    def simulate_investment(self, investment):
        """ Simulate the evolution of an investment over time.
        
        Args:
            investment (dict): The investment to simulate.
        """
        real_rate = self.calculate_real_rate(investment["rate"], investment["fees"])
        final_amount = investment["initial_amount"] * (1 + real_rate) ** self.duration

        for _ in range(self.duration * 12):
            final_amount += investment["monthly_amount"] * (1 + real_rate) ** (_ // 12)

        return final_amount

    def simulate(self):
        """ Simulate the evolution of all investments over time. """
        results = []

        for investment in self.investments:
            final_amount = self.simulate_investment(investment)
            results.append((investment["name"], final_amount))

        return results

    def plot_investments(self):
        """ Plot the evolution of all investments over time. """
        total_final_amounts = [0] * (self.duration + 1)

        for investment in self.investments:
            final_amounts = []
            years = list(range(self.duration + 1))
            for year in years:
                final_amount = self.simulate_investment(investment, year)
                final_amounts.append(final_amount)
                total_final_amounts[year] += final_amount

                salary = self.get_salary_for_year(year)
                investment["monthly_amount"] = salary * self.savings_rate * investment["allocation_percentage"]

            plt.plot(years, final_amounts, label=investment["name"])

        plt.plot(years, total_final_amounts, label="Total", linestyle="--")

        plt.xlabel("Year")
        plt.ylabel("Amount ({})".format(self.currency))
        plt.title("Evolution of investments over time")
        plt.legend()
        plt.show()


    def simulate_investment(self, investment, duration=None):
        """ Simulate the evolution of an investment over time.
        
        Args:
            investment (dict): The investment to simulate.
            duration (int): The duration of the simulation in years.
        """
        if duration is None:
            duration = self.duration

        final_amount = investment["initial_amount"]
        monthly_amount = self.salary * self.savings_rate * investment["allocation_percentage"]

        for _ in range(duration * 12):
            salary = self.get_salary_for_year(_ // 12)
            monthly_amount = salary * self.savings_rate * investment["allocation_percentage"]
            final_amount += monthly_amount * (1 + investment["rate"] - self.inflation_rate) ** (_ // 12)

        return final_amount

if __name__ == "__main__":
    
    # Exemple d'utilisation
    simulator = InvestmentSimulator(duration=100, inflation_rate=6, initial_salary=1500, savings_rate=50)
    
    simulator.add_investment("Livret A", rate=3, initial_amount=1000, allocation_percentage=30)
    simulator.add_investment("PEA", rate=10, initial_amount=500, allocation_percentage=40, fees=0.5)
    simulator.add_investment("PEL", rate=6, initial_amount=7000, allocation_percentage=30, fees=0.7)

    simulator.change_salary(1, 500)
    simulator.change_salary(5, 3500)
    simulator.change_salary(7, 100)
    

    results = simulator.simulate()
    print(results)
    simulator.plot_investments()

    #help(InvestmentSimulator)