products = {"laptop": 3, "phone":0, "tablet": 5, "mouse": 0 , "keyboard": 2}



def available_products(products:dict()):
    for value in products.values():
        if value > 0 :
            yield value
            
zarf = available_products(products)
print(next(zarf))

print(next(zarf))

print(next(zarf))

        
    