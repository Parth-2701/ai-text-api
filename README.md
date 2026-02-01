# AI Text API

A FastAPI-based REST API for AI-powered text processing and generation.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Author](#author)
- [Acknowledgements](#acknowledgements)

## 🔍 Overview

This API provides AI-powered text processing capabilities including text generation, analysis, and transformation. Built with FastAPI, it offers high performance and automatic API documentation.

## ✨ Features

- **Text Generation**: Generate AI-powered text based on prompts
- **Text Analysis**: Analyze and extract keywords from text
- **RESTful API**: Clean and intuitive API endpoints
- **Automatic Documentation**: Interactive API docs with Swagger UI
- **Fast Performance**: Built on FastAPI for high-speed processing
- **Type Safety**: Pydantic models for request/response validation
- **Modular Architecture**: Well-organized service layer

## 🛠 Technology Stack

- **Framework**: FastAPI
- **Language**: Python 3.8+
- **Validation**: Pydantic
- **Server**: Uvicorn

## 📁 Project Structure

```
ai-text-api/
├── main.py                 # Main application entry point
├── schemas.py              # Pydantic models for request/response validation
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore file
├── services/              # Business logic and service layer
│   └── ...                # Service modules
└── README.md              # Project documentation
```

## ✅ Prerequisites

Before running this application, ensure you have:

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Parth-2701/ai-text-api.git
cd ai-text-api
```

### 2. Create Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

````env
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

## 🚀 Running the Application

### Development Mode

Run the application with auto-reload enabled:

```bash
uvicorn main:app --reload
````

Or with custom host and port:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Production Mode

For production deployment:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

The API will be available at:

- **API Base URL**: `http://localhost:8000`
- **Interactive Docs (Swagger)**: `http://localhost:8000/docs`
- **Alternative Docs (ReDoc)**: `http://localhost:8000/redoc`

## 📚 API Documentation

Once the application is running, you can access:

1. **Swagger UI**: Navigate to `http://localhost:8000/docs` for interactive API documentation
2. **ReDoc**: Navigate to `http://localhost:8000/redoc` for alternative documentation
3. **OpenAPI Schema**: Available at `http://localhost:8000/openapi.json`

## 👨‍💻 Author

**Parth**

- GitHub: [@Parth-2701](https://github.com/Parth-2701)

## 🙏 Acknowledgments

- FastAPI for the amazing framework
- The open-source community for various tools and libraries
