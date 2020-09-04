from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS
import unittest

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""

        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_product_weight(self):
        'Testing the default weight is set to 10'

        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.flammability, 0.5)

    def test_steal_explode(self):
        'Testing the stealability and explosion of a product'

        prod1 = Product('boom boom', weight=1000)
        self.assertEqual(prod1.explode(), 'BABOOM!!!!!!!!')
        self.assertEqual(prod1.stealability, '{} is easily stealable'
                        .format(prod1.name))

class AcmeReportTests(unittest.TestCase):
    'Testing to see if our reports do what is expected!'
    
    def test_default_num_products(self):
        'testing to make sure num products is 30 by default'

        omar = generate_products()
        self.assertEqual(len(omar), 30)
    
    def test_legal_names(self):
        'testing to make sure names are perfect'

        omar = generate_products()
        self.assertIn(ADJECTIVES, NOUNS)

    