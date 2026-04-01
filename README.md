# Streamlit Example

A Streamlit demo app that visualizes Uber pickups data in NYC and supports querying data from MySQL databases.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Configure database (optional):

```bash
cp configs/.database.yaml.example configs/.database.yaml
```

Edit `configs/.database.yaml` with your MySQL connection details.

## Run

```bash
streamlit run app/main.py
```

## Features

- Interactive map of Uber pickups in NYC
- Filter pickups by hour using a slider
- Histogram of pickups by hour
- MySQL database integration with YAML-based configuration
