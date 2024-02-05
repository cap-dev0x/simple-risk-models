import numpy as np
import matplotlib.pyplot as plt

def calculate_standard_deviation(data):
    mean = np.mean(data)
    variance = np.var(data)
    std_deviation = np.sqrt(variance)
    return std_deviation

def plot_data(data):
    plt.hist(data, bins='auto', color='blue', alpha=0.7, rwidth=0.85)
    plt.title('Distribution of Fine Size for Enterpise Data Breaches ')
    plt.xlabel('Cost in Millions')
    plt.ylabel('Frequency')
    plt.show()

# Example data (replace this with your own set of integers)
data = [1190, 887, 575, 403, 370, 350, 277, 255, 200, 190, 148, 120, 102]

std_deviation = calculate_standard_deviation(data)
print(f"Standard Deviation: {std_deviation}")

# Plot the data
plot_data(data)