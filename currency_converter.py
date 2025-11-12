import streamlit as st


st.title("Конвертер валют")
col1, col2 = st.columns(2)
amount = col2.number_input("", min_value=0.0, value=1.0, step=1.0)
rates = {
    "EUR": 94,
    "USD": 81
}
currency = col1.selectbox("Валюта", options=list(rates.keys()))
st.success(f"{amount * rates[currency]} RUB")
