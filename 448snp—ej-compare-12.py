import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the GWAS data
gwas = pd.read_csv("asia<0.05.txt", delimiter='\t')

# Add a column 'i' to represent the index
gwas["i"] = gwas.index

# Calculate -log10(p) and store it in a new column 'log10_p'
gwas["log10_p_JPT"] = -np.log10(gwas["P"])
gwas["log10_p_EU"] = -np.log10(gwas["Pvalue"])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the scatterplot for Japan (JPT)
sns.scatterplot(data=gwas, x='i', y='log10_p_JPT', hue='CHR', palette='colorblind', s=20, ax=ax)

# Create the scatterplot for Europe (EU)
sns.scatterplot(data=gwas, x='i', y='log10_p_EU', hue='Chromosome', palette='colorblind', s=20, ax=ax, alpha=0.2)

# Calculate the median position for each chromosome
chrom_df = gwas.groupby('CHR')['i'].median()

# Set x-ticks and labels
ax.set_xticks(chrom_df)
ax.set_xticklabels([label.split(":")[1] for label in chrom_df.index])

# Set x-label and y-axis limits
ax.set_xlabel('Chromosome')
ax.set_ylabel('-log10(P)')
ax.set_ylim(0, 20)

# Add a horizontal dashed line at -log10(5e-8)
ax.axhline(y=-np.log10(1e-8), linewidth=2, linestyle="--", color="gray")

# Annotate specific SNP labels
# Annotate specific SNP labels
snp_labels = ['rs11118328','rs2322599','rs4732729','rs80256323','rs586274','rs10410651','rs2927439','rs10402271','rs71364511','rs7412','rs11672748']

# Annotate for Asian data
for label in snp_labels:
    asia_indices = gwas[gwas['SNP'] == label].index
    for idx in asia_indices:
        x_coord = gwas.loc[idx, 'i']
        y_coord = gwas.loc[idx, 'log10_p_JPT']
        ax.annotate(label, (x_coord, y_coord), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

# Annotate for European data
for label in snp_labels:
    europe_indices = gwas[gwas['MarkerName'] == label].index
    for idx in europe_indices:
        x_coord = gwas.loc[idx, 'i']
        y_coord = gwas.loc[idx, 'log10_p_EU']
        ax.annotate(label, (x_coord, y_coord), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

# Add a legend outside the plot
ax.legend(title='Chromosome', loc='upper right', bbox_to_anchor=(1.2, 1))

# Show the plot
plt.tight_layout()
plt.show()
