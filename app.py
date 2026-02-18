import streamlit as st

# 1. Настройка страницы
st.set_page_config(
    page_title="Blueberry Predictor", 
    page_icon="🫐", 
    layout="centered"
)

# 2. Кастомные стили (Синий цвет голубики и отступы)
st.markdown("""
    <style>
    /* Цвет основной кнопки */
    div.stButton > button:first-child {
        background-color: #2c5297;
        color: white;
        border-radius: 5px;
        width: 100%;
        height: 3.5em;
        font-weight: bold;
        border: none;
        margin-top: 20px;
    }
    div.stButton > button:hover {
        background-color: #1e3a6d;
        color: white;
    }
    /* Центрирование заголовка */
    .main-title {
        text-align: center;
        font-weight: bold;
        font-size: 30px;
        color: #1a1a1a;
        margin-bottom: 40px;
        line-height: 1.2;
    }
    /* Блок с результатом */
    .result-box {
        background-color: #f0f2f6;
        padding: 25px;
        border-radius: 10px;
        text-align: center;
        border-left: 8px solid #2c5297;
        margin-top: 30px;
    }
    /* Подвал */
    .footer {
        text-align: center;
        color: #666666;
        font-size: 14px;
        margin-top: 60px;
        border-top: 1px solid #eeeeee;
        padding-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Интерфейс (Заголовок)
st.markdown('<div class="main-title">Прогнозирование средней массы ягод<br>голубики высокорослой</div>', unsafe_allow_html=True)

# 4. Ввод данных (Центральная колонка)
cultivar = st.selectbox(
    "Выберите изучаемый сорт:",
    options=["Bonus", "Reka", "Patriot"]
)

# ВАЖНО: Поле ввода площади листа
leaf_area = st.number_input(
    "Введите площадь листовой пластинки (см²):",
    min_value=0.1,
    max_value=50.0,
    value=10.0,
    step=0.1
)

# 5. Логика расчета при нажатии кнопки
if st.button("Рассчитать"):
    # Базовая константа (Intercept)
    res = 1.425
    
    # Добавка за сорт
    if cultivar == "Reka":
        res += 0.398
    elif cultivar == "Patriot":
        res += 0.515
    # Для Bonus добавка 0
        
    # Добавка за площадь листа (коэффициент 0.039)
    res += (0.039 * leaf_area)
    
    # Вывод результата
    st.markdown(f"""
        <div class="result-box">
            <p style="margin:0; font-size:18px; color:#444444;">Прогноз средней массы ягоды для сорта <b>{cultivar}</b>:</p>
            <p style="margin:0; font-size:36px; font-weight:bold; color:#2c5297;">{res:.3f} г</p>
        </div>
    """, unsafe_allow_html=True)

# 6. Авторский подвал
st.markdown(f"""
    <div class="footer">
        Методическая справка:<br>
        Данный калькулятор использует уравнение регрессии:<br>
        <b>Y = 1.425 + B(сорт) + 0.039 * X(площадь листа)</b><br><br>
        © Зубик И.Н., Анцупова О.М.
    </div>
""", unsafe_allow_html=True)
