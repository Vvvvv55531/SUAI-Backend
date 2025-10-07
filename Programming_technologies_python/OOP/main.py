from fridge_and_freezer import Products, Fridge, Freezer
from scales import Product, Scales

if __name__ == '__main__':

    print("------Fridge------")
    fridge: Fridge = Fridge(3.0)
    fridge.add_product(Products("apple", 20.3, -20.3))
    fridge.add_product(Products("orange", -20.3, -21.3))
    fridge.add_product(Products("juice", 30.0, -21.3))
    fridge.storage_states()

    fridge.del_product(Products("juice", 30.0, -21.3))
    fridge.storage_states()

    fridge.storage_fullness()
    fridge.search_product("apple")

    print("\n------Freezer------")
    freezer: Freezer = Freezer(-21.0)
    freezer.add_product(Products("apple", 20.3, -21.3))
    freezer.add_product(Products("orange", -20.3, -21.3))
    freezer.add_product(Products("juice", 30.0, -21.3))
    freezer.storage_states()

    freezer.del_product(Products("juice", 30.0, -21.3))
    freezer.storage_states()

    freezer.storage_fullness()
    freezer.search_product("apple")

    print("\n------Scales------")
    scales: Scales = Scales(25.0)
    scales.add_product(Product("apple", "food", 19000.0, 19.0))
    scales.add_product(Product("orange", "food", 1000.0, 6.0))
    scales.add_product(Product("juice", "food", 1000.0, 1.0))
    scales.storage_states()
    scales.current_weight()

    scales.sort_by_cost()
    scales.storage_states()

    scales.sort_by_weight()
    scales.storage_states()

    scales.min_cost()
    scales.max_weight()
    scales.weight_of_type("food")

    scales.del_product(Product("orange", "food", 1000.0, 6.0))
    scales.storage_states()
    scales.current_weight()
