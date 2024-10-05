import math

# Ймовірність для кожного варіанту
p = 0.5

# Зарплати для першого варіанту (ризикового)
salary_1_low = 1000
salary_1_high = 3000

# Зарплата для другого варіанту (безризикового)
salary_2 = 2000

# Функція корисності U(x) = sqrt(x)
def utility(x):
    return math.sqrt(x)

# Функція для сподіваної корисності ризикового варіанту
def expected_utility_risk(salary_low, salary_high, p):
    u_low = utility(salary_low)  # Корисність для зарплати 1000
    u_high = utility(salary_high)  # Корисність для зарплати 3000

    # Сподівана корисність
    expected_utility = p * u_low + (1 - p) * u_high
    return expected_utility

# Основна функція для порівняння двох варіантів
def main():
    # Корисність для ризикового варіанту
    risk_utility = expected_utility_risk(salary_1_low, salary_1_high, p)
    print(f"Сподівана корисність для ризикового варіанту: {risk_utility:.2f}")

    # Корисність для безризикового варіанту
    no_risk_utility = utility(salary_2)
    print(f"Корисність для безризикового варіанту: {no_risk_utility:.2f}")

    # Порівняння варіантів
    if risk_utility > no_risk_utility:
        print("Особі краще обрати перший варіант (ризиковий).")
    else:
        print("Особі краще обрати другий варіант (безризиковий).")

main()
