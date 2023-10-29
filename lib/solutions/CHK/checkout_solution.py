

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
        'K': 70,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 20,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 17,
        'Y': 20,
        'Z': 21

    }

    # build dict with special offers (list of tuples in the values)
    special_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)],
    }

    free_offers = {
        'E': [(2, 'B')],
        'F': [(3, 'F')],
        'N': [(3, 'M')],
        'R': [(3, 'Q')],
        'U': [(4, 'U')],
    }

    group_discount_offers = {
        'E': [(2, 'B')],
    }

    group_discount_offers_list = ['S','T','X','Y','Z']


    checkout_total = 0
    n_discount_offers_count = 0
    
    # parse input string first
    basket_items = [item for item in skus]

    # count ocurrences of each item
    item_counts = {}
    for item in basket_items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

    found_discount_offers_items = {
        'S':0,
        'T':0,
        'X':0,
        'Y':0,
        'Z':0
    }

    # reverse dict
    item_counts = {v: item_counts[v] for v in sorted(item_counts.keys(), reverse=True)}
    filtered_total = 0

    # group discount offers
    for discount_item in group_discount_offers_list:
        if discount_item in item_counts:
            print(item_counts[discount_item])

    # if item in group_discount_offers_list:
    #     found_discount_offers_items[item] += 1 * item_counts[item]
    #     if sum(found_discount_offers_items.values()) == 3:
    #         filtered_item_counts = {key: value for key, value in found_discount_offers_items.items() if value > 0}
    #         for key, value in filtered_item_counts.items():   
    #             filtered_total += value * item_prices[key]
    #             item_counts[key] -= value
    #             found_discount_offers_items[key] -= 1
    #         #print(filtered_item_counts)
    #         checkout_total -= filtered_total - item_prices[item]
    #         checkout_total += 45
    #     #found_discount_offers_items[item] -= 1    

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
    print(checkout_total)
    return checkout_total

checkout('STX')


