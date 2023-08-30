import pandas as pd

data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['A', 'B', 'A', 'C', 'B'],
    'number_of_bedrooms': [3, 4, 5, 3, 4],
      'area_in_square_feet': [1500, 2000, 2500, 1800, 2200],
    'listing_price': [250000, 320000, 420000, 280000, 350000]
}
property_data = pd.DataFrame(data)
average_price_by_location = property_data.groupby('location')['listing_price'].mean()
print("Average Listing Price by Location:\n", average_price_by_location)
num_properties_more_than_four_bedrooms = property_data[property_data['number_of_bedrooms'] > 4].shape[0]
print("Number of Properties with More than Four Bedrooms:", num_properties_more_than_four_bedrooms)
property_with_largest_area = property_data[property_data['area_in_square_feet'] == property_data['area_in_square_feet'].max()]
print("Property with Largest Area:\n", property_with_largest_area)
