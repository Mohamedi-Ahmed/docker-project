# Docker Project: Data Management and Analysis Platform

## Objective
This project provides a containerized infrastructure for data management and analysis using MongoDB, Flask, Streamlit, and Jupyter.

## Project Structure
```plaintext
docker-project/
│
├── data/
│   └── mongo_data/
│
├── flask_app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── streamlit_app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── jupyter/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── notebooks/
│       ├── insert_data.py
│       └── insert_data.ipynb
│
├── docker-compose.yml
└── README.md
