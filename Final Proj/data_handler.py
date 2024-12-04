def load_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    data = data.dropna()  # Handle missing values
    return data

# Provide the correct path to your dataset
file_path = r"C:\Users\Canada\Desktop\Vince\My stuffs\All Works\3rd Year Subjects\My Works\CSST 102 Basic Machine Learning\Final Proj\data.csv"

# Call the function
data = load_data(file_path)
print(data.head())  # Just for debugging purposes