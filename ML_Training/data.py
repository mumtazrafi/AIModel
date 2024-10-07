import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Seed for reproducibility
Faker.seed(0)
np.random.seed(0)
random.seed(0)

# Define sample data
genders = ['Male', 'Female', 'Other']
skin_types = ['Oily', 'Dry', 'Combination', 'Sensitive']
skin_concerns_list = ['Acne', 'Wrinkles', 'Dark Spots', 'Dryness', 'Redness', 'Uneven Texture']
categories = ['Cleanser', 'Moisturizer', 'Serum', 'Sunscreen', 'Exfoliator', 'Mask']
brands = ['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE']
ingredients = ['Hyaluronic Acid', 'Salicylic Acid', 'Vitamin C', 'Retinol', 'Niacinamide', 'Glycolic Acid']
benefits = ['Hydration', 'Oil Control', 'Brightening', 'Anti-Aging', 'Exfoliation', 'Soothing']

# Generate Customers Data
num_customers = 1000
customers = []
for i in range(1, num_customers + 1):
    customer = {
        'customer_id': i,
        'age': np.random.randint(18, 65),
        'gender': random.choice(genders),
        'skin_type': random.choice(skin_types),
        'skin_concerns': ', '.join(random.sample(skin_concerns_list, k=random.randint(1,3)))
    }
    customers.append(customer)

customers_df = pd.DataFrame(customers)

# Generate Products Data
num_products = 200
products = []
for i in range(1, num_products + 1):
    product = {
        'product_id': i,
        'product_name': f"{random.choice(['Ultra', 'Hydra', 'Clear', 'Radiant', 'Pure'])} {random.choice(['Glow', 'Fresh', 'Smooth', 'Bright', 'Revive'])} {random.randint(100,999)}",
        'brand': random.choice(brands),
        'category': random.choice(categories),
        'ingredients': ', '.join(random.sample(ingredients, k=random.randint(2,4))),
        'benefits': ', '.join(random.sample(benefits, k=random.randint(1,3))),
        'suitable_skin_types': ', '.join(random.sample(skin_types, k=random.randint(1,4)))
    }
    products.append(product)

products_df = pd.DataFrame(products)

# Generate Interactions Data
interactions = []
interaction_id = 1
for _ in range(5000):  # 5 interactions per customer on average
    customer = random.choice(customers_df['customer_id'].tolist())
    product = random.choice(products_df['product_id'].tolist())
    rating = random.randint(1, 5)
    review = fake.sentence(nb_words=10)
    interaction = {
        'interaction_id': interaction_id,
        'customer_id': customer,
        'product_id': product,
        'rating': rating,
        'review': review
    }
    interactions.append(interaction)
    interaction_id += 1

interactions_df = pd.DataFrame(interactions)

# Save to CSV
customers_df.to_csv('customers.csv', index=False)
products_df.to_csv('products.csv', index=False)
interactions_df.to_csv('interactions.csv', index=False)

print("Synthetic dataset created and saved as CSV files.")
