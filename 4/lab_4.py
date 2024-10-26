import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Дані про акції
m = np.array([0.20, 0.40, 0.60])  # Сподівані норми прибутку
sigma = np.array([0.10, 0.18, 0.30])  # Середньоквадратичні відхилення
rho = np.array([[1, 1, -1],  # Кореляційна матриця
                [1, 1, -1],
                [-1, -1, 1]])

# Коваріаційна матриця
cov_matrix = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        cov_matrix[i, j] = sigma[i] * sigma[j] * rho[i, j]

# Функція для обчислення ризику портфеля
def portfolio_risk(x, cov_matrix):
    return np.sqrt(np.dot(x.T, np.dot(cov_matrix, x)))

# Функція для обчислення прибутку портфеля
def portfolio_return(x, m):
    return np.dot(x, m)

# Умова рівності суми ваг до 1
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# Обмеження для ваг (ваги повинні бути в межах від 0 до 1)
bounds = tuple((0, 1) for _ in range(3))

# Початкові припущення для ваг
x0 = np.array([1/3, 1/3, 1/3])

# Мінімізація ризику з обмеженням на максимальний прибуток
result = minimize(portfolio_risk, x0, args=(cov_matrix,), method='SLSQP', bounds=bounds, constraints=constraints)

# Оптимальні ваги для мінімального ризику
optimal_weights = result.x
max_risk_return = portfolio_return(optimal_weights, m)
min_risk = portfolio_risk(optimal_weights, cov_matrix)

# Генерація множини допустимих і ефективних портфелів
returns = []
risks = []
for weight1 in np.linspace(0, 1, 50):
    for weight2 in np.linspace(0, 1 - weight1, 50):
        weight3 = 1 - weight1 - weight2
        weights = np.array([weight1, weight2, weight3])
        ret = portfolio_return(weights, m)
        risk = portfolio_risk(weights, cov_matrix)
        returns.append(ret)
        risks.append(risk)

# Перетворення результатів у масиви для побудови графіків
returns = np.array(returns)
risks = np.array(risks)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.scatter(risks, returns, c=returns/risks, marker='o')
plt.colorbar(label='Коефіцієнт Шарпа')
plt.scatter(min_risk, max_risk_return, color='red', marker='*', s=200, label='Макс. прибуток, мін. ризик')
plt.xlabel('Ризик (σ)')
plt.ylabel('Сподівана норма прибутку (m)')
plt.title('Множини допустимих та ефективних портфелів')
plt.legend()
plt.show()

# Виведення результатів
optimal_weights, max_risk_return, min_risk
