# SmartCrop Recommendation System

A Machine Learning and Web-based project that helps farmers and users determine the most suitable crop to grow based on soil, weather, and environmental conditions. The system uses a trained ML model in the backend with a modern web frontend to provide accurate crop recommendations.

 Features :

Crop recommendation using Machine Learning

User-friendly web interface (React frontend)

Flask backend API

Responsive design

Easy to set up and run locally

Future ready for integration with weather APIs and IoT devices

...

Tech Stack

Frontend: React.js

Backend: Flask (Python)

Machine Learning: scikit-learn, pandas, numpy

Database (optional): SQLite / JSON-based storage

Others: Docker (for containerization), GitHub Actions (for CI/CD)



---


📂 Project Structure

SmartCrop-Recommendation-Full-Project/
│
├── backend/           # Flask backend with ML model
│   ├── app.py
│   ├── train_model.py
│   ├── requirements.txt
│   └── model.pkl
│
├── frontend/          # React frontend
│   ├── public/
│   ├── src/
│   │   └── App.jsx
│   └── package.json
│
├── README.md          # Project documentation
└── Dockerfile         # For deployment (optional)


---


⚙ Installation & Setup

🔹 Clone the repository

git clone https://github.com/thebadasschad/SmartCrop-Recommendation-Full-Project.git
cd SmartCrop-Recommendation-Full-Project

🔹 Backend Setup

cd backend
pip install -r requirements.txt
python app.py

Backend will run at: http://127.0.0.1:5000/

🔹 Frontend Setup

cd frontend
npm install
npm start

Frontend will run at: http://localhost:3000/


---

🖥 Usage

1. Open the frontend in your browser at http://localhost:3000/


2. Enter soil, temperature, humidity, rainfall, and other details.


3. Click "Recommend Crop" to see the most suitable crop.




---

---

🔮 Future Improvements

Integration with live weather APIs

Mobile app version

IoT device integration for automatic soil data collection

More datasets for better accuracy



---

🤝 Contributing

1. Fork this repo


2. Create a new branch (git checkout -b feature-branch)


3. Commit your changes (git commit -m "Added new feature")


4. Push to branch (git push origin feature-branch)


   5. Create a Pull Request




---

📜 License

This project is licensed under the MIT License – free to use and modify.


---

👨‍💻 Author

Nishant Kumar

GitHub: thebadasschad



---







