import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

ru_card_map = {
    'Electro Giant (Evol)': 'Электрогигант (эволюция)',
    'Электро гигант (эволюция)': 'Электрогигант (эволюция)',
    'Электрогигант (Эвол)': 'Электрогигант (эволюция)',
    'Royal Giant (Evol)': 'Королевский гигант (эволюция)',
    'Королевский гигант (эволюция)': 'Королевский гигант (эволюция)',
    'Wizard': 'Волшебник',
    'Ice Wizard': 'Ледяной волшебник',
    'Ледяной Волшебник': 'Ледяной волшебник',
    'Skeleton Army': 'Армия скелетов',
    'Армия Скелетов': 'Армия скелетов',
    'Arrows': 'Стрелы',
    'Cannon': 'Пушка',
    'Royal Recruits': 'Королевские рекруты',
}

heroes_pool = [
    'Герой Колдун',
    'Герой Рыцарь',
    'Герой Валькирия',
    'Герой Мушкетёр',
    'Остальные',
]

evolutions_pool = [
    'Электрогигант (эволюция)',
    'Королевский гигант (эволюция)',
    'Королевские рекруты (эволюция)',
    'Скелеты (эволюция)',
    'Варвары (эволюция)',
    'Остальные',
]

normal_cards_pool = [
    'Волшебник',
    'Ледяной волшебник',
    'Армия скелетов',
    'Стрелы',
    'Пушка',
    'Королевские рекруты',
    'Всадник на кабане',
    'Мега рыцарь',
    'Мини П.Е.К.К.А.',
    'Бревно',
    'Огненный шар',
    'Гоблинская бочка',
    'Электродух',
    'Тесла',
    'Остальные',
]


def make_rows(cards_list, category_name, n=180):
    evo_flag = category_name == 'evolution'
    weights = np.ones(len(cards_list), dtype=float)
    if 'Остальные' in cards_list:
        idx = cards_list.index('Остальные')
        weights[idx] = max(2.0, len(cards_list) * 0.4)
    probs = weights / weights.sum()

    # Генерируем реалистичный винрейт в районе ~48–68%
    wr = np.clip(np.random.normal(loc=56.5, scale=5.2, size=n), 45.0, 69.5)

    return pd.DataFrame({
        'match_id': np.arange(1, n + 1),
        'card_name': np.random.choice(cards_list, size=n, p=probs),
        'card_type': category_name,
        'player_trophies': np.random.randint(5000, 13000, size=n),
        'win_rate': wr,
        'card_level': np.random.randint(11, 16, size=n),
        'evolution_used': evo_flag if evo_flag else np.random.choice([False, True], size=n, p=[0.8, 0.2]),
    })


if os.path.exists('clash_royale_stats_ru.csv'):
    df = pd.read_csv('clash_royale_stats_ru.csv')
else:
    if os.path.exists('clash_royale_stats.csv'):
        base_df = pd.read_csv('clash_royale_stats.csv')
        base_df['card_name'] = base_df['card_name'].astype(str).str.strip().replace(ru_card_map)
        if 'win_rate' not in base_df.columns:
            base_df['win_rate'] = np.random.uniform(46.0, 67.5, size=len(base_df))
        if 'match_id' not in base_df.columns:
            base_df['match_id'] = np.arange(1, len(base_df) + 1)
        base_df['card_type'] = np.where(
            base_df['card_name'].str.lower().str.contains('эволюц'),
            'evolution',
            'normal',
        )
    else:
        base_df = make_rows(normal_cards_pool, 'normal', n=250)

    extra_heroes = make_rows(heroes_pool, 'hero', n=180)
    extra_evos = make_rows(evolutions_pool, 'evolution', n=200)
    extra_normal = make_rows(normal_cards_pool, 'normal', n=250)

    df = pd.concat([base_df, extra_heroes, extra_evos, extra_normal], ignore_index=True)
    df['match_id'] = np.arange(1, len(df) + 1)
    df.to_csv('clash_royale_stats_ru.csv', index=False)

df['card_name'] = df['card_name'].astype(str).str.strip().replace(ru_card_map)
df['win_rate'] = pd.to_numeric(df['win_rate'], errors='coerce')
df = df.dropna(subset=['card_name', 'win_rate'])


def prepare_pie_data(sub_df, max_named=10):
    s = sub_df.groupby('card_name').size()
    others_val = float(s.get('Остальные', 0.0))
    named = s.drop(index=['Остальные'], errors='ignore').sort_values(ascending=False)

    if len(named) > max_named:
        others_val += float(named.iloc[max_named:].sum())
        named = named.iloc[:max_named]

    if others_val > 0:
        named = pd.concat([named, pd.Series({'Остальные': others_val})])

    return named


def plot_pie(ax, series, title):
    wedges, texts, autotexts = ax.pie(
        series.values,
        labels=series.index,
        autopct='%1.1f%%',
        startangle=140,
        pctdistance=0.75,
        textprops={'fontsize': 9},
    )
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(8.5)
        autotext.set_fontweight('bold')

    ax.set_title(title, fontsize=11, fontweight='bold', pad=12)
    ax.axis('equal')


df_heroes = df[df['card_type'] == 'hero']
df_evo = df[df['card_type'] == 'evolution']
df_normal = df[df['card_type'] == 'normal']

fig1, axes1 = plt.subplots(1, 3, figsize=(19, 6.5))
plot_pie(axes1[0], prepare_pie_data(df_heroes, max_named=10), '1. Герои: популярность использования')
plot_pie(axes1[1], prepare_pie_data(df_evo, max_named=10), '2. Эволюции: популярность использования')
plot_pie(axes1[2], prepare_pie_data(df_normal, max_named=10), '3. Обычные карты (топ-10 + остальные)')
fig1.suptitle('Популярность использования карт', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('charts_popularity_3pie.png', dpi=150)


# --- БЛОК 2: 3 столбчатых графика процента побед (топ-10 без «Остальные», по возрастанию) ---
def top_winrate_ascending(sub_df, top_n=10):
    # Исключаем «Остальные», берём топ-N по среднему win_rate и сортируем от меньшего к большему
    filtered = sub_df[sub_df['card_name'].str.lower() != 'остальные']
    means = filtered.groupby('card_name')['win_rate'].mean()
    top_cards = means.sort_values(ascending=False).head(top_n)
    return top_cards.sort_values(ascending=True)


def plot_ascending_bars(ax, series, title, color):
    if series.empty:
        ax.text(0.5, 0.5, 'Нет данных', ha='center', va='center', fontsize=11, color='gray')
        ax.set_title(title, fontsize=11, fontweight='bold')
        return

    x = np.arange(len(series))
    bars = ax.bar(x, series.values, color=color, edgecolor='black', linewidth=0.6)

    ax.set_xticks(x)
    ax.set_xticklabels(series.index, rotation=30, ha='right', fontsize=9)
    ax.set_ylabel('Средний процент побед (%)', fontsize=10)
    ax.set_title(title, fontsize=11, fontweight='bold', pad=10)
    ax.grid(axis='y', linestyle='--', alpha=0.4)

    y_min = max(0.0, np.floor((series.min() - 3.0) / 2.0) * 2.0)
    y_max = min(100.0, np.ceil((series.max() + 2.5) / 2.0) * 2.0)
    ax.set_ylim(y_min, y_max)

    for bar, val in zip(bars, series.values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            val + 0.3,
            f'{val:.1f}%',
            ha='center',
            va='bottom',
            fontsize=8.5,
            fontweight='bold',
        )


fig2, axes2 = plt.subplots(1, 3, figsize=(20, 6.5))
plot_ascending_bars(
    axes2[0],
    top_winrate_ascending(df_heroes, top_n=10),
    '4. Герои: топ по % побед (по возрастанию)',
    color='#4C72B0',
)
plot_ascending_bars(
    axes2[1],
    top_winrate_ascending(df_evo, top_n=10),
    '5. Эволюции: топ по % побед (по возрастанию)',
    color='#DD8452',
)
plot_ascending_bars(
    axes2[2],
    top_winrate_ascending(df_normal, top_n=10),
    '6. Обычные карты (топ-10): % побед по возрастанию',
    color='#55A868',
)
fig2.suptitle('Процент побед по группам карт — от меньшего к большему', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('charts_winrate_bars.png', dpi=150)

plt.show()
