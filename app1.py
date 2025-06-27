{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "953b6dc3-205a-4ed3-9635-1ebde1e37376",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-27 12:47:37.327 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\p.hrithik kunal\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-06-27 12:47:37.344 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "# app.py\n",
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Load model\n",
    "model = pickle.load(open('model.pkl', 'rb'))\n",
    "\n",
    "st.title(\"Titanic Survival Predictor 🚢\")\n",
    "\n",
    "# User inputs\n",
    "Pclass = st.selectbox(\"Passenger Class\", [1, 2, 3])\n",
    "Sex = st.radio(\"Sex\", ['Male', 'Female'])\n",
    "Age = st.slider(\"Age\", 1, 80, 25)\n",
    "SibSp = st.number_input(\"Siblings/Spouses Aboard\", 0, 10, 0)\n",
    "Parch = st.number_input(\"Parents/Children Aboard\", 0, 10, 0)\n",
    "Fare = st.number_input(\"Fare Paid\", 0.0, 500.0, 50.0)\n",
    "Embarked = st.selectbox(\"Port of Embarkation\", ['S', 'C', 'Q'])\n",
    "\n",
    "# Map inputs\n",
    "Sex = 0 if Sex == 'Male' else 1\n",
    "Embarked = {'S': 0, 'C': 1, 'Q': 2}[Embarked]\n",
    "\n",
    "# Predict\n",
    "if st.button(\"Predict\"):\n",
    "    features = np.array([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])\n",
    "    prediction = model.predict(features)\n",
    "    st.success(\"✅ Survived!\" if prediction[0] == 1 else \"❌ Did not survive.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e5099c81-28ad-4445-a1f9-6f37e0fe0bf1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
