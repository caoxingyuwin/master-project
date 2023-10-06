import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the GWAS data
gwas = pd.read_csv("EUgwas2.txt", delimiter='\t')

# Add a column 'i' to represent the index
gwas["i"] = gwas.index

# Calculate -log10(p) and store it in a new column 'log10_p'
gwas["log10_p"] = -np.log10(gwas["Pvalue"])

# Create the initial scatterplot
plot = sns.scatterplot(data=gwas, x='i', y='log10_p', hue='Chromosome', palette='dark', s=4, legend=None)

# Calculate the median position for each chromosome
chrom_df = gwas.groupby('Chromosome')['i'].median()

# Set x-ticks and labels
plt.xticks(chrom_df, labels=chrom_df.index)

# Set x-label and y-axis limits
plot.set_xlabel('Chromosome')
plot.set_ylim(0, 20)

# Add a horizontal dashed line at -log10(5e-8)
plot.axhline(y=-np.log10(5e-8), linewidth=2, linestyle="--", color="gray")

# Show the plot
plt.show()
