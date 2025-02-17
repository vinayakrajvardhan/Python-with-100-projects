import pandas
import openpyxl

sales_data = pandas.read_excel('input.xlsx')
print(sales_data['Product'])

sales_data['Total'] = sales_data['Price'] * sales_data['Quantity']

sales_data.to_excel('output.xlsx',index=False)


