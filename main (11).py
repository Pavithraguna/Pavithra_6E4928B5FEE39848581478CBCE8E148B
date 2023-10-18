def linear_search_product(product_list, target_product):
    indices = []

    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)

    return indices

# Example usage:
products = ["Apple", "Banana", "Apple", "Orange", "Apple"]
target_product = "Apple"
result = linear_search_product(products, target_product)
print("Indices of", target_product, "are:", result)
