# Hybrid Media Recommender

A hybrid recommender system for movies and TV shows built with **PyTorch**, **Scikit-learn**, **FastAPI**, and **Airflow**.

## 📌 Project Overview
This project explores real-world recommender system design:
- **Collaborative filtering** (matrix factorization on user–item ratings).
- **Content-based filtering** (movie metadata, genres, tags).
- **Hybrid approach** combining both methods.
- **Serving layer** via FastAPI (real-time recommendations).
- **Batch scoring pipeline** via Airflow + Docker.

Dataset: [MovieLens 25M](https://grouplens.org/datasets/movielens/25m/).
