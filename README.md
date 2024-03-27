# Movie Recommender System

This is a Python application for a movie recommender system built using Streamlit. The system recommends similar movies based on user-selected choices.

## How it works:
1. **Data Retrieval**: The application fetches movie details including posters from The Movie Database (TMDb) API.
2. **Recommendation Algorithm**: It uses a precomputed similarity matrix to recommend similar movies based on the selected movie.
3. **User Interaction**: Users can select a movie from the provided dropdown menu.
4. **Recommendation Display**: After selecting a movie and clicking the "Recommend" button, the system displays recommended movies along with their posters and details.
5. **UI Customization**: Streamlit is used for creating an interactive and user-friendly interface.

## Components:
- `app.py`: This Python script contains the main application logic including data retrieval, recommendation algorithm, and user interface setup.
- `movies_dict.pkl`: A pickle file containing movie data.
- `similarity.pkl`: A pickle file containing the similarity matrix for movies.

## Instructions:
1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the application using `streamlit run app.py`.
4. Select a movie from the dropdown menu and click on the "Recommend" button to view recommended movies.

## Requirements:
- Python 3.x
- Streamlit
- Pandas
- Requests

