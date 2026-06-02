# AI Intern Assessment Submission

## Candidate Information

**Name:** Archee Sinha

**Role Applied For:** AI Intern

---

# Project Overview

This repository contains solutions for the AI Intern Assessment.

## Task 1: Intelligent Resume Ranking System

An NLP-based application that ranks candidates based on their relevance to a given Job Description.

### Features

* Text Preprocessing
* TF-IDF Vectorization
* Cosine Similarity
* Candidate Ranking
* Match Percentage Calculation
* CSV Export
* Streamlit Dashboard

### Technologies Used

* Python
* Scikit-Learn
* NLTK
* Pandas
* Streamlit

---

## Task 2: AI-Powered Student Query Assistant

An AI chatbot that answers student queries related to Programming, AI/ML, Career Guidance, and Interview Preparation.

### Features

* Gemini API Integration
* Chat History
* Conversation Logging
* Input Validation
* Exception Handling
* Streamlit Chat Interface

### Technologies Used

* Python
* Streamlit
* Google Gemini API
* Pandas
* Python-Dotenv

---

# Repository Structure

```text
AI-Intern-Assessment/

├── Resume Ranking System/
│   ├── app.py
│   ├── streamlit_app.py
│   ├── requirements.txt
│   ├── data/
│   ├── output/
│   └── utils/
│
├── Student Query Assistant/
│   ├── streamlit_app.py
│   ├── requirements.txt
│   ├── logs/
│   └── utils/
│
└── README.md
```

---

# Setup Instructions

## Prerequisites

* Python 3.10 or above
* Git
* Streamlit

---

## Clone Repository

```bash
git clone https://github.com/ArcheeSinha/AI-Intern-Assessment.git

cd AI-Intern-Assessment
```

---

# Task 1: Resume Ranking System

## Navigate to Project

```bash
cd "Resume Ranking System"
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run streamlit_app.py
```

---

# Task 2: Student Query Assistant

## Navigate to Project

```bash
cd "Student Query Assistant"
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

## Run Application

```bash
streamlit run streamlit_app.py
```

---

# Requirements Files

Both projects contain their own `requirements.txt` files with all necessary dependencies.

---

# Source Code

The complete source code for both tasks is included in this repository.

---

# Author

Archee Sinha

B.Tech CSE (Artificial Intelligence)

ABES Institute of Technology
