import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

while True:
    print("\n")
    print("Welcome to the Weather Data Analysis Tool!")
    print("1. Load Data")
    print("2. Display Data")
    print("3. Analyze Data")
    print("4. Plot garph of the  Data")
    print("5. Exit")
    choice = input("Please enter your choice (1-4): ")
    if choice == '1':
        file_path = input("Enter the path to the weather data CSV file: ")
        try:
            df = pd.read_csv(file_path)
            print("Data loaded successfully!")
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")
    elif choice == '2':
        if 'df' in locals():
            print("Displaying the first 5 rows of the data:")
            print(df)
        else:
            print("No data loaded. Please load the data first.")
    elif choice == '3':
        if 'df' in locals():
            print("\n")
            print("Analyzing data...")
            print(df.info())
            print("\n")
            print("\n")
            print("Summary statistics:")
            print(df.describe())
            print("\n")
            print("\n")
            print("Data types:")
            print(df.dtypes)
        else:
            print("No data loaded. Please load the data first.")
    elif choice == '4':
        if 'df' in locals():
            print("\n")
            plt.figure(figsize=(10, 5))
            plt.plot(df['Date'], df['MaxTemperature_C'], label='Temperature')
            plt.xlabel('Date')
            plt.ylabel('Temperature (°C)')
            plt.title('Temperature Over Time')
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()
            plt.show()
    
        else:
            print("No data loaded. Please load the data first.")
    elif choice == '5':
        print("Exiting the tool. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")





