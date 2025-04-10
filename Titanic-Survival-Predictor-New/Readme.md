# 🛳️ Titanic Survival Predictor - A Dockerized Streamlit App

# Live demo: https://my-docker-projects-5uhnrhbwswnxrksw6nnt9m.streamlit.app/

This project is a machine learning-based Titanic survival prediction app built with Streamlit and containerized using Docker. The model predicts whether a passenger survived based on features like age, gender, ticket class, etc.

# 🚀 How to Run the Project

1️⃣ Clone the Repository

If you haven't cloned the repository, run:

git clone https://github.com/alveerraa/My-Docker-Projects.git

cd My-Docker-Projects/Titanic-Survival-Predictor

2️⃣ Install Dependencies (Optional)

If running locally (without Docker), install required Python packages:

pip install -r requirements.txt

3️⃣ Train the Model

Run the train_model.py script to train the model and generate titanic_model.pkl:

python3 train_model.py

This will create a machine learning model and save it as titanic_model.pkl.

4️⃣ Run the App Locally (Without Docker)

If you want to test without Docker, run:

streamlit run app.py

Then, open http://localhost:8501 in your browser.

🐳 Run the App Using Docker

1️⃣ Build the Docker Image

docker build -t titanic-predictor .

2️⃣ Run the Docker Container

docker run -p 8501:8501 titanic-predictor

Once the container is running, open http://localhost:8501 in your browser.

📝 Project Structure

Titanic-Survival-Predictor/

│── Dockerfile              # Docker configuration
│── app.py                  # Streamlit web app
│── train_model.py           # ML model training script
│── requirements.txt         # Dependencies
│── titanic_model.pkl        # Trained model (created after running train_model.py)
│── README.md                # Project documentation

🔥 Key Features

✔️ Trained ML model using scikit-learn
✔️ Web app built with Streamlit
✔️ Containerized using Docker
✔️ Predicts survival probability of passengers

📌 Next Steps

Deploy the containerized app on AWS EC2 or Heroku

Improve the model accuracy by tuning hyperparameters

Add more features like family members, fare, embarkation port

🎉 Done!
