import streamlit as st
import matplotlib.pyplot as plt
from app import all_data
from matplotlib.ticker import MultipleLocator


def building_plot():
    # Строим каркас для подграфиков
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(25, 20))
    plt.subplots_adjust(wspace=0.0, hspace=0.3)

    # Записываем данные из необходимых столбцов в переменные для Строительство (номинальная зарплата)
    x1 = all_data['Год']
    y1 = all_data['Строительство (номинальная зарплата)']

    # Записываем данные из необходимых столбцов в переменные для Строительство (реальная зарплата)
    x2 = all_data['Год']
    y2 = all_data['Строительство (реальная зарплата)']

    # Строим графики на разных осях
    g1 = ax1.bar(x1, y1, color='tab:green', width=1.0, edgecolor='black')
    ax1.bar_label(g1, [''] + [f'{(y1 - y0) / y0 * 100:+.2f}%' for y0, y1 in zip(y1[:-1], y1[1:])], padding=5,
                  fontsize=8)
    # ax1.margins(y=0.1)

    g2 = ax2.bar(x2, y2, color='tab:green', width=1.0, edgecolor='black')
    ax2.bar_label(g2, [''] + [f'{(y1 - y0) / y0 * 100:+.2f}%' for y0, y1 in zip(y2[:-1], y2[1:])], padding=5,
                  fontsize=8)
    # ax1.margins(y=0.1)

    # Даем названия каждому набору осей
    ax1.set_title('Строительство\n\n(номинальная заработная плата за 2000-2023 годы)', y=1.04)
    ax2.set_title('Строительство\n\n(реальная заработная плата за 2000-2023 годы)', y=1.04)

    # Подписываем x-оси
    ax1.set_xlabel('Годы')
    ax2.set_xlabel('Годы')

    # Подписываем y-оси
    ax1.set_ylabel('Рублей')
    ax2.set_ylabel('Рублей')

    # Разворачиваем отметки на осях x
    ax1.set_xticks(all_data['Год'])
    ax2.set_xticks(all_data['Год'])

    # Добавление корректных интервалов по осям y
    ymarks = range(0, 110000, 10000)
    ax1.set_yticks(ymarks)
    ax2.set_yticks(ymarks)

    # Добавление доп тикеров осям y
    ax1.yaxis.set_minor_locator(MultipleLocator(5000))
    ax2.yaxis.set_minor_locator(MultipleLocator(5000))

    # Отображаем весь результат
    st.pyplot(fig)


# Заголовок
st.write("## Номинальная и реальная заработная плата по Строительству за 2000-2023 годы")

# Текст
st.markdown(
    """
    Ниже отображены графики номинальной и реальной заработной платы по Строительству за 2000-2023 годы. На графиках показан ежегодный прирост заработной платы в процентах. 
    """
)

# График
building_plot()

# Датасет
with st.expander("Датасет по Строительству"):
    st.dataframe(all_data.style.format({
                     "Год": "{}", # Show no formatting
                     "Инфляция": "{:.2f}",  # Show a float with two decimals
                     "Накопленная инфляция": "{:.2f}",
                     "Строительство (индекс реальной зарплаты)": "{:.2f}",
                     "Строительство (реальная зарплата)": "{}",
                     "Строительство (номинальная зарплата)": "{}"
                 }),
                 hide_index=True,
                 column_order=(
                     "Год",
                     "Инфляция",
                     "Накопленная инфляция",
                     "Строительство (индекс реальной зарплаты)",
                     "Строительство (реальная зарплата)",
                     "Строительство (номинальная зарплата)")
                 )

# Вывод
st.markdown(
    """
    #### Выводы  
    По Строительству номинальные начисленные зарплаты показывают рост год от года, однако в 2009 году номинальная зарплата в Строительстве показала снижение на 2.43% по сравнению с 2008 годом. Скорее всего сыграла роль 
    [финансово-экономического кризиса в России (2008—2010)](https://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%BD%D0%B0%D0%BD%D1%81%D0%BE%D0%B2%D0%BE-%D1%8D%D0%BA%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D1%80%D0%B8%D0%B7%D0%B8%D1%81_%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8_(2008%E2%80%942010)#%D0%A1%D1%82%D1%80%D0%BE%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D1%82%D0%B2%D0%BE). 
    В целом, номинальные начисленные зарплаты в Строительстве росли в пределах 2.06-46.2%.     
    Ожидаемо с учетом инфляции рост зарплаты выражен слабее. Также, помимо снижения заработной платы в 2009 году, увиденного нами на графике номинальной заработной платы, добавилось снижение в 2015 году по сравнению с 2014 годом на 2.34%. 
    Скорее всего повлиял скачок инфляции 2014-2015 годов и внешнеполитические вызовы. В целом, реальные начисленные зарплаты в Строительстве росли в пределах 2.34-34.17%.
    """
)