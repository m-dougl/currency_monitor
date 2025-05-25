import requests 
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType
)
from config import API_URL

def fetch_from_api(spark):
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
    except requests.RequestException as e:
        raise RuntimeError(f'Error to access API: {e}')
    
    schema = StructType([
        StructField("id", StringType(), True),
        StructField("symbol", StringType(), True),
        StructField("name", StringType(), True),
        StructField("current_price", DoubleType(), True),
        StructField("market_cap", DoubleType(), True)
    ])
    return spark.createDataFrame(data, schema)