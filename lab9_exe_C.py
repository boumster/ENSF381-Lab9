"""
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
Name : lab9_exe_C . py
Assignment : Lab 9 , Exercise C
Author ( s ) : Phoenix Bouma, Victor Gouttin
Submission : Mar 20, 2024
Description : Fetch data by Python .
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""


import requests
import json

def fetch_product_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # The JSON for products key
        return response.json()['products']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def list_all_products (products):
    # Iterate through the products list and print the product name and price
    for product in products:
        print(f"{product['title']} - {product['price']}")

def search_product(products, name):
    # Iterate through the products list and check if the product name exists
    for product in products:
        # if the product name exists, print the product name and price
        if product['title'].lower() == name.lower():
            print(f"{product['title']} - {product['price']}")
            return
    # After it iterate through the entire list, if the item is not found, print the message
    print(f"Product {name} not found")

def main():
    products_url = "https://dummyjson.com/products"
    products = fetch_product_data(products_url)

    if products:
        while True:
            # Display the menu
            print("\n1. List all products")
            print("2. Search product by name")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            # Check the user's choice
            if choice == 1:
                print("\nList of all products")
                list_all_products(products)
            elif choice == 2:
                # Ask the user to enter the product name
                name = input("\nEnter product name: ")
                # Search the product by name
                search_product(products, name)
            elif choice == 3:
                # Exit the program
                break
            else:
                # If the user's choice is invalid, print the message
                print("Invalid choice")

if __name__ == "__main__":
    main()