import streamlit as st

# Настройка страницы и фавикона (иконки в браузере)
st.set_page_config(
    page_title="Blueberry Predictor", 
    page_icon="🫐", 
    layout="centered"
)

# --- Кастомные стили (CSS) для дизайна в стиле голубики ---
st.markdown("""
    <style>
    /* Цвет кнопки - темно-синий / голубичный */
    div.stButton > button:first-child {
        background-color: #2c5297;
        color: white;
        border-radius: 5px;
        width: 100%;
        height: 3em;
        font-weight: bold;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #1e3a6d;
        color: white;
        border: none;
    }
    /* Центрирование заголовка */
    .main-title {
        text-align: center;
        font-weight: bold;
        font-size: 32px;
        margin-bottom: 30px;
    }
    /* Оформление блока результата */
    .result-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border-left: 5px solid #2c5297;
    }
    /* Авторский блок */
    .footer {
        text-align: center;
        color: grey;
        font-size: 14px;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Интерфейс приложения ---

# Заголовок
st.markdown('<div class="main-title">Прогнозирование средней массы ягод<br>голубики высокорослой</div>', unsafe_allow_html=True)

# Изображение голубики (можно заменить на прямую ссылку на фото)
# st.image("https://cdn-icons-png.flaticon.com/512/1043/1043534.png", width=100) # Иконка вместо значка в тексте

# Выбор сорта
cultivar = st.selectbox(
    "Выберите изучаемый сорт:",
    options=["Bonus", "Reka", "Patriot"]
)

# Пустая строка для отступа
st.write("")

# Кнопка расчета
if st.button("Рассчитать"):
    # Коэффициенты модели
    intercept = 1.425
    coeff_reka = 0.398
    coeff_patriot = 0.515
    
    # Расчет
    if cultivar == "Reka":
        predicted_mass = intercept + coeff_reka
    elif cultivar == "Patriot":
        predicted_mass = intercept + coeff_patriot
    else:
        predicted_mass = intercept # Для Bonus
    
    # Вывод результата в стиле скриншота
    st.markdown(f"""
        <div class="result-box">
            <p style="margin:0; font-size:18px;">Прогнозируемая средняя масса ягоды:</p>
            <p style="margin:0; font-size:28px; font-weight:bold; color:#2c5297;">{predicted_mass:.3f} г</p>
        </div>
    """, unsafe_allow_html=True)

# --- Футер с авторами ---
st.markdown('<div class="footer">© Зубик И.Н., Анцупова О.М.</div>', unsafe_allow_html=True)
