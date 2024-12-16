# Marketplace Chatbot and Dashboard

This project integrates a chatbot powered by Rasa for handling marketplace inquiries and a React-based dashboard for managing unanswered queries.

---

## 📜 Table of Contents

- [Introduction](#-introduction)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Installation and Setup](#-installation-and-setup)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Contributions](#-contributions)
- [License](#-license)
- [Contact](#-contact)

---

## 📖 Introduction

The Marketplace Chatbot and Dashboard project provides an automated solution for handling client inquiries about marketplace listings. It includes:
- A chatbot for answering common questions about availability, pickup addresses, and timings.
- A dashboard for reviewing and responding to unanswered queries manually.

---

## ✨ Features

- **Chatbot**: Handles inquiries about product availability, pickup locations, and timings.
- **Dashboard**: Displays unanswered queries for manual review and response.
- **Database Integration**: Uses SQLite for storing unanswered queries.
- **Responsive Design**: Built using React and Bootstrap.

---

## 🔧 Technologies Used

- **Backend**: Flask, Flask-SQLAlchemy
- **Chatbot**: Rasa
- **Frontend**: React, Bootstrap
- **Database**: SQLite
- **Deployment**: Local or cloud-based setup

---

## 🔧 Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/username/marketplace-chatbot.git
cd marketplace-chatbot
```

### 2. Set Up the Backend
- Navigate to the root directory and set up a virtual environment:
  ```bash
  python -m venv marketplace_env
  source marketplace_env/bin/activate  # Linux/Mac
  marketplace_env\Scripts\activate  # Windows
  ```
- Install the required Python packages:
  ```bash
  pip install -r requirements.txt
  ```
- Run the Flask app:
  ```bash
  python app.py
  ```

### 3. Set Up the Chatbot
- Navigate to the Rasa directory:
  ```bash
  cd rasa
  ```
- Train the chatbot:
  ```bash
  rasa train
  ```
- Run the Rasa action server:
  ```bash
  rasa run actions
  ```
- Start the chatbot:
  ```bash
  rasa shell
  ```

### 4. Set Up the Frontend
- Navigate to the `dashboard` directory:
  ```bash
  cd dashboard
  ```
- Install dependencies:
  ```bash
  npm install
  ```
- Start the React app:
  ```bash
  npm start
  ```

---

## 🗂 Project Structure

```plaintext
marketplace-chatbot/
├── app.py                   # Flask backend for API and database
├── dashboard/               # React-based frontend
│   ├── public/              # Static assets
│   ├── src/                 # React components and pages
│   ├── package.json         # Frontend dependencies
│   └── ...
├── rasa/                    # Chatbot configuration and files
│   ├── domain.yml           # Rasa domain file
│   ├── actions.py           # Custom actions for the chatbot
│   ├── config.yml           # Chatbot pipeline configuration
│   └── ...
├── requirements.txt         # Backend dependencies
└── README.md                # Project documentation
```

---

## 🌐 API Endpoints

### 1. **Log Unanswered Queries**
**Endpoint**:
`POST /api/log_unanswered`

**Payload**:
```json
{
  "message": "Unanswered query text"
}
```

**Response**:
```json
{
  "status": "success",
  "message": "Logged successfully"
}
```

---

### 2. **Get Unanswered Queries**
**Endpoint**:
`GET /api/get_unanswered`

**Response**:
```json
[
  {
    "id": 1,
    "message": "Unanswered query text",
    "timestamp": "2024-06-16T12:00:00"
  }
]
```

---

### 3. **Respond to Query**
**Endpoint**:
`POST /api/respond`

**Payload**:
```json
{
  "query_id": 1,
  "response": "Here is the response text."
}
```

**Response**:
```json
{
  "status": "success",
  "message": "Response sent successfully"
}
```

---

## 🔄 Contributions

Contributions are welcome! Please fork the repository and submit a pull request.

---

## © License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## 📞 Contact

For questions or feedback, contact:
- **Email**: amzeftawy@gmail.com
- **GitHub**: [ammar-y62](https://github.com/ammar-y62)
