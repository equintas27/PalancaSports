from ingestion.ingest import openVideo
import os

if __name__ == "__main__":
    openVideo("Videos/Yamal.mp4")
    os.listdir("Videos")