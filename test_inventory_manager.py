import unittest
from inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        self.inv_manager = InventoryManager()
        self.inv_manager.add_item(1, "Laptop", "Electronics", 10, 999.99)
        self.inv_manager.add_item(2, "Mouse", "Electronics", 5, 25.50)

    def test_add_item(self):
        self.inv_manager.add_item(3, "Keyboard", "Electronics", 15, 45.00)
        self.assertEqual(len(self.inv_manager.inventory), 3)

    def test_remove_item(self):
        self.inv_manager.remove_item(2)
        self.assertEqual(len(self.inv_manager.inventory), 1)

    def test_update_stock(self):
        self.inv_manager.update_stock(1, 8)
        self.assertEqual(self.inv_manager.inventory.loc[self.inv_manager.inventory['Item_ID'] == 1, 'Stock_Quantity'].values[0], 8)

    def test_generate_low_stock_report(self):
        low_stock = self.inv_manager.generate_low_stock_report(6)
        self.assertEqual(len(low_stock), 1)  # Only the mouse has a stock below 6

if __name__ == '__main__':
    unittest.main()
