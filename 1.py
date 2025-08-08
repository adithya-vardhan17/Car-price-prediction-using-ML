import matplotlib.pyplot as plt
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
average_prices = [15000, 14500, 14000, 13800, 13500, 13000, 12800]
plt.figure(figsize=(10, 6))
plt.plot(years, average_prices, marker='o', linestyle='-', linewidth=2)
plt.title('Average Car Price Over Years')
plt.xlabel('Year')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.show()
