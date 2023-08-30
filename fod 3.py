import numpy as np
house_data = np.array([
    [3, 1500, 200000],
    [4, 1800, 250000],
    [5, 2200, 300000],
    [4, 1700, 230000],
    [5, 2100, 280000],
    [3, 1600, 210000],
    [6, 2400, 320000]
])


bedrooms_column = house_data[:, 0]
sale_price_column = house_data[:, 2]


more_than_four_bedrooms_mask = bedrooms_column > 4

sale_prices_more_than_four_bedrooms = sale_price_column[more_than_four_bedrooms_mask]


average_sale_price_more_than_four_bedrooms = np.mean(sale_prices_more_than_four_bedrooms)

print("Average sale price of houses with more than four bedrooms:", average_sale_price_more_than_four_bedrooms)
