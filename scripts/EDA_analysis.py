import pandas as pd  
import numpy as np  
# Load the dataset  
data = pd.read_csv('f:/አስዃላ/online/10 kifia Aim/data/benin-malanville.csv')  
data = pd.read_csv('f:/አስዃላ/online/10 kifia Aim/data/sierraleone-bumbuna.csv')
data = pd.read_csv('f:/አስዃላ/online/10 kifia Aim/data/togo-dapaong_qc.csv')

# Display the first few rows of the dataset  
print(data.head())
# Summary statistics for numeric columns  
summary_statistics = data.describe()  
# Display the summary statistics  
print("\nSummary Statistics for All Columns:")  
print(summary_statistics)
