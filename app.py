import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# load data
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
products = pickle.load(open("products.pkl", "rb"))

# product vectors
X = vectorizer.transform(products["text"])

# page config
st.set_page_config(
    page_title="IKEA Product Price Prediction",
    page_icon="🛋️"
)

# title
st.title("🛋️ IKEA Product Price Prediction")

st.write(
    "Enter a furniture product description to predict IKEA price."
)

# input
product_input = st.text_input(
    "Enter Product Description",
    "wooden bed"
)

# prediction
if st.button("Predict Price"):

    # transform input
    input_vec = vectorizer.transform([product_input])

    # similarity
    similarity = cosine_similarity(input_vec, X)

    # best match
    index = similarity.argmax()

    # output
    predicted_price = products.iloc[index]["price"]

    matched_product = products.iloc[index]["product_name"]

    st.success(
        f"Predicted IKEA Price: €{round(predicted_price, 2)}"
    )

    st.write("Closest IKEA Product Match:")
    st.write(matched_product)