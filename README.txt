===================================================
MENTAL HEALTH PREDICTION SYSTEM
===================================================

This system uses facial analysis and psychometric assessments to predict mental states, emotional well-being, and potential behavioral tendencies based on age groups.

---------------------------
FEATURES
---------------------------
- Upload image for analysis
- Age group detection (Child, Young, Grown-up)
- Emotion detection using DeepFace
- Mental health scoring with psychometric questions
- Hunger and mood alerts for children
- Crime probability check for young individuals
- Depression risk analysis for adults

---------------------------
TECHNOLOGIES USED
---------------------------
- Python 3.8+
- Streamlit (Web UI)
- OpenCV (Image Processing)
- NumPy (Data Handling)
- PyTorch (Custom CNN Model for Age Classification)
- Torchvision (Image Transforms)
- DeepFace (Emotion Detection Model)

---------------------------

---------------------------
INSTALLATION INSTRUCTIONS
---------------------------
1. Clone the repository:
   git clone <https://github.com/souviksengupta801/MENTAL-HEALTH-PREDICTION-SYSTEM
   cd mental-health-system

2. Create a virtual environment (optional but recommended):
   python -m venv venv
   venv\Scripts\activate  (Windows)
   source venv/bin/activate  (Linux/Mac)

3. Install dependencies:
   pip install -r requirements.txt

---------------------------
MINIMUM REQUIREMENTS
---------------------------
- Python 3.8+
- 2GB RAM minimum
- Internet connection (for DeepFace on first run)
- Webcam or face images (for testing)

---------------------------
HOW TO RUN
---------------------------
Run the following command from the project root:

   streamlit run app.py

Then open the local URL shown in your terminal (usually http://localhost:8501).

---------------------------
CREDITS
---------------------------
Developed by: Souvik Sengupta
Supervisor: Dr. Abhishek Roy
Project: Mental Health Prediction Using Natural Language Sentiment and Facial Expression Recognition