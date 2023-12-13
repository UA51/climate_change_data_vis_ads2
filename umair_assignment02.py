
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path= 'assignment_data_file.csv'
data = pd.read_csv(file_path)

# Select data for the specific indicators and country
indicators_to_plot = ['Arable land (% of land area)', 'Forest area (% of land area)', 'CO2 emissions (metric tons per capita)']
selected_country = 'United Arab Emirates'

# Filter data
selected_data = data[(data['Country Name'] == selected_country) & (data['Indicator Name'].isin(indicators_to_plot))]

# Extract years and values for the bar chart
years = selected_data.columns[2:]
values1 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[0]].iloc[0, 2:]
values2 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[1]].iloc[0, 2:]
values3 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[2]].iloc[0, 2:]

# Make sure all values arrays have the same length
min_length = min(len(values1), len(values2), len(values3))
values1 = values1[:min_length]
values2 = values2[:min_length]
values3 = values3[:min_length]

# Plot the clustered column chart
plt.figure(figsize=(12, 8))
bar_width = 0.25
bar_positions1 = [pos - bar_width for pos in range(len(years[:min_length]))]
bar_positions2 = [pos for pos in range(len(years[:min_length]))]
bar_positions3 = [pos + bar_width for pos in range(len(years[:min_length]))]

bar1 = plt.bar(bar_positions1, values1, width=bar_width, label=indicators_to_plot[0], color='Green')
bar2 = plt.bar(bar_positions2, values2, width=bar_width, label=indicators_to_plot[1], color='Orange')
bar3 = plt.bar(bar_positions3, values3, width=bar_width, label=indicators_to_plot[2], color='Blue')

plt.title(f'{selected_country} - Climate Indicators (1990-2020)')
plt.xlabel('Year')
plt.ylabel('Values')
plt.xticks(range(len(years[:min_length])), years[:min_length])  # Set the x-axis ticks to represent years
plt.legend()
plt.grid(axis='y')
plt.show()

# Load the dataset
data = pd.read_csv(file_path)

# Select specific indicator for analysis
indicator_to_plot = 'CO2 emissions (metric tons per capita)'
# Select the specific countries for analysis
selected_countries = ['United Arab Emirates', 'Argentina', 'Canada', 'Chile', 'Finland']

# Filter data for selected indicator and countries
selected_data = data[(data['Indicator Name'] == indicator_to_plot) & (data['Country Name'].isin(selected_countries))]

# Create a bar chart
plt.figure(figsize=(12, 8))
bar_width = 0.15

for i, country in enumerate(selected_countries):
    country_data = selected_data[selected_data['Country Name'] == country]
    bar_positions = [pos + i * bar_width for pos in range(len(country_data.columns[2:]))]
    plt.bar(bar_positions, country_data.iloc[:, 2:].values.flatten(), width=bar_width, label=country)

plt.title(f'{indicator_to_plot} Across Countries for All Years')
plt.xlabel('Year')
plt.ylabel('Value')
plt.xticks([pos + 2 * bar_width for pos in range(len(country_data.columns[2:]))], country_data.columns[2:])  # Set the x-axis ticks
plt.legend()
plt.grid(axis='y')
plt.show()
# Load the dataset
file_path = r'assignment_data_file.csv'
data = pd.read_csv(file_path)

# Select specific indicators for analysis
indicators_to_analyze = ['Arable land (% of land area)', 'Forest area (% of land area)', 'CO2 emissions (metric tons per capita)']

# Select the specific country for analysis
selected_country = 'United Arab Emirates'

# Filter data for selected indicators and country
selected_data = data[(data['Indicator Name'].isin(indicators_to_analyze)) & (data['Country Name'] == selected_country)]

# Plot time trends for the selected country and indicators
plt.figure(figsize=(16, 10))
for indicator in indicators_to_analyze:
    indicator_data = selected_data[selected_data['Indicator Name'] == indicator]
    plt.plot(indicator_data.columns[2:], indicator_data.iloc[0, 2:], label=indicator)

plt.xlabel('Year')
plt.ylabel('Value')
plt.title(f'Time Trends for {selected_country} - Selected Indicators')
plt.legend()

# The y-axis limits are determined automatically

plt.show()
# Load the dataset
file_path = r'assignment_data_file.csv'
data = pd.read_csv(file_path)

# Select specific indicators for analysis
indicators_to_analyze = ['Arable land (% of land area)', 'Forest area (% of land area)', 'CO2 emissions (metric tons per capita)']

# Select the specific country for analysis
selected_country = 'Argentina'

# Filter data for selected indicators and country
selected_data = data[(data['Indicator Name'].isin(indicators_to_analyze)) & (data['Country Name'] == selected_country)]

# Plot time trends for the selected country and indicators
plt.figure(figsize=(16, 10))
for indicator in indicators_to_analyze:
    indicator_data = selected_data[selected_data['Indicator Name'] == indicator]
    plt.plot(indicator_data.columns[2:], indicator_data.iloc[0, 2:], label=indicator)

plt.xlabel('Year')
plt.ylabel('Value')
plt.title(f'Time Trends for {selected_country} - Selected Indicators')
plt.legend()

# The y-axis limits are determined automatically

plt.show()
# Load the dataset
file_path = 'assignment_data_file.csv'
data = pd.read_csv(file_path)

# Select specific indicators for correlation matrix
selected_indicators = ['Arable land (% of land area)', 'Forest area (% of land area)', 'CO2 emissions (metric tons per capita)']

# Choose a specific country
selected_country = 'Argentina'

# Filter data for selected indicators and country
selected_data = data[(data['Country Name'] == selected_country) & (data['Indicator Name'].isin(selected_indicators))]

# Extract years dynamically from the columns
years = selected_data.columns[4:]  # Assuming the years start from the 5th column

# Pivot the data
pivot_data = selected_data.melt(id_vars=['Country Name', 'Indicator Name'], value_vars=years, var_name='Year', value_name='Value')
pivot_data['Year'] = pivot_data['Year'].astype(int)  # Convert 'Year' to integer type

# Create a correlation matrix for selected indicators
correlation_matrix = pivot_data.pivot_table(index='Year', columns='Indicator Name', values='Value').corr()

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Draw the heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Set the title
plt.title(f'Correlation Matrix for {selected_country} - Selected Indicators')

# Show the plot
plt.show()

# Load the dataset
file_path = 'assignment_data_file.csv'
data = pd.read_csv(file_path)

# Select specific indicators for correlation matrix
selected_indicators = ['Arable land (% of land area)', 'Forest area (% of land area)', 'CO2 emissions (metric tons per capita)']

# Choose a specific country
selected_country = 'Chile'

# Filter data for selected indicators and country
selected_data = data[(data['Country Name'] == selected_country) & (data['Indicator Name'].isin(selected_indicators))]

# Extract years dynamically from the columns
years = selected_data.columns[4:]  # Assuming the years start from the 5th column

# Pivot the data
pivot_data = selected_data.melt(id_vars=['Country Name', 'Indicator Name'], value_vars=years, var_name='Year', value_name='Value')
pivot_data['Year'] = pivot_data['Year'].astype(int)  # Convert 'Year' to integer type

# Create a correlation matrix for selected indicators
correlation_matrix = pivot_data.pivot_table(index='Year', columns='Indicator Name', values='Value').corr()

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))
# Draw the heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
# Set the title
plt.title(f'Correlation Matrix for {selected_country} - Selected Indicators')

# Show the plot
plt.show()
