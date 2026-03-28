# 🚀 JobReady - AI Career Assessment Platform

JobReady is a powerful web application designed to help tech enthusiasts discover their ideal career path. By leveraging OpenAI's GPT-4o-mini, the platform evaluates your current skills and provides personalized recommendations, readiness scores, and learning paths.

## ✨ Features

- **AI-Powered Assessment**: Get a deep analysis of your technical and soft skills using OpenAI's GPT-4o-mini.
- **Personalized Career Matching**: Discover which tech role (Frontend, Backend, AI/Data Science, DSA) fits you best.
- **Professional PDF Reports**: Download a comprehensive career assessment report as a PDF.
- **Readiness Score**: A clear visual representation of how prepared you are for your target career.
- **Skill Gap Identification**: Know exactly what you need to learn next with automated gap analysis.
- **Mobile Responsive UI**: Fully optimized for a seamless experience on desktop, tablet, and mobile devices.
- **Progress Tracking**: Save your assessment progress and view your results anytime.
- **Secure Authentication**: User registration and login powered by Flask-Login.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **AI Engine**: OpenAI API (GPT-4o-mini)
- **PDF Generation**: fpdf2
- **Frontend**: HTML5, CSS3 (Flexbox/Grid), JavaScript
- **Deployment**: Render / GitHub

## 🚦 Getting Started

### Prerequisites

- Python 3.8+
- An OpenAI API Key ([Get it here](https://platform.openai.com/api-keys))

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/JobReady.git
   cd JobReady
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your_secret_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the application**:
   ```bash
   python run.py
   ```
   Visit `http://127.0.0.1:5000` in your browser.

## ☁️ Deployment on Render

1. **Push your code to GitHub**.
2. **Create a New Web Service** on Render.
3. **Connect your GitHub repository**.
4. **Environment Settings**:
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn wsgi:app`
5. **Add Environment Variables** in Render Dashboard:
   - `SECRET_KEY`: A random secure string.
   - `OPENAI_API_KEY`: Your OpenAI API Key.
   - `PYTHON_VERSION`: `3.10.0` (or your preferred version).

## 📂 Project Structure

```text
AYproject/
├── app/
│   ├── core/           # Configuration & Extensions
│   ├── models/         # Database Models
│   ├── routes/         # Blueprints & API Endpoints
│   ├── services/       # AI & Logic Services
│   ├── static/         # CSS, JS, & Assets
│   └── templates/      # HTML Templates
├── run.py              # Entry point
├── requirements.txt    # Dependencies
└── .env                # Secret environment variables
```

## 📄 License

This project is licensed under the MIT License.

---
Built with ❤️ by the JobReady Team.
