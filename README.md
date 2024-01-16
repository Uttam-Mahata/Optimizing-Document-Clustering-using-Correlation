# Document Clustering Optimization

## Overview

This Python script optimizes document clustering using correlation-based clustering. It preprocesses text documents, applies clustering optimization, and compares the performance of various clustering algorithms.

## Prerequisites

Make sure you have the necessary Python packages installed:

pip install pandas numpy scikit-learn matplotlib nltk


## Usage
- Preprocessing Documents:

Place your text documents in the 'Input' folder.
Run the following command to preprocess the documents and generate a CSV file:
python main.py
- Optimizing Clusters:

The script performs optimization for different threshold values.
View the results by running the script. It will display the optimal threshold values, the number of clusters, and the error for each threshold.
- Comparison of Clustering Algorithms:

The script compares the optimized clustering results with popular clustering algorithms (KMeans, AffinityPropagation, GaussianMixture, AgglomerativeClustering).
The comparison includes metrics such as Davies Bouldin Index, Silhouette Score, Calinski Harabasz Score, Adjusted Rand Score, and Normalized Mutual Information.
## Results
The script generates graphical representations of the number of clusters and errors for different threshold values.
Optimal threshold values are highlighted, assisting in selecting the best configuration.
## Dependencies
- Python 3.x
- Libraries: pandas, numpy, scikit-learn, matplotlib, nltk

## Contributors

| Name              |  GitHub Profile                                   |
|-------------------|---------------------------------------------------|
| Suraj Kashyap     |  [surajkashyap](https://github.com/imsuraj675)    |
| Uttam Mahata      | [uttam-mahata](https://github.com/Uttam-Mahata)   |


If you're interested in contributing, please reach out to the project maintainer or submit a pull request. We appreciate your support!
