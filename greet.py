import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

def process_data(data):
    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data)
    return df

def plot_data(df):
    df.plot(kind='bar', x='category', y='value')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.title('Category Values')
    plt.show()

def main():
    url = 'https://api.example.com/data'
    data = fetch_data(url)
    df = process_data(data)
    plot_data(df)

if __name__ == "__main__":
    main()
