def print_list(products):
    print("Your list of products:")
    for product in products:
        print(product)


def count_products(products):
    print("Number of products in the list:", len(products))


def is_product_on_list(products):
    product_name = input("Enter a product name: ")
    if product_name in products:
        print("Yes, the product is on the list.")
    else:
        print("No, the product is not on the list.")


def count_product_appearances(products):
    product_name = input("Enter a product name: ")
    count = products.count(product_name)
    print("The product appears", count, "times in the list.")


def delete_product(products):
    product_name = input("Enter a product name to delete: ")
    if product_name in products:
        products.remove(product_name)
        print("The product", product_name, "was deleted from the list.")
    else:
        print("Product not found in the list.")


def add_product(products):
    product_name = input("Enter a product name to add: ")
    products.append(product_name)
    print("The product", product_name, "was added to the list.")


def print_illegal_products(products):
    illegal_products = [product for product in products if len(product) < 3 or not product.isalpha()]
    if illegal_products:
        print("Illegal products in the list:")
        for illegal_product in illegal_products:
            print(illegal_product)
    else:
        print("No illegal products in the list.")


def remove_duplicates(products):
    unique_products = list(set(products))
    products.clear()
    products.extend(unique_products)
    print("Duplicates removed from the list.")


def main():
    input_str = input("Enter a comma-separated list of products: ")
    products = input_str.split(',')

    while True:
        print("\nSelect an action:")
        print("1. Print list of products")
        print("2. Count number of products")
        print("3. Check if product is on the list")
        print("4. Count appearances of a product")
        print("5. Delete a product")
        print("6. Add a product")
        print("7. Print illegal products")
        print("8. Remove duplicates")
        print("9. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print_list(products)
        elif choice == 2:
            count_products(products)
        elif choice == 3:
            is_product_on_list(products)
        elif choice == 4:
            count_product_appearances(products)
        elif choice == 5:
            delete_product(products)
        elif choice == 6:
            add_product(products)
        elif choice == 7:
            print_illegal_products(products)
        elif choice == 8:
            remove_duplicates(products)
        elif choice == 9:
            print("Goodbye!")
            break


if __name__ == '__main__':
    main()
