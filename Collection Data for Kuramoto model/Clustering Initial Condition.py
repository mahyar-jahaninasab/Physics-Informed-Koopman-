import numpy as np
import h5py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def scale_initial_conditions(N, start, end):
    random_numbers = np.random.rand(N)
    scaled_numbers = start + (end - start) * random_numbers
    return scaled_numbers

all_initial_conditions = []
IC = []
num_clusters = 40
interval_start = 0
interval_end = 2 * np.pi
cluster_width = (interval_end - interval_start) / num_clusters
ss = 2 * np.pi * np.random.rand(16)

for j in range(20):
    cluster_start = 0 
    for i in range(num_clusters): 
        initial_conditions_temp = scale_initial_conditions(N=16, start=cluster_start, end=(cluster_start+cluster_width))
        cluster_start += cluster_width
        all_initial_conditions.append(initial_conditions_temp)

    data_ic = np.stack(all_initial_conditions)
    IC.append(data_ic)
    all_initial_conditions = []
file_name = 'IC.h5'
with h5py.File(file_name, 'w') as f:
    for idx, array in enumerate(IC):
        f.create_dataset(f'array_{idx}', data=array)

file_name = 'IC.h5'

# Read the list of NumPy arrays from HDF5
with h5py.File(file_name, 'r') as f:
    my_list = [np.array(f[f'array_{idx}']) for idx in range(len(f))]

# with h5py.File(file_name, 'r') as f:
#     my_list = [np.array(f[f'array_{idx}']) for idx in range(len(f))]





# Assuming 'angles' is your NumPy array with shape (40, 16)
angles = np.vstack(IC)

# Convert the array to a long-form DataFrame for Seaborn
angles_df = pd.DataFrame(angles, columns=[f' {i+1}' for i in range(16)])
angles_df = angles_df.melt(var_name='Oscillator Number', value_name='Initial Condition (Radian)')

# Define a rainbow color palette for the 16 oscillators
rainbow_palette = sns.color_palette("rainbow", 16)

# Plotting with Seaborn
plt.figure(figsize=(14, 8))

# Set thick black border for the plot
ax = plt.gca()
ax.spines['top'].set_linewidth(2)
ax.spines['top'].set_color('black')
ax.spines['right'].set_linewidth(2)
ax.spines['right'].set_color('black')
ax.spines['bottom'].set_linewidth(2)
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_linewidth(2)
ax.spines['left'].set_color('black')

# Adjusting the font size for labels and numbers
font_size = 14  # Adjust this value as needed
ax.xaxis.label.set_size(font_size)
ax.yaxis.label.set_size(font_size)
ax.tick_params(axis='both', which='major', labelsize=font_size)

# Create box plot with rainbow colors
sns.boxplot(x='Oscillator Number', y='Initial Condition (Radian)', data=angles_df, palette=rainbow_palette)
plt.xlabel('Oscillator Number')
plt.ylabel('Initial Condition (Radian)')
plt.grid(True)

# Save the plot in a high-quality format
plt.savefig('angle_distribution_high_quality.png', dpi=800, bbox_inches='tight')

# Display the plot
plt.show()
