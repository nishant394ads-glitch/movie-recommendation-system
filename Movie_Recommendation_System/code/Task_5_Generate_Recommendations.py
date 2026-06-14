import pandas as pd
 
print("="*60)
print("TASK 5: GENERATE RECOMMENDATIONS")
print("="*60)
 
# Load data
print("\n1. Loading data...")
ratings = pd.read_csv('data/ratings_cleaned.csv')
movies = pd.read_csv('data/movies_cleaned.csv')
user_similarity_df = pd.read_csv('data/user_similarity.csv', index_col=0)
 
# Convert to int
user_similarity_df.columns = user_similarity_df.columns.astype(int)
user_similarity_df.index = user_similarity_df.index.astype(int)
 
# Create matrix
print("2. Creating user-movie matrix...")
user_movie_matrix = ratings.pivot_table(
    index='userId',
    columns='movieId',
    values='rating'
)
user_movie_matrix = user_movie_matrix.fillna(0)
 
# Define recommendation function
def recommend_movies(user_id, n_recommendations=5):
    """Recommend movies for a user"""
    
    if user_id not in user_movie_matrix.index:
        return pd.DataFrame()
    
    # Find similar users
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:11]
    
    # Get movies user hasn't watched
    watched = user_movie_matrix.loc[user_id]
    unwatched = watched[watched == 0].index.tolist()
    
    # Calculate recommendations
    recommendations = {}
    for movie_id in unwatched:
        ratings_from_similar = user_movie_matrix.loc[similar_users.index, movie_id]
        weighted_score = (ratings_from_similar * similar_users.values).sum()
        normalized = weighted_score / similar_users.sum()
        
        if normalized > 0:
            recommendations[movie_id] = normalized
    
    # Sort and get top N
    if not recommendations:
        return pd.DataFrame()
    
    top = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:n_recommendations]
    
    # Convert to dataframe
    result = []
    for movie_id, score in top:
        movie_name = movies[movies['movieId'] == movie_id]['title'].values
        if len(movie_name) > 0:
            result.append({
                'movieId': int(movie_id),
                'title': movie_name[0],
                'recommendation_score': round(score, 4)
            })
    
    return pd.DataFrame(result)
 
# Generate recommendations
print("\n3. Generating recommendations for sample users...")
print("="*60)
 
sample_users = list(user_movie_matrix.index)[:5]
 
for user_id in sample_users:
    print(f"\nRecommendations for User {user_id}:")
    recs = recommend_movies(user_id)
    if len(recs) > 0:
        for idx, row in recs.iterrows():
            print(f"   {idx+1}. {row['title']} (score: {row['recommendation_score']:.4f})")
    else:
        print("   No recommendations available")
 
# Generate for all users
print("\n4. Generating recommendations for all users...")
all_recs = []
count = 0
 
for user_id in user_movie_matrix.index:
    recs = recommend_movies(user_id, n_recommendations=3)
    if len(recs) > 0:
        recs['userId'] = user_id
        all_recs.append(recs)
        count += 1
 
# Save
print("5. Saving recommendations...")
if all_recs:
    recommendations_df = pd.concat(all_recs, ignore_index=True)
    recommendations_df = recommendations_df[['userId', 'movieId', 'title', 'recommendation_score']]
    recommendations_df.to_csv('output/recommendations.csv', index=False)
    print(f"   Generated {len(recommendations_df)} recommendations for {count} users")
    print("   ✓ Saved: output/recommendations.csv")
 
print("\n" + "="*60)
print("✓ RECOMMENDATIONS COMPLETE!")
print("="*60)
 