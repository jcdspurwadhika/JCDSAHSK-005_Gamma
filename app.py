import streamlit as st
import pandas as pd
import joblib

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Olist Customer Return Prioritization",
    layout="wide"
)

st.title("Olist Customer Return Prioritization")
st.caption(
    "Customer scoring demo using held-out test customers."
)

# =========================
# LOAD MODEL & HOLDOUT DATA
# =========================
model = joblib.load("olist_return_model.joblib")
holdout_demo = pd.read_csv("olist_holdout_demo.csv")

# =========================
# MODEL FEATURES
# =========================
model_features = [
    "recency_days",
    "frequency",
    "monetary",
    "total_items",
    "unique_products",
    "orders_with_known_value",
    "known_merchandise_value",
    "orders_missing_value"
]

# =========================
# CUSTOMER SEARCH
# =========================
st.subheader("Customer Holdout Test")

customer_id = st.text_input(
    "Customer ID",
    placeholder="Paste customer_unique_id from olist_holdout_demo.xlsx"
)

if st.button("Search & Predict"):

    if customer_id.strip() == "":
        st.warning("Please input a Customer ID.")

    else:
        customer_match = holdout_demo.loc[
            holdout_demo["customer_unique_id"].astype(str)
            == customer_id.strip()
        ]

        if customer_match.empty:
            st.error(
                "Customer ID was not found in the holdout dataset."
            )

        else:
            customer_row = customer_match.iloc[0]

            customer_features = pd.DataFrame([
                customer_row[model_features]
            ])

            # =========================
            # PREDICTION
            # =========================
            classes = list(
                model.named_steps["model"].classes_
            )

            returned_index = classes.index(0)

            return_score = (
                model.predict_proba(
                    customer_features
                )[0][returned_index]
            )

            predicted_class = (
                model.predict(
                    customer_features
                )[0]
            )

            actual_class = int(
                customer_row["churn_180d"]
            )

            predicted_label = (
                "Returned / Not Churn"
                if predicted_class == 0
                else "Churn / No New Order"
            )

            actual_label = (
                "Returned / Not Churn"
                if actual_class == 0
                else "Churn / No New Order"
            )

            # =========================
            # CUSTOMER INFO
            # =========================
            st.subheader("Historical Customer Behavior")

            st.dataframe(
                customer_features,
                use_container_width=True
            )

            # =========================
            # RESULT
            # =========================
            st.subheader("Prediction Result")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Return Score",
                    f"{return_score:.2%}"
                )

            with col2:
                st.metric(
                    "Predicted Outcome",
                    predicted_label
                )

            with col3:
                st.metric(
                    "Actual Holdout Outcome",
                    actual_label
                )

            # =========================
            # MATCH CHECK
            # =========================
            if predicted_class == actual_class:
                st.success(
                    "Prediction matches the actual holdout outcome."
                )
            else:
                st.error(
                    "Prediction does not match the actual holdout outcome."
                )

            st.info(
                "The actual outcome comes from the held-out test snapshot. "
                "The target label is not used as a model input."
            )