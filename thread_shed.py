daily_sales_new = daily_sales.replace(';,;', '+')

transactions = daily_sales_new.split(',')

detailed_trans = []
for entry in transactions:
  detailed_trans.append(entry.split('+'))

transactions_clean = []
for lst in detailed_trans:
  transaction_clean = []
  for item in lst:
    transaction_clean.append(item.replace("\n", "").strip(" "))
  transactions_clean.append(transaction_clean)
print(transactions_clean)

customers = []
sales = []
thread_sold = []

for lst in transactions_clean:
  customers.append(lst[0])
  sales.append(lst[1])
  thread_sold.append(lst[2])

print(customers, sales, thread_sold)
