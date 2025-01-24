# Which is Bigger?

## Overview

The **"Which is Bigger?"** project is a Python-based web application powered by **Dash** and the **Gemini Generative AI** model. This app compares two numbers and determines which one is larger using advanced AI capabilities. The project is containerized with Docker for easy deployment and scalability.

---

## Features

- Simple and intuitive user interface built with **Dash**.
- Uses **Google Gemini Generative AI** to make comparisons.
- Securely manages sensitive API keys using environment variables.
- Fully containerized with Docker for seamless deployment.

---

## Project Structure

```
which_is_bigger/
│
├── app.py                # Main Dash application
├── gemini_module.py      # Gemini AI logic (unchanged as provided)
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (optional, ignored by Git)
├── Dockerfile            # Docker instructions
├── .dockerignore         # Files to exclude from Docker image
└── venv/                 # Virtual environment
```

---

## Prerequisites

- Python 3.9 or higher
- Docker (if running in a container)
- An active **Gemini API key**

---

## Installation

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/which-is-bigger.git
   cd which-is-bigger
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set the environment variable for the API key:
   - On Linux/macOS:
     ```bash
     export GEMINI_API_KEY="your_api_key_here"
     ```
   - On Windows:
     ```powershell
     set GEMINI_API_KEY="your_api_key_here"
     ```
5. Run the app:
   ```bash
   python app.py
   ```
6. Open your browser and navigate to:
   ```
   http://127.0.0.1:8082
   ```

---

### Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t which-is-bigger .
   ```
2. Run the Docker container:
   - With environment variable:
     ```bash
     docker run -d -p 8082:8082 -e GEMINI_API_KEY="your_api_key_here" which-is-bigger
     ```
   - With `.env` file:
     ```bash
     docker run -d -p 8082:8082 --env-file .env which-is-bigger
     ```
3. Open your browser and navigate to:
   ```
   http://127.0.0.1:8082
   ```

## Environment Variables

The app requires the following environment variable:

- `GEMINI_API_KEY`: Your Gemini API key. This is mandatory and must not be hardcoded.

For local development, create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

