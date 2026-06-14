import pandas as pd
from datetime import datetime
 
print("="*60)
print("TASK 7: GENERATE PROJECT REPORT")
print("="*60)
 
# Load data
print("\n1. Loading data...")
ratings = pd.read_csv('data/ratings_cleaned.csv')
movies = pd.read_csv('data/movies_cleaned.csv')
recommendations = pd.read_csv('output/recommendations.csv')
movie_ratings = ratings.merge(movies, on='movieId')
 
# Calculate statistics
print("2. Calculating statistics...")
 
total_users = ratings['userId'].nunique()
total_movies = movies['movieId'].nunique()
total_ratings = len(ratings)
 
avg_rating = ratings['rating'].mean()
mode_rating = ratings['rating'].mode()[0]
 
user_counts = ratings.groupby('userId')['rating'].count()
avg_per_user = user_counts.mean()
max_user_ratings = user_counts.max()
 
top_movies = movie_ratings.groupby('title')['rating'].count().sort_values(ascending=False).head(5)
top_rated = movie_ratings.groupby('title')['rating'].mean().sort_values(ascending=False).head(5)
 
# Create report
print("3. Creating report content...")
 
report = f"""# Movie Recommendation System - Project Report
 
**Date:** {datetime.now().strftime('%B %d, %Y')}  
**Project:** Level 1 - AI/ML Internship  
**Author:** Nishant  
 
---
 
## Executive Summary
 
This project implements a **collaborative filtering-based movie recommendation system** that analyzes user ratings to suggest personalized movie recommendations. The system successfully processes a dataset of user ratings and generates meaningful recommendations based on user similarity patterns.
 
---
 
## Dataset Overview
 
| Metric | Value |
|--------|-------|
| **Total Users** | {total_users} |
| **Total Movies** | {total_movies} |
| **Total Ratings** | {total_ratings:,} |
 
---
 
## Key Statistics
 
### Rating Statistics
- **Average Rating:** {avg_rating:.2f}/5.0
- **Most Common Rating:** {mode_rating:.0f} stars
- **Ratings per User (avg):** {avg_per_user:.0f}
- **Most Active User:** {max_user_ratings} ratings
 
### Top 5 Most Rated Movies
 
| Rank | Movie Title | Ratings |
|------|-------------|---------|
"""
 
for idx, (title, count) in enumerate(top_movies.items(), 1):
    report += f"| {idx} | {title} | {count} |\n"
 
report += f"""
 
### Top 5 Highest Rated Movies
 
| Rank | Movie Title | Rating |
|------|-------------|--------|
"""
 
for idx, (title, rating) in enumerate(top_rated.items(), 1):
    report += f"| {idx} | {title} | {rating:.2f}⭐ |\n"
 
report += """
 
---
 
## Methodology
 
### Algorithm: User-Based Collaborative Filtering
 
**How It Works:**
1. Create a user-movie rating matrix
2. Calculate similarity between users using cosine similarity
3. For each user, find similar users
4. Recommend movies that similar users rated highly
5. Exclude movies the target user already watched
 
**Key Principle:** 
If two users have similar rating patterns, they likely enjoy similar movies.
 
---
 
## Tasks Completed
 
✅ **Task 1:** Data Collection  
✅ **Task 2:** Data Cleaning & Preprocessing  
✅ **Task 3:** Exploratory Data Analysis  
✅ **Task 4:** Recommendation Algorithm Implementation  
✅ **Task 5:** Generate Recommendations  
✅ **Task 6:** Create Visualizations  
✅ **Task 7:** Generate Project Report  
 
---
 
## Results
 
### Recommendations Generated
 
"""
 
if len(recommendations) > 0:
    unique_users = recommendations['userId'].nunique()
    report += f"""- **Total Recommendations:** {len(recommendations):,}
- **Users Covered:** {unique_users}
- **Avg Recommendations per User:** {len(recommendations)/unique_users:.1f}
 
"""
 
report += """---
 
## Project Artifacts
 
### Generated Files
 
**Data Files:**
- `data/movies_cleaned.csv` - Cleaned movie data
- `data/ratings_cleaned.csv` - Cleaned rating data
- `data/user_similarity.csv` - User similarity matrix
 
**Output Files:**
- `output/recommendations.csv` - Generated recommendations
- `output/01_movie_analysis.png` - Analysis dashboard
- `output/02_user_activity.png` - User activity chart
- `output/03_genre_analysis.png` - Genre distribution
 
**Code Files:**
- `code/Task_2_Data_Cleaning.py`
- `code/Task_3_Data_Analysis.py`
- `code/Task_4_Recommendation_Algorithm.py`
- `code/Task_5_Generate_Recommendations.py`
- `code/Task_6_Visualizations.py`
- `code/Task_7_Generate_Report.py`
 
---
 
## Technologies Used
 
- **Python 3.12**
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning (cosine similarity)
- **Matplotlib & Seaborn** - Data visualization
 
---
 
## Conclusions
 
This project successfully demonstrates the implementation of a collaborative filtering recommendation system. The system:
 
✅ Processes real movie ratings data  
✅ Identifies user patterns and similarities  
✅ Generates personalized recommendations  
✅ Creates professional visualizations  
✅ Produces comprehensive documentation  
 
The skills learned through this project are directly applicable to real-world recommendation systems used by major tech companies like Netflix, Amazon, and YouTube.
 
---
 
## Future Improvements
 
1. **Hybrid Recommendations** - Combine collaborative and content-based filtering
2. **Matrix Factorization** - More efficient similarity calculations
3. **Deep Learning** - Neural networks for complex patterns
4. **Real-time Updates** - Dynamic recommendations as users rate new movies
5. **Web Deployment** - Build a user-facing web application
 
---
 
**End of Report**
 
Generated: {datetime.now().strftime('%A, %B %d, %Y at %I:%M %p')}
"""
 
# Save report
print("4. Saving report...")
with open('report.md', 'w', encoding='utf-8') as f:
    f.write(report)
 
print("="*60)
print("✓ REPORT GENERATED!")
print("="*60)
print("\n✓ Saved: report.md")
print("\n" + "="*60)
print("✓ ALL TASKS COMPLETE!")
print("="*60)
print("\nProject Summary:")
print(f"  • Total Users: {total_users}")
print(f"  • Total Movies: {total_movies}")
print(f"  • Total Ratings: {total_ratings:,}")
print(f"  • Recommendations Generated: {len(recommendations):,}")
print("\nReady for GitHub! 🚀") 