import cProfile
import pandas as pd

def pandas():
    # Load the messy dataset
    df = pd.read_csv('messy_dataset.csv')

    # Display the first few rows of the dataset to understand its structure
    print("Original dataset:")
    print(df.head())

    # Check for missing values and handle them
    print("\nHandling missing values:")
    print("Number of missing values before handling:", df.isnull().sum().sum())
    df.fillna(method='ffill', inplace=True)  # Forward fill missing values
    print("Number of missing values after handling:", df.isnull().sum().sum())

    # Remove duplicates
    print("\nRemoving duplicates:")
    print("Number of duplicates before removing:", df.duplicated().sum())
    df.drop_duplicates(inplace=True)
    print("Number of duplicates after removing:", df.duplicated().sum())

    # Convert data types if necessary
    print("\nConverting data types:")
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    # Perform additional cleaning and transformations as needed

    # Save the cleaned dataset
    df.to_csv('cleaned_dataset.csv', index=False)

    print("\nCleaned dataset saved successfully.")

cProfile.run('pandas()')