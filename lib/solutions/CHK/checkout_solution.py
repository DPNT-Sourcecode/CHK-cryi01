

# noinspection PyUnusedLocal
# skus = unicode string
from math import floor
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
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50

    }

    # build dict with special offers (list of tuples in the values)
    special_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
    }

    free_offers = {
        'E': [(2, 'B')],
        'F': [(3, 'F')]
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

    # reverse dict
    item_counts = {v: item_counts[v] for v in sorted(item_counts.keys(), reverse=True)}

    for item, count in item_counts.items():
        # free offers
        if item in free_offers:
            for free_offer in free_offers[item]:
                free_offers_count, free_offers_item = free_offer
                if free_offers_item in item_counts.keys() and item_counts[free_offers_item] > 0:
                    item_counts[free_offers_item] -= abs(floor(item_counts[item] / free_offers_count))
        # special offers
        if item in special_offers:
            for special_offer in special_offers[item]:
                special_offer_count, special_offer_price = special_offer
                while item_counts[item] >= special_offer_count:
                    checkout_total += special_offer_price
                    item_counts[item] -= special_offer_count
        # normal cases
        if item_counts[item] > 0:
            if item in item_prices:
                checkout_total += item_counts[item] * item_prices[item]
            else:
                return -1

    return checkout_total

