import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("C:\\Users\\yashs\\Downloads\\OnlineRetail.csv")

# Data preprocessing
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
data['Month'] = data['InvoiceDate'].dt.to_period('M')

# Function to find popular items globally, country-wise, and month-wise
def find_popular_items(data):
    global_popular = data.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
    country_popular = data.groupby(['Country', 'Description'])['Quantity'].sum().groupby('Country', group_keys=False).nlargest(1)
    month_popular = data.groupby(['Month', 'Description'])['Quantity'].sum().groupby('Month', group_keys=False).nlargest(1)
    
    global_popular = global_popular.reset_index()
    country_popular = country_popular.reset_index()
    month_popular = month_popular.reset_index()

    return global_popular, country_popular, month_popular

# Function to analyze and print recommendations
def analyze_and_print_recommendations(data):
    global_popular, country_popular, month_popular = find_popular_items(data)
    
    print("Globally Popular Items:")
    print(global_popular[['Description', 'Quantity']])

    print("\nCountry-wise Popular Items:")
    print(country_popular[['Country', 'Description', 'Quantity']])

    print("\nMonth-wise Popular Items:")
    print(month_popular[['Month', 'Description', 'Quantity']])

# Function to predict popular items based on user input and generate bar chart
def predict_popular_items_by_input(data):
    while True:
        country_input = input("Enter the country (or 'exit' to quit): ")
        if country_input.lower() == 'exit':
            break
        month_input = input("Enter the month (format: YYYY-MM): ")
        
        selected_data = data[(data['Country'] == country_input) & (data['Month'] == month_input)]
        if selected_data.empty:
            print("No data found for the given input.")
        else:
            popular_item = selected_data.groupby('Description')['Quantity'].sum().idxmax()
            print("Predicted Popular Item:", popular_item)

            # Generate bar chart for the predicted popular item
            plt.figure(figsize=(8, 6))
            sns.barplot(x='Quantity', y='Description', data=selected_data[selected_data['Description'] == popular_item])
            plt.xlabel('Quantity Sold')
            plt.ylabel('Item Description')
            plt.title(f'Popular Item in {country_input} for {month_input}')

# Generate bar plots for popular items
def generate_bar_plots(data):
    global_popular, _, _ = find_popular_items(data)
    
    plt.figure(figsize=(12, 10))
    ax = sns.barplot(x='Quantity', y='Description', data=global_popular, orient='h')
    plt.xlabel('Quantity Sold')
    plt.ylabel('Item Description')
    plt.title('Globally Popular Items')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right', fontsize=10)

    # Adjust subplot layout for better fit
    plt.tight_layout()

    # Display the plot
    plt.show()

# Main function
if __name__ == "__main__":
    analyze_and_print_recommendations(data)
    generate_bar_plots(data)
    predict_popular_items_by_input(data)
