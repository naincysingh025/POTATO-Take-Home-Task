# POTATO-Take-Home-Task
## Overview
This project ingests tweet data from a TSV file and provides querying functionalities via Elasticsearch. Optionally, it can be run as a Flask API and packaged in Docker.

## Setup Instructions

1. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   python ingest_data.py path_to_your_tsv_file
   python query_data.py
   python api.py
   docker build -t potato-twitter .
   docker run -p 5000:5000 potato-twitter
