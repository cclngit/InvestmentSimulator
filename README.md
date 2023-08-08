# Investment Simulator

<p align="center">
<img src="https://img.shields.io/badge/Last_commit-july_2023-yellow" />
&nbsp;
<img src="https://img.shields.io/badge/Build-passing-Lime" />
&nbsp;
<img src="https://img.shields.io/badge/Licence-MIT-orange" />
&nbsp;
<a href="https://bmc.link/MoreThanRobots" target="_blank"><img src="https://img.shields.io/badge/Buy_me_a_coffe-$-blue" /></a>
</p>

The Investment Simulator is a Python class that allows you to simulate the evolution of investments over time. It takes into account factors such as inflation rate, salary changes, investment rates, and fees to provide a realistic projection of investment growth.

## Installation

To use the Investment Simulator, simply copy the `investment_simulator.py` file into your project directory. 

## Usage

To use the Investment Simulator, first create an instance of the `InvestmentSimulator` class:

```python
simulator = InvestmentSimulator(duration, inflation_rate, initial_salary, savings_rate, currency)
```

- `duration` (int): The duration of the simulation in years.
- `inflation_rate` (float): The inflation rate in percent.
- `initial_salary` (float): The initial salary in euros/usd.
- `savings_rate` (float): The percentage of the salary that is saved each month.
- `currency` (str): The currency of the simulation.

Next, you can add investments to the simulation using the `add_investment` method:

```python
simulator.add_investment(name, rate, initial_amount, allocation_percentage, fees)
```

- `name` (str): The name of the investment.
- `rate` (float): The nominal rate of the investment in percent.
- `initial_amount` (float): The initial amount invested in euros/usd.
- `allocation_percentage` (float): The percentage of the salary that is invested each month.
- `fees` (float): The fees of the investment in percent.

You can also change the salary at specific years using the `change_salary` method:

```python
simulator.change_salary(year, new_salary)
```

- `year` (int): The year at which the salary is changed.
- `new_salary` (float): The new salary in euros/usd.

To simulate the evolution of investments over time, use the `simulate` method:

```python
results = simulator.simulate()
```

The `simulate` method returns a list of tuples, where each tuple represents an investment and its final amount.

To plot the evolution of investments over time, use the `plot_investments` method:

```python
simulator.plot_investments()
```

This will generate a plot showing the evolution of each investment, as well as the total amount over time.

## Example

Here's an example of how to use the Investment Simulator:

```python
simulator = InvestmentSimulator(duration=20, inflation_rate=2, initial_salary=2000, savings_rate=40)

simulator.add_investment("Stocks", rate=8, initial_amount=5000, allocation_percentage=50)
simulator.add_investment("Bonds", rate=4, initial_amount=3000, allocation_percentage=30)
simulator.add_investment("Real Estate", rate=6, initial_amount=10000, allocation_percentage=20)

results = simulator.simulate()

print(results)

simulator.plot_investments()
```

This example simulates the evolution of three investments (stocks, bonds, and real estate) over a period of 20 years. The inflation rate is set to 2%, and the initial salary is 2000 euros/usd. The savings rate is 40%, meaning 40% of the salary is saved each month. The investments have different rates of return and allocation percentages. The `simulate` method returns a list of tuples, where each tuple represents an investment and its final amount. The `plot_investments` method generates a plot showing the evolution of each investment over time.

## Contributing

Contributions to the Investment Simulator are welcome! If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request.

## License

The Investment Simulator is open source and available under the [MIT License](https://github.com/cclngit/InvestmentSimulator/blob/main/LICENSE). Feel free to use, modify, and distribute the code as needed.