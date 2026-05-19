import pandas as pd

# Create sample sales data
data = {
    'Order_Date': ['2024-01-15', '2024-01-20', '2024-02-10', '2024-02-25', '2024-03-05'],
    'Region': ['East', 'West', 'East', 'Central', 'West'],
    'Category': ['Furniture', 'Technology', 'Office Supplies', 'Furniture', 'Technology'],
    'Sales': [1250.50, 2300.00, 450.75, 3100.00, 1890.25],
    'Profit': [350.00, 690.00, 90.00, 930.00, 560.00]
}

df = pd.DataFrame(data)

# Data cleaning & transformation
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.month_name()
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100

print("\n📊 Sales Summary by Region:")
print(df.groupby('Region')['Sales'].sum().round(2))

# Save for Tableau
df.to_csv('cleaned_sales_data.csv', index=False)
print("\n✅ Saved to 'cleaned_sales_data.csv' - Ready for Tableau!")
