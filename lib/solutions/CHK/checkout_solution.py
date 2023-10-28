

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    """
    Desc
    
    Args:
        skus (str): a String containing the SKUs of all the products in the basket
    
    Returns:
        int: an Integer representing the total checkout value of the items 
    """
    checkout_total = 0
    
    #parse input string first

    items = skus.split(,)

    if skus == "A":
        checkout_total += 50
    



