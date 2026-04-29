def apply_discount(price , discount):
    if not isinstance (price , (int , float)):
        return "The price should be a number"
        #return
    
    if not isinstance(discount , (int , float)):
        return "The discount should be a number"
        #return

    if price <= 0:
        return 'The price should be greater than 0'
        #return

    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
        #return

    if discount == 100:
        return 0

    return price - (price * discount / 100)
