import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

sales_by_person_year = df.groupby(['Sales_Rep_Name', 'Year'])["Value"].sum().reset_index()

sales_by_person_year.columns = ['Sales_Rep_Name', 'Year', 'Total_Sales']

print("Total Sales by each Person per year:")
print(sales_by_person_year)

# sales_by_person_year.plot(kind='bar',  title = "Total Sales by each Person")
# plt.ylabel("Total Sales")
# plt.show()
