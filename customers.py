

print("---Excerise 1 ---")

customer = {
    "name": "Alice",
    "Name": "Not-Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
    "address": {
        "street": "123 Main St,"
    }
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])


print("--- Excerise 2 ---")
customer['phone'] = '555-555'
print(customer)
customer["tier"]  = "platinum"
print(customer)
del customer["Name"]
print(customer)

print(customer.get("ytd_spend", 0))


print("--- Excerise 3 ---")

print(customer.get("email", "no email on file"))

print("--- Excerise 4 ---")


for key  in customer:
  print(key, ":", customer[key])

for something in customer:
  print(something, ":", customer[something])

print("--- Excerise 5 ---")

tier_discounts = {"bronze": 0,
                   "silver": 0.05,
                   "gold": 0.1,
                   "platinum": 0.15
                   }

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1- discount_rate)
print(f"Tier: {customer["tier"]}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")


print("--- Excerise 6 ---")

customers = [
  {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
  {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
  {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
  rate = tier_discounts.get(record["tier"], 0)
  discount = 300 * rate
  print(f"{record["name"]} ({record["tier"]}): ${discount:.2f}")

print("--- Excerise 7 ---")
catalog = {
  "widget A": {"price": 9.99, "stock":150},
  "Gadget C": {"price": 49.99, "stock": 8},
}
for product_name, product_details in catalog.items():
  if product_details["stock"] < 20:
    print(f"LOW STOCK: {product_name}- only {product_details['stock']} left")

# --- Excerise 8 ---
print("--- Excerise 8 ---")
transactions = [
  {"region": "South", "amount": 300},
  {"region": "North", "amount": 150},
  {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
  region = sale["region"]
  amount = sale["amount"]
  sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

#Reflection

# --- 1 ---

# I would use .get when I'm not sure if a key exists in a dictionary because
# it allows me to set a default value. I would use the bracket when I know a key exist. 
#The rule of thumb whould to .get for optional info while using brackets for known.

# --- 2 ---

# It kind of reminds me of PivotTables in Excel because both can organize 
# data into categories and calculate totals. However, Python is more useful for larger datasets because it proccess
#larger amount of infor automattically.