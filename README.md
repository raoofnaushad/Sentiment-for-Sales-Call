# AlertDriving Sales Sentiment Analyzer

![AlertDriving Logo](frontend/public/AlertDrivingImage.avif)

## Overview
The Sales Sentiment Analyzer is a cutting-edge tool developed for AlertDriving's sales team to enhance customer interaction analysis. This application processes customer responses in real-time, providing instant sentiment analysis to help sales representatives better understand and respond to customer feedback.


## 🏗 Architecture

### Tech Stack
**Frontend:**
- Next.js 14 (React Framework)
- TypeScript
- Tailwind CSS
- Environment-based configuration

**Backend:**
- Python 3.9+
- FastAPI
- LLM Integration
- Pydantic

## 🚀 Getting Started

### Prerequisites
- Node.js (v18 or higher)
- Python 3.9+
- npm or yarn
- pip (Python package manager)

### Installation

1. **Clone the Repository**
```bash
git clone [repository-url]
cd alertdriving-sentiment-analyzer
```

2. **Backend Setup**
```bash
# Create and activate virtual environment
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --reload --port 8000
```

3. **Frontend Setup**
```bash
# In a new terminal
cd frontend
npm install

# Create .env.local file
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

# Start development server
npm run dev
```

## 📁 Project Structure