# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define the input and output file paths
input_file_path = "/Volumes/a/00.NCGG_GWAS_data/japanchr19_data.txt"
output_file_path = "/Volumes/a/00.NCGG_GWAS_data/japanchr19_0.05data.txt"

# Read the input file into a DataFrame
df = pd.read_csv(input_file_path, delimiter='\t')  # Assuming tab-separated data

# Filter data based on P-value less than 0.05
filtered_data = df[df['P'] < 0.05]

# Write the filtered data to the output file
filtered_data.to_csv(output_file_path, sep='\t', index=False)

print(f"Filtered data for P-value < 0.05 saved to {output_file_path}")
