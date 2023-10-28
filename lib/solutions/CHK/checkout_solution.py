

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
        #'E': [(2, 'B')]
    }

    free_offers = {
        'E': [(2, 'B')]
    } 

    checkout_total = 0
    
    # parse input string first
    basket_items = [item for item in skus]

    # count ocurrences of each item
    item_counts = {}
    for item in basket_items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

    for item, count in item_counts.items():
        if item in special_offers:
            for special_offer in special_offers[item]:
                special_offer_count, special_offer_price = special_offer
                while count >= special_offer_count:
                    checkout_total += special_offer_price
                    count -= special_offer_count
        if item in free_offers:
            for free_offer in free_offers[item]:
                free_offers_count, special_offer_free_item = special_offer

        if count > 0:
            if item in item_prices:
                checkout_total += count * item_prices[item]
            else:
                return -1

    print(checkout_total)
    return checkout_total

checkout('EEB')

"""
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
"""





