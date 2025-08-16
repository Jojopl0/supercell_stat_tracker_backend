import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BRAWL_STATS_API_KEY = os.getenv("BRAWL_STATS_API_KEY")
    CLASH_ROYALE_API_KEY = os.getenv("CLASH_ROYALE_API_KEY")
    #REDIS_HOST = os.getenv("REDIS_HOST")
    #REDIS_PORT = os.getenv("REDIS_PORT")
    #REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
    #REDIS_DB = os.getenv("REDIS_DB")
    REDIS_URL= "redis://localhost:6379"

    # API Base URLs
    CLASH_ROYALE_BASE_URL = "https://api.clashroyale.com/v1"
    BRAWL_STARS_BASE_URL = "https://api.brawlstars.com/v1"


settings = Settings()