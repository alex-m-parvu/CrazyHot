import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd


# Function to plot the Crazy Hot Matrix
def plot_crazy_hot_matrix(hot_values, crazy_values, alpha=0.5, return_area=False, plot = True):
    """
    Plots the Crazy Hot Matrix and optionally returns the area where the center of the data points is located.

    Parameters:
    hot_values (list or array): A list or array of hot values.
    crazy_values (list or array): A list or array of crazy values.
    alpha (float, optional): Transparency level for the data points. Default is 0.5.
    return_area (bool, optional): If True, the function returns the area where the cluster center is located. Default is False.
    plot (bool, optional): If True, the function plots the Crazy Hot Matrix. Default is True.

    Returns:
    str: The name of the area where the cluster center is located, if return_area is True.

    The plot includes several zones:
    - "No Go Zone": x < 5
    - "Danger Zone": Above the diagonal line for x >= 5
    - "Fun Zone": Below the diagonal line for 5 <= x < 8
    - "Girlfriend Zone": Below the diagonal line for x >= 8 and y >= 7
    - "Wife Zone": x >= 8 and 5 <= y < 7
    - "Unicorn Zone": x >= 8 and y < 5
    - "Trany Zone": y < 4

    The function uses KMeans clustering to find the center of the data points and determines the zone based on the center's coordinates.
    """
    
    # Convert inputs to numpy arrays
    hot_values = np.array(hot_values)
    crazy_values = np.array(crazy_values)
    
    # Combine hot and crazy values into a 2D array
    data = np.column_stack((hot_values, crazy_values))
    
    # Use KMeans to find the center of the cluster
    kmeans = KMeans(n_clusters=1)
    kmeans.fit(data)
    center = kmeans.cluster_centers_[0]

    if plot:
        # Plot the hot and crazy values
        plt.scatter(hot_values, crazy_values, c='blue', label='Data Points', alpha=alpha)
        
        # Plot the center of the cluster
        plt.scatter(center[0], center[1], c='red', marker='o', label='Cluster Center', s=100)
        
        # Hash out the area where x is lower than 5
        plt.axvspan(0, 5, color='gray', alpha=0.5, hatch='//')
        
        # Add "No Go Zone" text
        plt.text(1, 6.5, 'No Go Zone', fontsize=16, color='gray', weight='bold')
        
        # Draw a diagonal line (Crazy Line)
        plt.plot([0, 10], [4, 10], color='purple', linestyle='--', label='Crazy Line', linewidth=3.5)
        
        # Hash out the area above the diagonal and x > 5
        x = np.linspace(5, 10, 100)
        y = 0.6 * x + 4
        plt.fill_between(x, y, 10, color='red', alpha=0.3, hatch='x')
        
        # Add "Danger Zone" text
        plt.text(5.5, 9.3, 'Danger Zone', fontsize=16, color='red', weight='bold')
        
        # Hash out the area below the diagonal and x is between 5 and 8
        x_below = np.linspace(5, 8, 100)
        y_below = 0.6 * x_below + 4
        plt.fill_between(x_below, 4, y_below, color='blue', alpha=0.3, hatch='/')
        plt.text(5.3, 6, 'Fun Zone', fontsize=16, color='blue', weight='bold')
        
        # Hash out the area below the diagonal where y is 7 or above and x is 8 or above
        x_above_8 = np.linspace(8, 10, 100)
        y_above_7 = 0.6 * x_above_8 + 4
        plt.fill_between(x_above_8, 7, y_above_7, color='yellow', alpha=0.3, hatch='/')
        plt.text(8, 7.8, 'Girlfriend\n    Zone', fontsize=13, color='gray', weight='bold')
        
        # Hash out the area where x is 8 or above and y is between 5 and 7
        x_green = np.linspace(8, 10, 100)
        plt.fill_between(x_green, 5, 7, color='green', alpha=0.3, hatch='|')
        plt.text(8, 6, 'Wife Zone', fontsize=13, color='green', weight='bold')
    
        # Hash out the area where x is 8 or above and y is between 5 and 7
        x_pink = np.linspace(8, 10, 100)
        plt.fill_between(x_pink, 4, 5, color='pink', alpha=0.3, hatch='|')
        plt.text(8.2, 4.1, 'Unicorn\n   Zone', fontsize=13, color='purple', weight='bold')
    
        # Hash out the area where x is 8 or above and y is between 5 and 7
        x_trany = np.linspace(0, 10, 100)
        plt.fill_between(x_trany, 0, 4, color='red', alpha=0.3, hatch='|')
        plt.text(0.5, 1.5, 'Trany Zone', fontsize=50, color='darkred', weight='bold')
    
        plt.axhline(y=4, c='black', label='Woman Border',  color='r', linestyle='--', linewidth=3.5)
    
        # Add labels and title
        plt.xlabel('Hot')
        plt.ylabel('Crazy')
        plt.title('Crazy Hot Matrix')
        plt.xlim(0,10)
        plt.ylim(0,10)
        plt.legend(loc=(0.01,-0.31))
        
        # Show the plot
        plt.show()

    # Determine the area where the center is located
    area = "Unknown"
    if center[1] < 4:
        area = "Trany Zone"
    elif center[0] < 5:
        area = "No Go Zone"
    elif center[0] >= 5 and center[0] < 8:
        if center[1] < 0.6 * center[0] + 4:
            area = "Fun Zone"
        else:
            area = "Danger Zone"
    elif center[0] >= 8:
        if center[1] < 5:
            area = "Unicorn Zone"
        elif center[1] < 7:
            area = "Wife Zone"
        elif center[1] < 0.6 * center[0] + 4:
            area = "Girlfriend Zone"
        else:
            area = "Danger Zone"

    # Return the area if return_area is True
    if return_area:
        return area