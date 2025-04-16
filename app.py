import streamlit as st
import numpy as np
import cv2
from utils.face_utils import detect_age_group, analyze_expression

st.set_page_config(page_title="Mental Health Analyzer", layout="centered")

st.title("🧠 Mental Health Prediction System")
st.markdown("Upload an image to analyze age group, emotional state, and mental health factors.")

uploaded_file = st.file_uploader("Upload a face image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Read and decode image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_array = cv2.imdecode(file_bytes, 1)

    # Show image
    st.image(img_array, channels="BGR", caption="Uploaded Image", use_container_width=True)

    with st.spinner("Analyzing image... please wait."):
        age, age_group = detect_age_group(img_array)
        # Manual override (for testing purposes)
    override = st.checkbox("Manually set age group?")
    if override:
        age_group = st.selectbox("Choose Age Group:", ["Child", "Young", "Grown-up"])
        emotion = analyze_expression(img_array)
        
    emotion = analyze_expression(img_array)
    st.success("✅ Analysis Complete")



    st.markdown(f"**👤 Age Group**: {age_group} (Estimated Age: {age})")
    st.markdown(f"**😐 Dominant Emotion**: {emotion.capitalize()}")

    # ===================
    # AGE-BASED LOGIC
    # ===================

    if age_group == "Child":
        st.subheader("🍼 Child (0–6) Analysis")

        if emotion in ["sad", "neutral", "tired"]:
            st.warning("🔔 The child may be hungry.")
        else:
            st.success("😊 The child seems to be in a good mood.")

    elif age_group == "Young":
        st.subheader("🧒 Young (7–17) Psychometric Quiz")

        q1 = st.radio("Do you often feel angry or irritated?", ["Yes", "No"])
        q2 = st.radio("Do you like breaking rules?", ["Yes", "No"])
        q3 = st.radio("Do you feel empathy for others?", ["Yes", "No"])
        q4 = st.radio("Do you get into fights often?", ["Yes", "No"])
        q5 = st.radio("Do you enjoy harming animals or property?", ["Yes", "No"])

        score = sum([q == "Yes" for q in [q1, q2, q4, q5]])

        if score >= 3:
            st.error("⚠️ Possible criminal tendencies detected.")
        else:
            st.success("✅ Low risk of criminal behavior.")

        st.markdown("🧠 Mental State:")
        if score == 0:
            st.success("Excellent")
        elif score <= 2:
            st.warning("Moderate")
        else:
            st.error("Poor")

    elif age_group == "Grown-up":
        st.subheader("👨 Adult (18+) Mental Health Quiz")

        q1 = st.radio("Do you often feel hopeless?", ["Yes", "No"])
        q2 = st.radio("Do you enjoy activities like before?", ["Yes", "No"])
        q3 = st.radio("Do you have trouble sleeping?", ["Yes", "No"])
        q4 = st.radio("Do you feel anxious or panicked?", ["Yes", "No"])
        q5 = st.radio("Do you have thoughts of harming yourself?", ["Yes", "No"])

        mh_score = sum([q == "Yes" for q in [q1, q3, q4, q5]])
        crime_flag = q5 == "Yes" or emotion == "angry"

        if crime_flag:
            st.error("🚨 Emotional distress detected. High-risk alert.")
        elif emotion == "angry":
            st.warning("⚠️ Elevated aggression detected.")
        else:
            st.success("✅ Emotionally stable.")

        st.markdown("🧠 Mental Health Rating:")
        if mh_score == 0:
            st.success("Excellent")
        elif mh_score <= 2:
            st.warning("Moderate")
        else:
            st.error("Poor")

