import unittest
from shopping_cart import Item, ShoppingCart, NotExistError

API_VERSION = 17

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.pan = Item("Pan", 7.0)
        self.jugo = Item("Jugo", 5.0)

        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)
    

    def tearDown(self):
        pass

    def test_cinco(self):
        assert 5 + 5 == 10

    def test_nombre(self):
        self.assertEqual(self.pan.name, "Pan")

    def test_nombre_no_igual(self):
        self.assertNotEqual(self.jugo.name, "Manzana")

    def test_contiene_productos(self):
        self.assertTrue(self.shopping_cart.contains_items())

    def test_no_contiene_productos(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains_items())

    def test_obtener_productoO(self):
        item = self.shopping_cart.get_item(self.pan)
        self.assertIs(item, self.pan)
        self.assertIsNot(item, self.jugo)

    def test_exception(self):
        with self.assertRaises(NotExistError):
            self.shopping_cart.get_item(self.jugo)

    def test_total(self):
        total = self.shopping_cart.total()
        self.assertGreater(total, 0)
        self.assertLess(total, self.pan.price  + 1.0)
        self.assertEqual(total, self.pan.price)

    def test_codigo(self):
        self.assertRegex(self.pan.code(), self.pan.name)

    def test_fail(self):
        if 2 > 3:
            self.fail("Dos no es mayor que tres")

    # @unittest.skip("Motivo de Skip")
    # @unittest.skipIf(API_VERSION < 18, "API Version Obsoleta")
    @unittest.skipUnless(3 > 5 , "Motivos")
    def test_prueba_skip(self):
        pass

if __name__ == '__main__':
    unittest.main()
