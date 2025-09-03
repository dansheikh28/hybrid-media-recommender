import pandas as pd
from src.models.popularity import PopularityRecommender


def test_compute_top_returns_n_rows():
    ratings = pd.DataFrame(
        {
            "userId": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
            "movieId": [10, 10, 10, 20, 10, 20, 20, 20, 30, 30],
            "rating": [4, 5, 5, 4, 4, 5, 4, 5, 5, 5],
        }
    )
    movies = pd.DataFrame(
        {
            "movieId": [10, 20, 30],
            "title": ["A", "B", "C"],
        }
    )

    rec = PopularityRecommender(min_ratings=2, top_n=2)
    top = rec.compute_top(ratings, movies)

    assert len(top) == 2
    assert set(top.columns) == {"movieId", "title", "avg_rating", "num_ratings"}
