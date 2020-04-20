# file created by Gabriel de Blois: gabriel.de-blois@epitech.eu

from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import numpy as np

def make_pca_on_df_with_interesting_columns(df, interestingColumns, targets_name, n_components = 2):
    pca = PCA(n_components=n_components)
    x = df[interestingColumns]
    columns = [f"principal component {i}" for i in range (1, n_components + 1)]
    principalComponents = pca.fit_transform(x)
    principalDf = pd.DataFrame(data = principalComponents, columns = columns)
    principalDf[targets_name] = df[targets_name]
    return principalDf, pca

def display_music_features_by_genre_with_pca_2D(principalDf, targets_name, colors, plot_size = 50, title = "PCA"):
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title(title, fontsize = 20)

    targets = principalDf[targets_name].unique()
    colors = [colors[i] for i in range(len(targets))]
    for target, color in zip(targets,colors):
        indicesToKeep = principalDf[targets_name] == target
    
        p1 = list(principalDf.loc[indicesToKeep, 'principal component 1'])
        p2 = list(principalDf.loc[indicesToKeep, 'principal component 2'])
    
        ax.scatter(p1, p2, c = color, s = plot_size)

    ax.legend(targets)
    ax.grid()
    return fig

def display_and_compute_music_features_by_genre_with_pca_2D(df, colors, targets_name, interestingColumns, plot_size = 50, title = "PCA"):
    principalDf, pca = make_pca_on_df_with_interesting_columns(df, interestingColumns, targets_name)
    return display_music_features_by_genre_with_pca_2D(principalDf, targets_name, colors, plot_size=plot_size, title = title), pca

def make_pca_on_df_with_interesting_columns(df, interestingColumns, targets_name, n_components = 2):
    pca = PCA(n_components=n_components)
    x = df[interestingColumns]
    columns = [f"principal component {i}" for i in range (1, n_components + 1)]
    principalComponents = pca.fit_transform(x)
    principalDf = pd.DataFrame(data = principalComponents, columns = columns)
    principalDf[targets_name] = df[targets_name]
    return principalDf, pca

def display_music_features_by_genre_with_pca_3D(principalDf, targets_name, colors, plot_size = 50, title = "PCA"):
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1, projection='3d') 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_zlabel('Principal Component 2', fontsize = 15)
    ax.set_title(title, fontsize = 20)

    targets = principalDf[targets_name].unique()
    colors = [colors[i] for i in range(len(targets))]
    for target, color in zip(targets,colors):
        indicesToKeep = principalDf[targets_name] == target
    
        p1 = list(principalDf.loc[indicesToKeep, 'principal component 1'])
        p2 = list(principalDf.loc[indicesToKeep, 'principal component 2'])
        p3 = list(principalDf.loc[indicesToKeep, 'principal component 3'])
    
        ax.scatter(p1, p2, p3, c = color, s = plot_size)

    ax.legend(targets)
    ax.grid()
    return fig

def display_and_compute_music_features_by_genre_with_pca_3D(df, colors, targets_name, interestingColumns, plot_size = 50, title = "PCA"):
    principalDf, pca = make_pca_on_df_with_interesting_columns(df, interestingColumns, targets_name, n_components = 3)
    return display_music_features_by_genre_with_pca_3D(principalDf, targets_name, colors, plot_size=plot_size, title = title), pca


def my_radarplot(categories: list, values: list, max_value: float=1.0, number_of_ticks: int=4, ticksize: int=8) :
    if number_of_ticks <= 0:
        # avoiding is a division by zero
        return
    
    # number of variable
    N = len(categories)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values += values[:1]
 
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
 
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
 
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, size=8)
 
    # Draw ylabels
    ax.set_rlabel_position(0)
    for tick in range(number_of_ticks):
        ticknumbers = [x / number_of_ticks for x in range(1, number_of_ticks)]
        ticklabels = [f"{x:.2f}" for x in ticknumbers]
        
    plt.yticks(ticknumbers, ticklabels, color="grey", size=ticksize)
    plt.ylim(0, max_value)
 
    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')
 
    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)