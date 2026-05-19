import streamlit as st
import pickle

# load trained model
model = pickle.load(open("model.pkl", "rb"))

# load vectorizer
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# page config
st.set_page_config(
    page_title="IKEA Product Price Prediction",
    page_icon="🛋️",
    layout="centered"
)

# title
st.title("🛋️ IKEA Product Price Prediction")

st.write(
    "Enter any IKEA furniture product description to predict price."
)

# user input
product_name = st.text_input(
    "Enter Product Description",
    "Wooden bed with storage"
)

# prediction button
if st.button("Predict Price"):

    # transform text
    data = vectorizer.transform([product_name])

    # predict
    prediction = model.predict(data)

    # show output
    st.success(
        f"Predicted IKEA Price: €{round(prediction[0], 2)}"
    )