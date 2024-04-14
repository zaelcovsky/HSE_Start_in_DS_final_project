![Python Versions](https://img.shields.io/badge/python-3.10--3.11-blue)
![Streamlit version](https://img.shields.io/badge/streamlit-1.33.0-white)
![St Pages](https://img.shields.io/badge/st--pages-0.4.5-white)
![License](https://img.shields.io/github/license/blackary/st_pages)  
  
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hse-start-in-ds-project.streamlit.app/)

## Итоговый проект курса "Старт в Data Science"  
Курс проводится онлайн-магистратурой "Машинное обучение и высоконагруженные системы" ФКН ВШЭ и идет в формате марафона, то есть непрерывного двухмесячного интенсивного обучения.
Курс посвящен изучению основ программирования на языке Python, а также освоению ключевых подходов и инструментов аналитики и визуализации данных (SQL, Pandas, Streamlit).  

В проекте проведен анализ динамики уровня средних зарплат в разрезе по видам экономической деятельности за 2000-2023 годы  в России. Рассмотрены три вида экономической деятельности (в соответствии с ОКВЭД (до 2016 года) и ОКВЭД 2):
1) Строительство  
2) Производство кокса и нефтепродуктов  
3) Образование

Построен график изменения простой и накопленной инфляции по годам.  
Построены графики изменения номинальной начисленной зарплаты по годам для этих видов экономической деятельности.   
Пересчитаны средние зарплаты с учетом уровня инфляции и построены графики изменения реальных начисленных зарплат с учетом инфляции.   
Сделаны выводы.  

В проекте используются открытые данные из официальных источников: 
1) [Росстат](https://rosstat.gov.ru/labor_market_employment_salaries)  
2) [Инфляция в России](https://уровень-инфляции.рф/)  


Первый этап работы выполнен в Jupyter Notebook - [final_project.ipynb](https://github.com/zaelcovsky/HSE_Start_in_DS_final_project/blob/main/notebook/final_project.ipynb)  
Второй этап работы выполнен в виде ```streamlit``` приложения и задеплоен на [Streamlit Community Cloud](https://hse-start-in-ds-project.streamlit.app/)  

Для запуска проекта локально:  
1) Клонируем проект
```shell
git clone https://github.com/zaelcovsky/HSE_Start_in_DS_final_project.git
```
2) Устанавливаем необходимые зависимости
```shell
pip install -r requirements.txt
```
3) Запускаем ```streamlit``` приложениe
```shell
streamlit run app.py
```  
##  
Студент Черепанов С.Ю.