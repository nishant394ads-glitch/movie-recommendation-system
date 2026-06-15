import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os
import plotly.express as px
import plotly.graph_objects as go
 
# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="Movie Recommendation Engine",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "### Movie Recommendation System\nAI-Powered Collaborative Filtering Engine\nCognevance Technologies"
    }
)
 
# ============================================================================
# CUSTOM PROFESSIONAL STYLING
# ============================================================================
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    .main {
        padding: 2rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .metric-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
        transition: transform 0.2s;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    
    .recommendation-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        transition: transform 0.2s;
    }
    
    .recommendation-card:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    .recommendation-card h3 {
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
    }
    
    .recommendation-card p {
        font-size: 0.95rem;
        opacity: 0.9;
    }
    
    .stat-box {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .stat-box h2 {
        color: #667eea;
        font-size: 2.5rem;
        margin: 0.5rem 0;
    }
    
    .stat-box p {
        color: #666;
        font-size: 0.95rem;
        margin: 0;
    }
    
    .section-title {
        color: #667eea;
        font-size: 2rem;
        margin: 2rem 0 1rem 0;
        padding-bottom: 1rem;
        border-bottom: 3px solid #667eea;
    }
    
    .info-box {
        background: #e8f4f8;
        border-left: 4px solid #667eea;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .success-box {
        background: #d4edda;
        border-left: 4px solid #28a745;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        color: #155724;
    }
    
    .button-custom {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        font-weight: 600;
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        border-top: 2px solid #ddd;
        margin-top: 3rem;
    }
    
</style>
""", unsafe_allow_html=True)
 
# ============================================================================
# LOAD DATA
# ============================================================================
@st.cache_data
def load_data():
    ratings = pd.read_csv('data/ratings_cleaned.csv')
    movies = pd.read_csv('data/movies_cleaned.csv')
    recommendations = pd.read_csv('output/recommendations.csv')
    return ratings, movies, recommendations
 
try:
    ratings, movies, recommendations = load_data()
    data_loaded = True
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.info("Make sure all data files are in the correct locations")
    data_loaded = False
 
# ============================================================================
# SIDEBAR CONFIGURATION
# ============================================================================
with st.sidebar:
    st.markdown("---")
    st.markdown("### 🎬 Navigation Menu")
    st.markdown("---")
    
    page = st.radio(
        "Select Page:",
        ["🏠 Dashboard", "🎯 Get Recommendations", "📊 Analytics", "🔍 Movie Explorer", "📄 Documentation"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    
    if data_loaded:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Users", f"{ratings['userId'].nunique()}")
            st.metric("Movies", f"{movies['movieId'].nunique():,}")
        with col2:
            st.metric("Ratings", f"{len(ratings):,}")
            st.metric("Recs", f"{len(recommendations):,}")
    
    st.markdown("---")
    st.markdown("""
    ### 📚 About
    **Movie Recommendation Engine**
    
    AI-powered system using collaborative filtering
    
    🏢 Cognevance Technologies  
    📍 AI/ML Internship Project
    """)
 
# ============================================================================
# PAGE 1: DASHBOARD
# ============================================================================
if page == "🏠 Dashboard":
    # Header
    st.markdown("""
    <div class="header">
        <h1>🎬 Movie Recommendation Engine</h1>
        <p>AI-Powered Collaborative Filtering System</p>
    </div>
    """, unsafe_allow_html=True)
    
    if not data_loaded:
        st.error("⚠️ Unable to load data. Please check your files.")
        st.stop()
    
    # Key Metrics
    st.markdown("<h2 class='section-title'>📈 System Overview</h2>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stat-box">
            <h2>{ratings['userId'].nunique()}</h2>
            <p>👥 Active Users</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-box">
            <h2>{movies['movieId'].nunique():,}</h2>
            <p>🎬 Movies</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-box">
            <h2>{len(ratings):,}</h2>
            <p>⭐ Total Ratings</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="stat-box">
            <h2>{len(recommendations):,}</h2>
            <p>💡 Recommendations</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Algorithm Explanation
    st.markdown("<h2 class='section-title'>🧠 How It Works</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Algorithm: User-Based Collaborative Filtering
        
        **Step 1: User-Movie Matrix**
        - Create matrix: Users × Movies
        - Values: User ratings
        
        **Step 2: Calculate Similarity**
        - Use cosine similarity metric
        - Measure rating pattern similarity
        
        **Step 3: Find Similar Users**
        - Identify top 10 most similar users
        - Based on rating behavior
        """)
    
    with col2:
        st.markdown("""
        **Step 4: Generate Recommendations**
        - Look at movies similar users rated
        - Calculate weighted scores
        - Rank by recommendation strength
        
        **Step 5: Filter Results**
        - Exclude already-watched movies
        - Return top 5 recommendations
        - Include confidence scores
        
        **Why It Works**
        - Based on proven recommendation logic
        - Captures user preferences
        - Personalized for each user
        """)
    
    st.markdown("---")
    
    # Visualizations
    st.markdown("<h2 class='section-title'>📊 Data Visualizations</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if os.path.exists('output/01_movie_analysis.png'):
            img = Image.open('output/01_movie_analysis.png')
            st.image(img, caption="📊 Movie Analysis Dashboard", use_column_width=True)
    
    with col2:
        if os.path.exists('output/02_user_activity.png'):
            img = Image.open('output/02_user_activity.png')
            st.image(img, caption="👥 User Activity Distribution", use_column_width=True)
    
    st.image(Image.open('output/03_genre_analysis.png'), caption="🎬 Genre Analysis", use_column_width=True)
 
# ============================================================================
# PAGE 2: GET RECOMMENDATIONS
# ============================================================================
elif page == "🎯 Get Recommendations":
    st.markdown("""
    <div class="header">
        <h1>🎯 Personalized Recommendations</h1>
        <p>Get movies tailored to your taste</p>
    </div>
    """, unsafe_allow_html=True)
    
    if not data_loaded:
        st.error("⚠️ Unable to load data.")
        st.stop()
    
    st.markdown("""
    <div class="info-box">
    <strong>ℹ️ How to use:</strong> Enter a User ID to receive personalized movie recommendations 
    based on the collaborative filtering algorithm. Each recommendation includes a confidence score.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    valid_users = sorted(recommendations['userId'].unique())
    
    with col1:
        user_id = st.selectbox(
            "Select User ID:",
            valid_users,
            index=0,
            help="Choose from available users in the system"
        )
    
    with col2:
        st.write("")
        st.write("")
        num_recs = st.slider("# of Recommendations:", 1, 10, 5)
    
    with col3:
        st.write("")
        st.write("")
        get_recs = st.button("🔍 Get Recommendations", use_container_width=True, key="rec_button")
    
    st.markdown("---")
    
    if get_recs:
        user_recs = recommendations[recommendations['userId'] == user_id].head(num_recs)
        
        if len(user_recs) > 0:
            st.markdown(f"""
            <div class="success-box">
            ✅ <strong>Found {len(user_recs)} personalized recommendations for User {int(user_id)}!</strong>
            </div>
            """, unsafe_allow_html=True)
            
            for idx, row in user_recs.iterrows():
                score_percentage = int(row['recommendation_score'] * 20)  # Convert to percentage
                
                st.markdown(f"""
                <div class="recommendation-card">
                    <h3>#{idx + 1}: {row['title']}</h3>
                    <p><strong>Movie ID:</strong> {int(row['movieId'])}</p>
                    <p><strong>Confidence Score:</strong> {row['recommendation_score']:.4f}</p>
                    <div style="background: rgba(255,255,255,0.2); border-radius: 8px; overflow: hidden; height: 8px; margin-top: 0.5rem;">
                        <div style="background: rgba(255,255,255,0.8); height: 100%; width: {score_percentage}%;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning(f"❌ No recommendations found for User {int(user_id)}")
 
# ============================================================================
# PAGE 3: ANALYTICS
# ============================================================================
elif page == "📊 Analytics":
    st.markdown("""
    <div class="header">
        <h1>📊 Advanced Analytics</h1>
        <p>In-depth analysis of the recommendation system</p>
    </div>
    """, unsafe_allow_html=True)
    
    if not data_loaded:
        st.error("⚠️ Unable to load data.")
        st.stop()
    
    # Rating Statistics
    st.markdown("<h2 class='section-title'>⭐ Rating Statistics</h2>", unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Average Rating", f"{ratings['rating'].mean():.2f}/5.0")
    with col2:
        st.metric("Median Rating", f"{ratings['rating'].median():.1f}")
    with col3:
        st.metric("Mode Rating", f"{ratings['rating'].mode()[0]:.0f}⭐")
    with col4:
        st.metric("Min Rating", f"{ratings['rating'].min()}")
    with col5:
        st.metric("Max Rating", f"{ratings['rating'].max()}")
    
    st.markdown("---")
    
    # User Behavior
    st.markdown("<h2 class='section-title'>👥 User Behavior</h2>", unsafe_allow_html=True)
    
    user_counts = ratings.groupby('userId')['rating'].count()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Avg Ratings/User", f"{user_counts.mean():.0f}")
    with col2:
        st.metric("Most Active User", f"{user_counts.max()} ratings")
    with col3:
        st.metric("Least Active User", f"{user_counts.min()} rating")
    with col4:
        st.metric("Median/User", f"{user_counts.median():.0f}")
    
    st.markdown("---")
    
    # Top Content
    st.markdown("<h2 class='section-title'>🎬 Top Content</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Most Rated Movies")
        top_movies_list = ratings.merge(movies, on='movieId').groupby('title')['rating'].count().sort_values(ascending=False).head(10)
        
        df_top = pd.DataFrame({
            'Movie': top_movies_list.index,
            'Ratings': top_movies_list.values
        })
        df_top['Rank'] = range(1, len(df_top) + 1)
        st.dataframe(df_top[['Rank', 'Movie', 'Ratings']], use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("#### Highest Rated Movies")
        top_rated_list = ratings.merge(movies, on='movieId').groupby('title')['rating'].mean().sort_values(ascending=False).head(10)
        
        df_rated = pd.DataFrame({
            'Movie': top_rated_list.index,
            'Rating': top_rated_list.values
        })
        df_rated['Rank'] = range(1, len(df_rated) + 1)
        st.dataframe(df_rated[['Rank', 'Movie', 'Rating']], use_container_width=True, hide_index=True)
 
# ============================================================================
# PAGE 4: MOVIE EXPLORER
# ============================================================================
elif page == "🔍 Movie Explorer":
    st.markdown("""
    <div class="header">
        <h1>🔍 Movie Explorer</h1>
        <p>Search and discover movies in the database</p>
    </div>
    """, unsafe_allow_html=True)
    
    if not data_loaded:
        st.error("⚠️ Unable to load data.")
        st.stop()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        search_query = st.text_input("🔍 Search for a movie:", placeholder="e.g., The Shawshank Redemption")
    
    with col2:
        st.write("")
        search_button = st.button("Search", use_container_width=True)
    
    if search_button and search_query:
        # Search in movies
        search_results = movies[movies['title'].str.contains(search_query, case=False, na=False)]
        
        if len(search_results) > 0:
            st.markdown(f"<div class='success-box'>✅ Found {len(search_results)} movie(s)</div>", unsafe_allow_html=True)
            
            for idx, row in search_results.iterrows():
                movie_id = row['movieId']
                movie_title = row['title']
                movie_genres = row['genres'] if 'genres' in row else "N/A"
                
                # Get rating info
                movie_ratings = ratings[ratings['movieId'] == movie_id]['rating']
                avg_rating = movie_ratings.mean() if len(movie_ratings) > 0 else 0
                num_ratings = len(movie_ratings)
                
                st.markdown(f"""
                <div class="recommendation-card">
                    <h3>{movie_title}</h3>
                    <p><strong>Genres:</strong> {movie_genres}</p>
                    <p><strong>Average Rating:</strong> {avg_rating:.2f}/5.0 ({num_ratings} ratings)</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning(f"❌ No movies found matching '{search_query}'")
 
# ============================================================================
# PAGE 5: DOCUMENTATION
# ============================================================================
elif page == "📄 Documentation":
    st.markdown("""
    <div class="header">
        <h1>📄 Project Documentation</h1>
        <p>Complete project details and information</p>
    </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists('report.md'):
        with open('report.md', 'r', encoding='utf-8') as f:
            report_content = f.read()
        st.markdown(report_content)
    else:
        st.warning("📋 Report file not found. Please ensure report.md exists.")
    
    st.markdown("---")
    st.markdown("""
    ### 🔗 Project Links
    
    - **GitHub Repository:** [movie-recommendation-system](https://github.com/nishant394ads-glitch/movie-recommendation-system)
    - **Dataset:** MovieLens
    - **Author:** Nishant
    - **Organization:** Cognevance Technologies
    """)
 
# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
<div class="footer">
    <h4>🎬 Movie Recommendation System</h4>
    <p>AI-Powered Collaborative Filtering Engine</p>
    <p> AI/ML Internship Project</p>
</div>
""", unsafe_allow_html=True)