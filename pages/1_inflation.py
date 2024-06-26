import streamlit as st
import matplotlib.pyplot as plt
from app import all_data


def inflation_plot():
    # Построение линейного графика
    fig, ax1 = plt.subplots(figsize=(20, 8))

    # Записываем данные из необходимых столбцов в переменные
    x1 = all_data['Год']
    y1 = all_data['Инфляция']

    x2 = all_data['Год']
    y2 = all_data['Накопленная инфляция']

    # Добавляем первый график Накопленной инфляции
    ax1.plot(x2, y2, color='tab:blue')

    # Заголовок графика
    plt.title("Накопленная и простая инфляция за 2000-2023 гг.", fontsize=15, y=1.04)

    # Подпись каждой из осей первого графика
    ax1.set_xlabel("Годы", fontsize=14)
    ax1.set_ylabel("Накопленная инфляция, %", fontsize=14, color='tab:blue')

    # Настраиваем первый график
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    ymarks_2 = range(0, 1000, 50)
    ax1.set_yticks(ymarks_2)
    ax1.fill_between(x2, y2, alpha = 0.8)
    plt.grid()

    # Добавляем второй график простой инфляции
    ax2 = ax1.twinx()
    ax2.plot(x1, y1, color='tab:red', linewidth=2, marker='.', markeredgecolor='red', markersize=14.0)

    # Настраиваем второй график
    ax2.set_ylabel("Инфляция, %", fontsize=14, color='tab:red')
    ymarks = range(0, 25)
    ax2.set_yticks(ymarks)
    ax2.tick_params(axis='y', labelcolor='tab:red')

    # Отрегулируем графики между собой
    fig.tight_layout()

    # Разворачиваем отметки на оси x на 45 градусов
    plt.xticks(rotation=45)

    # Отображаем весь результат
    st.pyplot(fig)


# Заголовок
st.write("## Накопленная и простая инфляция за 2000-2023 годы")

# Текст
st.markdown(
    """
    Ниже отображен смежный график накопленной и простой инфляции за 2000-2023 годы. Инфляция с 2000 по 2023 год составила 793,8% (то есть цены за 23 года выросли немного меньше, чем в 9 раз).  
    """
)

# График
inflation_plot()

# Датасет
with st.expander("Датасет по инфляции"):
    st.dataframe(all_data.style.format({
                     "Год": "{}", # Show no formatting
                     "Инфляция": "{:.2f}",  # Show a float with two decimals
                     "Накопленная инфляция": "{:.2f}"
                 }),
                 hide_index=True,
                 column_order=(
                     "Год",
                     "Инфляция",
                     "Накопленная инфляция")
                 )

# Текст
st.markdown(
    """
    Давайте поймем, в чем состоит проблема вычисления инфляции за определенный период времени. Индексы потребительских цен (ИПЦ) рассчитываются органами статистики помесячно. Но если за январь рост цен составил 1%, а за февраль 2%, то, очевидно, нельзя просто сложить эти два значения и сказать, что с января по март инфляция составила 3%. Ведь прирост на начало марта считается к уровню начала февраля, а не января. Корректный расчет накопленной инфляции выглядит так:
     """
)
st.latex(
    r"""
    (1,01* 1,02 - 1) * 100 \%
    """
)
st.markdown(
    """
    то есть инфляция за два месяца составила 3,02%. Аналогичным образом считается и накопленная инфляция по годам. Чем длиннее ряд, тем больше будет отклонение от простой арифметической суммы.
    """
)
