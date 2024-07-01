# ETL-Workflow-Postgres-AirbnbNY

# Airbnb NYC ETL Pipeline Project

## Overview
This project demonstrates a scalable ETL (Extract, Transform, Load) pipeline using the Airbnb New York City dataset. The pipeline is implemented in two parts:
1. **ETL.ipynb**: A Jupyter notebook where the initial data exploration, cleaning, transformation, and loading steps are implemented.
2. **ETL.py**: A Metaflow script that defines a reproducible and robust ETL workflow, automating the steps defined in the notebook.

## Project Structure
<img width="555" alt="Screenshot 2024-07-01 at 12 23 53" src="https://github.com/vaibhavnagar02/ETL-Workflow-Postgres-AirbnbNY/assets/87512533/09c1ae29-f37f-4e79-9acf-3871a410486e">


## Dataset
The dataset used in this project is the **Airbnb New York City 2019** dataset, available on Kaggle. It contains information about Airbnb listings in NYC, including details about the hosts, location, price, availability, and more.

## Setup Instructions

### Prerequisites
1. PostgreSQL database set up on your local machine or a cloud instance.
2. Python environment with necessary libraries installed: ( You can directly pip install -r requirements.txt )
   - pandas
   - SQLAlchemy
   - Metaflow
  

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/vaibhavnagar02/ETL-Workflow-Postgres-AirbnbNY.git
    cd airbnb-nyc-etl
    ```

2. Install the required Python packages:
    ```sh
    pip install pandas sqlalchemy metaflow
    or
    pip install -r requirements.txt
    ```

3. Set up your PostgreSQL database and create a database named `airbnb-ny`. Update the database connection parameters in both `ETL.ipynb` and `ETL.py` with your PostgreSQL credentials.

### Running the Project

#### 1. Data Exploration and Initial ETL Development
The `ETL.ipynb` notebook is used for the initial ETL development:

- **Data Ingestion**: Load the Airbnb NYC dataset from a CSV file (`AB_NYC_2019.csv`) into a pandas DataFrame.
- **Data Cleaning**:
  - Fill missing values in the `name` and `host_name` columns with 'Absent'.
  - Drop the `last_review` and `reviews_per_month` columns as they are not needed for the analysis.
- **Data Transformation**:
  - Calculate the average price per neighborhood and add it as a new column (`avg_price_neighborhood`).
  - Calculate the total number of listings per neighborhood and add it as a new column (`listings_count_neighborhood`).
- **Data Loading**: Load the transformed DataFrame into a PostgreSQL table named `airbnb_listings_enhanced`.

To run the notebook:
```sh
python ETL.py run```

The ETL.py script uses Metaflow to define an automated ETL workflow:

	•	start: Initialize the ETL flow.
	•	load_data: Load data from the PostgreSQL table into a pandas DataFrame.
	•	transform_data:
	•	Handle missing values by filling ‘Absent’ in name and host_name.
	•	Drop last_review and reviews_per_month columns.
	•	Calculate the average price and total listings per neighborhood.
	•	load_to_postgres: Load the transformed data back into the PostgreSQL database.
	•	end: Conclude the ETL flow.
