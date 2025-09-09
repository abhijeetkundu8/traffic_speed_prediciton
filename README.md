Traffic Speed Prediction App 🚦
A Machine Learning web app built using Streamlit to predict the speed of traffic on different roads, based on historical data (lags, hour of day, and day of week). This project demonstrates data analysis, feature engineering, and model deployment in a simple and interactive way.

🔍 Project Overview
Goal: Predict the traffic speed (in km/h) using historical speed data.

Model: Random Forest Regressor with lag features and time-based features.

Frontend: Streamlit web app for user interaction.

Deployment: Ready for deployment on Streamlit Cloud or any hosting platform.

📊 Dataset
The model is trained using synthetic traffic speed datasets:

speeddata_Aug.csv

speeddata_Sep.csv

Each record includes:

road_id – ID of the road segment.

day_id – Day of data recording.

time_id – 10-minute intervals in a day.

speed – Average speed on that road segment.

⚙️ Features
EDA: Data visualization of speed distribution and trends.

Feature Engineering: Added lag1, lag2, lag3 (past 30 minutes' speed), hour, and day_of_week.

Model: RandomForestRegressor trained and stored as traffic_speed_model.pkl.

Web App: Interactive UI to input road ID, hour, day of week, and previous speeds.

🛠️ Tech Stack
Python: pandas, numpy, matplotlib, seaborn

Machine Learning: scikit-learn (RandomForestRegressor)

Web App: Streamlit

Model Persistence: joblib

Deployment: Streamlit Cloud

🚀 How to Run Locally
1. Clone the Repository
git clone https://github.com/your-username/traffic-speed-predictor.git
cd traffic-speed-predictor
2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate   # For Windows
3. Install Dependencies
pip install -r requirements.txt
4. Run the App
streamlit run app.py

📂 Project Structure

traffic-speed-predictor/
├── app.py                    # Streamlit app
├── traffic_speed_model.pkl   # Trained ML model
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── notebook.ipynb            # Data analysis & model training


🌐 Live Demo
https://abhijeetkundu8-traffic-speed-prediciton-app-jfh9xh.streamlit.app/







