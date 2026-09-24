import streamlit as st
import requests

st.title("LegalEase: AI-Powered Legal Document Generator")
st.write("Generate customized legal agreements effortlessly.")

doc_type = st.selectbox(
    "Select Document Type",
    ["Rental Agreement", "Non-Disclosure Agreement (NDA)", "Employment Contract", "Service Level Agreement (SLA)"]
)

details = st.text_area("Enter essential details (e.g., Party Names, Duration, Amount, Location):")

if st.button("Generate Document"):
    if details.strip() == "":
        st.warning("Please enter necessary details!")
    else:
        with st.spinner("Generating legal document..."):
            try:
                # Backend FastAPI endpoint
                response = requests.post(
                    "http://localhost:8000/generate-doc",
                    json={"doc_type": doc_type, "details": details}
                )
                if response.status_code == 200:
                    result = response.json().get("document")
                    st.success("Document Generated Successfully!")
                    st.text_area("Generated Document", value=result, height=400)
                else:
                    st.error("Error from Backend API")
            except Exception as e:
                st.error(f"Failed to connect to backend: {e}")
