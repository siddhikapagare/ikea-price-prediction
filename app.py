import streamlit as st

st.title("IKEA Product Price Prediction")

product_name = st.text_input(
    "Enter Product Name",
    "Wooden Bed"
)

if st.button("Predict Price"):

    predicted_price = len(product_name) * 15

    st.success(
        f"Predicted Price: €{round(predicted_price, 2)}"
    )