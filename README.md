# Movie Recommendation System

**Level 1 Project - AI/ML Internship at Cognevance Technologies**

A complete collaborative filtering-based movie recommendation system built from scratch using Python.

## 📊 Project Overview

This project implements a user-based collaborative filtering algorithm to recommend movies based on user ratings and preferences. The system analyzes real user data and generates personalized movie suggestions.

## 📈 Key Statistics

- **Total Users:** 668
- **Total Movies:** 10,329
- **Total Ratings:** 105,339
- **Recommendations Generated:** 2,004

## 🛠️ Technologies Used

- Python 3.12
- Pandas & NumPy (Data manipulation)
- Scikit-learn (Machine Learning)
- Matplotlib & Seaborn (Data Visualization)

## 📁 Project Structure

movie-recommendation-system/

├── code/                          # Python scripts
│   ├── Task_2_Data_Cleaning.py
│   ├── Task_3_Data_Analysis.py
│   ├── Task_4_Recommendation_Algorithm.py
│   ├── Task_5_Generate_Recommendations.py
│   ├── Task_6_Visualizations.py
│   └── Task_7_Generate_Report.py
├── output/                        # Results
│   ├── recommendations.csv
│   ├── 01_movie_analysis.png
│   ├── 02_user_activity.png
│   └── 03_genre_analysis.png
└── report.md                      # Full documentation

## ✅ Tasks Completed

- ✅ Task 1: Data Collection
- ✅ Task 2: Data Cleaning & Preprocessing
- ✅ Task 3: Exploratory Data Analysis
- ✅ Task 4: Recommendation Algorithm (Collaborative Filtering)
- ✅ Task 5: Generate Movie Recommendations
- ✅ Task 6: Create Visualizations & Charts
- ✅ Task 7: Generate Comprehensive Report

## 🧠 How the Algorithm Works

1. **User-Movie Matrix** - Create a matrix of users vs movies with ratings
2. **Calculate Similarity** - Use cosine similarity to find similar users
3. **Find Neighbors** - For each user, identify top 10 most similar users
4. **Generate Recommendations** - Recommend movies that similar users rated highly
5. **Exclude Watched** - Don't recommend movies the user already rated

## 📊 Visualizations Generated

- **01_movie_analysis.png** - 4-panel dashboard with rating distribution, top movies, and average ratings
- **02_user_activity.png** - User engagement and activity patterns
- **03_genre_analysis.png** - Popular movie genres distribution

## 🎯 Key Findings

- Average movie rating: 3.5/5.0
- Users show high variability in engagement (1 to 1000+ ratings)
- Recommendation system successfully identifies similar users
- Generated 2,004 personalized movie suggestions for 668 users
- Top rated movies average 4.0+ stars

## 🚀 How to Use

1. Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

2. Run tasks in order:
```bash
python code/Task_2_Data_Cleaning.py
python code/Task_3_Data_Analysis.py
python code/Task_4_Recommendation_Algorithm.py
python code/Task_5_Generate_Recommendations.py
python code/Task_6_Visualizations.py
python code/Task_7_Generate_Report.py
```

3. Check `output/` folder for results

## 📊 Output Files Generated

- `recommendations.csv` - 2,004 movie recommendations
- `01_movie_analysis.png` - Analysis dashboard
- `02_user_activity.png` - User engagement chart
- `03_genre_analysis.png` - Genre distribution
- `report.md` - Complete project report

## 👨‍💻 Author

**Nishant** - AI/ML Internship Program  
Cognevance Technologies

## 📝 License

MIT License - Feel free to use this project for learning and reference!
---
*This project demonstrates core machine learning concepts including data preprocessing, exploratory analysis, similarity metrics, and collaborative filtering recommendation systems.*
