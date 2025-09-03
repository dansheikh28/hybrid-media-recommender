from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import pandas as pd


@dataclass
class PopularityRecommender:
    min_ratings: int = 50  # filter out movies with too few ratings
    top_n: int = 10  # how many to recommend

    def compute_top(
        self, ratings_df: pd.DataFrame, movies_df: pd.DataFrame
    ) -> pd.DataFrame:
        # count ratings per movie
        counts = ratings_df.groupby("movieId").size().rename("num_ratings")
        means = ratings_df.groupby("movieId")["rating"].mean().rename("avg_rating")

        stats = pd.concat([counts, means], axis=1).reset_index()
        stats = stats[stats["num_ratings"] >= self.min_ratings]

        merged = stats.merge(movies_df, on="movieId", how="left")
        ranked = merged.sort_values(
            ["num_ratings", "avg_rating"], ascending=[False, False]
        )
        return ranked.head(self.top_n)[
            ["movieId", "title", "avg_rating", "num_ratings"]
        ]

    def from_files(self, raw_dir: Path) -> pd.DataFrame:
        ratings = pd.read_csv(raw_dir / "ratings.csv")
        movies = pd.read_csv(raw_dir / "movies.csv")
        return self.compute_top(ratings, movies)
