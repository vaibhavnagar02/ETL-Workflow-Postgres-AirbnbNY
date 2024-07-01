from metaflow import FlowSpec, step
import pandas as pd
from sqlalchemy import create_engine

class ETLFlow(FlowSpec):

    @step
    def start(self):
        """
        Start step of the ETL flow.
        """
        print("Starting the ETL flow...")
        self.next(self.load_data)

    @step
    def load_data(self):
        """
        Load data from the PostgreSQL table into a pandas DataFrame.
        """
        # Database connection parameters
        self.db_name = 'airbnb-ny'
        self.db_user = 'postgres'  # replace with your PostgreSQL username
        self.db_password = 'nagar7754'  # replace with your PostgreSQL password
        self.db_host = 'localhost'  # or the host of your PostgreSQL server
        self.db_port = '5432'  # default PostgreSQL port

        # Create a connection string
        self.connection_string = f'postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'
        
        # Load data into a pandas DataFrame
        self.query = 'SELECT * FROM airbnb_listings'  # replace with your table name
        engine = create_engine(self.connection_string)
        self.df = pd.read_sql(self.query, engine)

        print("Data loaded successfully.")
        self.next(self.transform_data)

    @step
    def transform_data(self):
        """
        Transform the data by handling missing values, normalizing, and adding new columns.
        """
        # Handle missing values
        self.df['name'].fillna('Absent', inplace=True)
        self.df['host_name'].fillna('Absent', inplace=True)

        # Drop unnecessary columns
        self.df.drop(['last_review', 'reviews_per_month'], axis=1, inplace=True)

        # Calculate the average price per neighborhood
        self.df['avg_price_neighborhood'] = self.df.groupby('neighbourhood')['price'].transform('mean')

        # Calculate the total number of listings per neighborhood
        self.df['listings_count_neighborhood'] = self.df.groupby('neighbourhood')['id'].transform('count')

        print("Data transformed successfully.")
        self.next(self.load_to_postgres)

    @step
    def load_to_postgres(self):
        """
        Load the transformed data back into the PostgreSQL database.
        """
        # Define the name of the new table
        new_table_name = 'airbnb_listings_update'

        # Create a SQLAlchemy engine
        engine = create_engine(self.connection_string)

        # Upload the modified DataFrame back to PostgreSQL
        self.df.to_sql(new_table_name, engine, if_exists='replace', index=False)

        print(f"DataFrame successfully uploaded to table '{new_table_name}' in the PostgreSQL database.")
        self.next(self.end)

    @step
    def end(self):
        """
        End step of the ETL flow.
        """
        print("ETL flow completed.")

if __name__ == '__main__':
    ETLFlow()