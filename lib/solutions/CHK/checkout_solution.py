

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
    # build dict with baseline price
    item_prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }

    # build dict with special offers (list of tuples in the values)
    special_offers = {
        'A': [(3, 130), (5, 120)],
        'B': [(2, 45)],
        # E: ?
    }

    checkout_total = 0
    a_occurence = 0
    b_occurence = 0
    
    # parse input string first
    basket_items = [item for item in skus]

    # count ocurrences of each item
    item_counts = {}
    for item in basket_items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
    print(item_counts)

    for item in basket_items:
        if item.strip()  == "A":
            a_occurence += 1
            checkout_total += item_prices[item]
            if a_occurence == 3:
                checkout_total -= 150
                checkout_total += 130
                a_occurence = 0
        if item.strip()  == "B":
            b_occurence += 1
            checkout_total += item_prices[item]
            if b_occurence == 2:
                checkout_total -= 60
                checkout_total += 45
                b_occurence = 0
        #if item in special_offers:

        if item in item_prices:
            checkout_total += item_prices[item]
        else:
            return -1

    print(checkout_total)
    return checkout_total

checkout('CD')


