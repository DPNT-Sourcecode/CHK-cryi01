

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    """
    Method used to calculate the total checkout value based on the products contained in a basket
    
    Args:
        skus (str): a String containing the SKUs of all the products in the basket
    
    Returns:
        int: an Integer representing the total checkout value of the items 
    """
    checkout_total = 0
    
    # parse input string first
    basket_items = skus.split(",")
    print(basket_items)

    for item in basket_items:
        if item.strip()  == "3A" :
            checkout_total += 130
        if item.strip()  == "A":
            checkout_total += 50
        if item.strip()  == "2B":
            checkout_total += 45
        if item.strip()  == "B":
            checkout_total += 30
        if item.strip()  == "C":
            checkout_total += 20
        if item.strip()  == "D":
            checkout_total += 15
    
    print(checkout_total)
    return checkout_total

if __name__ == "__main__":
    checkout("A, B, 3A")







