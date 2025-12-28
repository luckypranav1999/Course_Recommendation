## 🔍 Project Overview

This project builds an **end-to-end course recommendation system** using **implicit user feedback** such as *viewing, enrolling, and completing courses*.

The system answers the question:

> **“Fans who took course X also took course Y”**

It follows a **real-world ML workflow**:

* Data preparation
* Exploratory Data Analysis (EDA)
* Baseline model
* Evaluation
* Iterative improvement
* Advanced model (Matrix Factorization)
* Production-ready design thinking

---

## 🎯 Problem Statement

Users do not provide explicit ratings for courses.
Instead, we observe **implicit behavior**, such as:

* Viewing a course
* Enrolling in a course
* Completing a course

The goal is to **learn user preferences from behavior** and recommend relevant next courses.

---

### `users.csv`

Contains user profile information used for personalization.

| Column        | Description                |
| ------------- | -------------------------- |
| user_id       | Unique fan/user ID         |
| role          | Coach, Player, Medic, etc. |
| skill_level   | Beginner, Level_1, UEFA_A  |
| profile_score | Profile completeness score |

---

### `items.csv`

Contains course and program details.

| Column     | Description                |
| ---------- | -------------------------- |
| item_id    | Course / Program ID        |
| item_type  | course / program           |
| category   | Coaching, Fitness, Medical |
| difficulty | Skill level                |

---

### `interactions.csv`

Contains implicit feedback data.

| Column      | Description                   |
| ----------- | ----------------------------- |
| user_id     | User identifier               |
| item_id     | Course identifier             |
| interaction | viewed / enrolled / completed |
| weight      | Interaction strength          |
| timestamp   | Event time                    |

#### Interaction Weights

| Interaction | Weight | Reason            |
| ----------- | ------ | ----------------- |
| viewed      | 1      | Weak signal       |
| enrolled    | 3      | Medium intent     |
| completed   | 5      | Strong preference |

---

## 🔍 Exploratory Data Analysis (EDA)

Before modeling, we analyze:

* User role distribution
* Course category distribution
* Interaction type distribution
* Sparsity of the user–item matrix
* Most completed (popular) courses

**Why EDA?**

* Validate data quality
* Confirm sparsity (collaborative filtering suitability)
* Identify noisy signals (e.g. views)

---

## 🧠 Model 1: Item–Item Collaborative Filtering (Baseline)

### Idea

If many users take **Course A** and **Course B** together, recommend **B** to users who took **A**.

### Steps

1. Build **User × Item matrix**
2. Compute **Item × Item co-occurrence matrix**
3. Recommend top items based on similarity scores

### Why Item–Item?

* Simple and interpretable
* Strong baseline
* Scales well
* Easy to explain in interviews

---

## 🧪 Training & Evaluation Strategy

### Train–Test Split

* **Time-based split**

  * Train = past interactions
  * Test = future interactions

> Prevents data leakage and mimics real-world usage.

---

### Evaluation Metrics

We do **not** use accuracy ❌

Correct metrics for recommender systems:

* **Precision@K** → Quality of recommendations
* **Recall@K** → Coverage of user interest

---

### Baseline Results

```
Precision@5 ≈ 0.027
Recall@5    ≈ 0.077
```

This is expected due to sparse implicit data.

---

## 🚀 Model Improvements

### Changes Made

* Removed weak signals (`viewed`)
* Used only strong interactions (`enrolled`, `completed`)
* Added popularity smoothing

### Improved Results

```
Precision@5 ≈ 0.044
Recall@5    ≈ 0.134
```

📈 ~70% improvement in Recall

---

## 🧠 Model 2: Matrix Factorization (Latent Factors)

### Why Matrix Factorization?

Item–Item models underfit sparse data.

Matrix Factorization learns **hidden (latent) preferences**, such as:

* User preference for tactical or fitness content
* Course focus on certain skill dimensions

### Implementation

* Used `TruncatedSVD` to learn latent embeddings
* Generated user and item vectors
* Scored recommendations using vector dot products

### Benefits

* Better personalization
* Handles sparsity
* Industry-standard approach (ALS-style)


## 🧑‍💻 Author

**Pranav Teckchandani**
Machine Learning & AI Enthusiast
