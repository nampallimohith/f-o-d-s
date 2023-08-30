
item_prices = [2.5, 3.0, 1.75, 5.0]  
quantities = [4, 2, 3, 1]  
discount_rate = 10  
tax_rate = 8  
total_cost_before_discounts = sum(price * quantity for price, quantity in zip(item_prices, quantities))

total_discount = (discount_rate / 100) * total_cost_before_discounts
total_cost_after_discounts = total_cost_before_discounts - total_discount
total_tax = (tax_rate / 100) * total_cost_after_discounts
final_total_cost = total_cost_after_discounts + total_tax
print("Total Cost Before Discounts: $", total_cost_before_discounts)
print("Total Discount: $", total_discount)
print("Total Cost After Discounts: $", total_cost_after_discounts)
print("Total Tax: $", total_tax)
print("Final Total Cost: $", final_total_cost)
