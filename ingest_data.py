# ingest_data.py
import pandas as pd
from elasticsearch import Elasticsearch
import sys

# Set up Elasticsearch
es = Elasticsearch()

def ingest_data(file_path):
    try:
        # Load the TSV data into a pandas DataFrame
        df = pd.read_csv(file_path, sep='\t')
        
        # Clean the data (Remove NaN or invalid rows)
        df = df.dropna(subset=['tweet_id', 'user_id', 'text'])
        
        # Ingest each row into Elasticsearch
        for _, row in df.iterrows():
            doc = row.to_dict()
            es.index(index='tweets', id=row['tweet_id'], body=doc)
        
        print(f"Successfully ingested data from {file_path}.")
    except Exception as e:
        print(f"Error during data ingestion: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python ingest_data.py <path_to_tsv_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    ingest_data(file_path)
