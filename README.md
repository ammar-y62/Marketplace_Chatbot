# Marketplace Chatbot and Dashboard

This project implements an integrated **Marketplace Chatbot** using **Rasa** and a **React-based Dashboard** to manage unanswered queries and inventory data.

## 📋 Project Overview

The project is divided into three main components:

1. **Rasa Chatbot**: A chatbot for answering questions about product availability, pickup location, and timing.
2. **Backend**: A **Flask API** for managing inventory, logging unanswered queries, and serving data to the dashboard.
3. **React Dashboard**: A user-friendly interface to view unanswered queries and manage scripts.

---

## 🛠️ Technologies Used

### Backend
- **Flask**: Python web framework for API development.
- **Flask-SQLAlchemy**: Database ORM for managing unanswered queries.
- **SQLite**: Lightweight database for storing queries.
- **Pandas**: For reading and managing Excel-based inventory data.
- **CORS**: For enabling frontend-backend communication.

### Chatbot
- **Rasa**: Conversational AI framework to create the chatbot.
- **Rasa SDK**: For building custom actions and integrating APIs.

### Frontend
- **React**: JavaScript library for building the dashboard UI.
- **Bootstrap**: CSS framework for responsive and modern UI components.

---

## 🚀 Features

### Chatbot
- Answer questions about:
  - Product availability.
  - Pickup address.
  - Pickup timing.
- Logs unanswered queries to the backend for manual responses.

### Backend API
- Stores unanswered queries into the database.
- Serves inventory data to the chatbot.
- Provides data endpoints for the frontend dashboard.

### React Dashboard
- Displays unanswered queries dynamically.
- Toggle between **Dark Mode** and **Light Mode**.
- Allows saving manual scripts for unresolved queries.

---

## 📁 Project Structure

```plaintext
Marketplace_Chatbot/
│
├── dashboard/            # React frontend code
│   ├── public/           # Static files
│   ├── src/              # React components
│   │   ├── api.js        # API calls to the backend
│   │   ├── components/   # React UI components
│   │   ├── App.js        # Main App file
│   │   └── index.js      # Entry point for React
│   └── package.json      # React project dependencies
│
├── rasa/                 # Rasa chatbot configuration
│   ├── actions.py        # Custom Rasa actions
│   ├── data/             # NLU, stories, and rules files
│   ├── domain.yml        # Rasa domain configuration
│   └── endpoints.yml     # Custom action server configuration
│
├── static/               # Old static files (no longer used)
│   └── ...
│
├── templates/            # Old HTML templates (deprecated)
│
├── app.py                # Flask backend server
├── instance/             # SQLite database for unanswered queries
│   └── unanswered_queries.db
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
