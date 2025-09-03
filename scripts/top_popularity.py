from pathlib import Path
from src.models.popularity import PopularityRecommender

if __name__ == "__main__":
    raw = Path("data/raw/ml-25m")
    rec = PopularityRecommender(min_ratings=200, top_n=10)
    print(rec.from_files((raw)))
