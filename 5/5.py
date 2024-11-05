import numpy as np
import pandas as pd

# Дані
crops = ["Жито", "Овес", "Пшениця", "Гречка"]
profits = np.array([
    [15, 12, 9, 6],   # Жито
    [19, 13, 10, 7],  # Овес
    [20, 12, 12, 8],  # Пшениця
    [21, 15, 8, 6]    # Гречка
])

# Ймовірності станів економічного середовища
probabilities = np.array([0.3, 0.2, 0.3, 0.2])

# Розрахунок середнього значення, дисперсії та коефіцієнта варіації для кожної культури
mean_profits = np.dot(profits, probabilities)  # Середні прибутки
variances = np.dot((profits - mean_profits[:, None])**2, probabilities)  # Дисперсії
std_devs = np.sqrt(variances)  # Стандартні відхилення
coeff_variations = std_devs / mean_profits  # Коефіцієнти варіації

# Створення таблиці результатів
results = pd.DataFrame({
    "Культура": crops,
    "Середній прибуток": mean_profits,
    "Дисперсія": variances,
    "Стандартне відхилення": std_devs,
    "Коефіцієнт варіації": coeff_variations
})

# Пошук культури з мінімальною дисперсією та мінімальним коефіцієнтом варіації
min_variance_crop = results.loc[results["Дисперсія"].idxmin()]
min_coeff_variation_crop = results.loc[results["Коефіцієнт варіації"].idxmin()]

# Виведення результатів
print("Таблиця результатів:")
print(results)
print("\nКультура з мінімальною дисперсією:")
print(min_variance_crop)
print("\nКультура з мінімальним коефіцієнтом варіації:")
print(min_coeff_variation_crop)
