import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##### Load the dataset
data = pd.read_csv('data.csv')

##### Convert 'Invoice Date' to datetime
data['Invoice Date'] = pd.to_datetime(data['Invoice Date'])

##### Overall sales trends over time
plt.figure(figsize=(12, 6))
monthly_sales = data.groupby(data['Invoice Date'].dt.to_period('M'))['Total Sales'].sum()
monthly_sales.plot(kind='line', marker='o')
plt.title('Total Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

##### Top-performing products by total sales
plt.figure(figsize=(12, 6))
product_sales = data.groupby('Product')['Total Sales'].sum().sort_values(ascending=False)
product_sales.plot(kind='bar')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

##### Revenue contribution by region
plt.figure(figsize=(12, 6))
region_sales = data.groupby('Region')['Total Sales'].sum()
region_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140, legend=False)
plt.title('Revenue Contribution by Region')
plt.ylabel('')
plt.tight_layout()
plt.show()

##### Sales method impact
plt.figure(figsize=(12, 6))
sales_method = data.groupby('Sales Method')['Total Sales'].sum().sort_values(ascending=False)
sales_method.plot(kind='bar')
plt.title('Total Sales by Sales Method')
plt.xlabel('Sales Method')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

