🚀 Project Overview

This system verifies user identity by analyzing documents and detecting authenticity. It helps organizations:

Automate KYC verification
Reduce fraud and manual effort
Improve onboarding speed
Enhance compliance processes


📂 Project Structure
AI-KYC-Verification-System/
│── app/                 # Streamlit web application
│── dataset/             # Input datasets (ID images, etc.)
│── src/                 # Core logic & ML pipeline
│── requirements.txt     # Project dependencies


🛠️ Tech Stack
Python
OpenCV → Image processing
NumPy, Pandas → Data handling
Scikit-learn / Deep Learning → Model building
Streamlit → Web interface


⚙️ Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/Vinit3019/ai-kyc-verification.git
cd ai-kyc-verification

2️⃣ Install Dependencies
pip install -r requirements.txt
🧠 How It Works
Upload identity document (Aadhaar, PAN, etc.)
Preprocess image using OpenCV
Extract relevant features
Verify authenticity using ML model
Display verification result

▶️ Run the Application
streamlit run app/app.py

Open in browser:

http://localhost:8501


📊 Features

✔️ Document image processing
✔️ AI-based identity verification
✔️ Fraud detection capability
✔️ Interactive web interface
✔️ Fast and automated KYC flow

📈 Future Improvements
Add OCR (Tesseract) for text extraction
Face matching (selfie vs ID)
Integrate GenAI for explanation & validation
Deploy on cloud (AWS/GCP/Azure)
Add API integration for real-world usage
🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Vinit S B
GitHub: https://github.com/Vinit3019
