from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 
            'Portable', 'Improved', 'Loving']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 
        'Guliotine', 'Computer', 'Atomic Bomb']


def generate_products(num_products=30):
    products = []
    # Generating random wacky products suitable for ACME
    for _ in range(num_products):
      product_name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
      products.append(product_name)
    return products

def inventory_report(products):
    i = 0
    name = []
    for k in products:
      name = products[i]
      name = Product(name, price=random.randint(5, 100), weight=random.randint(5,100), 
                     flammability=random.uniform(0, 2.5))
    return name
    

if __name__ == '__main__':
    inventory_report(generate_products())