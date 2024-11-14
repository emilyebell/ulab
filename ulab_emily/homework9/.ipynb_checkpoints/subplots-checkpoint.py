

import matplotlib.pyplot as plt
import numpy as np

# Function to plot subplots side-by-side (horizontal)
def plot_horizontal_subplots(x):
    
    h_x = np.cos(x) # calculate h(x) = cosx
    k_x = np.sin(x) # calculate k(x) = sinx
    
    # figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 8))
    
    # left subplot
    ax1.plot(x, h_x, color='blue')
    ax1.set_title("h(x) = cos(x)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("h(x)")
    
    # right subplot
    ax2.plot(x, k_x, color='red')
    ax2.set_title("k(x) = sin(x)")
    ax2.set_xlabel("x")
    ax2.set_ylabel("k(x)")
    
    # show plot
    plt.tight_layout()
    plt.show()


def plot_vertical_subplots(x):
    # Function to plot subplots on top of each other (vertical)
    
    h_x = np.cos(x) # calculate h(x) = cosx
    k_x = np.sin(x) # calculate k(x) = sinx
    
    # figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # top subplot
    ax1.plot(x, h_x, color='blue')
    ax1.set_title("h(x) = cos(x)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("h(x)")
    
    # bottom subplot
    ax2.plot(x, k_x, color='red')
    ax2.set_title("k(x) = sin(x)")
    ax2.set_xlabel("x")
    ax2.set_ylabel("k(x)")
    
    # show plot
    plt.tight_layout()
    plt.show()
