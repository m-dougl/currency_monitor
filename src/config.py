from pyspark.sql import SparkSession
from dotenv import load_dotenv
import os 

load_dotenv()

def create_spark_session():
    return SparkSession.builder.appName("currency_etl") \
        .config("spark.jars.packages", "org.postgresql:postgresql:42..0") \
        .getOrCreate()
        
POSTGRES_CONFIG = {
    'url': os.getenv('POSTGRES_URL'),
    'properties': {
        'user': os.getenv('POSTGRES_USER'),
        'password': os.getenv('POSTGRES_PASSWORD'),
        'driver': 'org.postgresql.Driver'
    }
}

API_URL = 'https://api.coingecko.com/api/v3/coins/markets'