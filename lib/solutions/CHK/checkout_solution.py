

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
    basket_items = [item for item in skus]

    for item in basket_items:
        if item not in ["A", "B", "C", "D"]:
            return -1
        if item.strip()  == "A":
            a_occurence += 1
            checkout_total += 50
            if a_occurence == 3:
                checkout_total -= 150
                checkout_total += 130
                a_occurence = 0
        if item.strip()  == "B":
            b_occurence += 1
            checkout_total += 30
        if item.strip()  == "C":
            c_occurence += 1
            checkout_total += 20
        if item.strip()  == "D":
            d_occurence += 1
            checkout_total += 15

    return checkout_total

