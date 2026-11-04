import pandas as pd
import numpy as np

# Генерируем фейковые данные для проекта по Clash Royale
np.random.seed(42)
n_rows = 500

cards_pool = [
    'Electro Giant (Evol)', 'Royal Giant (Evol)', 'Wizard', 
    'Ice Wizard', 'Skeleton Army', 'Arrows', 'Cannon', 'Royal Recruits'
]

data = {
    'match_id': range(1, n_rows + 1),
    'card_name': np.random.choice(cards_pool, n_rows),
    'player_trophies': np.random.randint(5000, 13000, n_rows),
    'win_rate': np.random.uniform(45.0, 68.0, n_rows),
    'card_level': np.random.randint(11, 16, n_rows),
    'evolution_used': np.random.choice([True, False], n_rows, p=[0.4, 0.6])
}

df = pd.DataFrame(data)

# Сохраняем в CSV-файл
df.to_csv('clash_royale_stats.csv', index=False)
print("Файл clash_royale_stats.csv успешно создан!")
