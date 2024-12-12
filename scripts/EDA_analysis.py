import pandas as pd  

# Load the CSV data  
file_path = 'f:/አስዃላ/online/10 kifia Aim/data/togo-dapaong_qc.csv'  # Replace with your file path  
data = pd.read_csv(file_path)  

# Display the first few rows of the dataset  
print(data.head())  

# 1. Check for missing values in GHI, DNI, DHI columns  
missing_values = data[['GHI', 'DNI', 'DHI']].isnull().sum()  
print("Missing values in GHI, DNI, DHI:")  
print(missing_values)  

# 2. Check for incorrect entries (e.g., negative values)  
negative_values = {  
    'GHI': data[data['GHI'] < 0].shape[0],  
    'DNI': data[data['DNI'] < 0].shape[0],  
    'DHI': data[data['DHI'] < 0].shape[0],  
    'ModA': data[data['ModA'] < 0].shape[0],  
    'ModB': data[data['ModB'] < 0].shape[0],  
    'WS': data[data['WS'] < 0].shape[0],  
    'WSgust': data[data['WSgust'] < 0].shape[0],  
}  

print("\nNumber of negative values found:")  
print(negative_values)  

# 3. Check for outliers in sensor readings ModA, ModB and wind speed WS, WSgust  
def find_outliers(df, column):  
    Q1 = df[column].quantile(0.25)  
    Q3 = df[column].quantile(0.75)  
    IQR = Q3 - Q1  
    return df[(df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR))]  

outliers_ModA = find_outliers(data, 'ModA')  
outliers_ModB = find_outliers(data, 'ModB')  
outliers_WS = find_outliers(data, 'WS')  
outliers_WSgust = find_outliers(data, 'WSgust')  

print("\nOutliers in ModA:")  
print(outliers_ModA)  

print("\nOutliers in ModB:")  
print(outliers_ModB)  

print("\nOutliers in WS:")  
print(outliers_WS)  

print("\nOutliers in WSgust:")  
print(outliers_WSgust)  

# Optional: Save the outlier records to a new CSV file for further examination  
outliers_combined = pd.concat([outliers_ModA, outliers_ModB, outliers_WS, outliers_WSgust])  
outliers_combined.to_csv('outliers.csv', index=False)