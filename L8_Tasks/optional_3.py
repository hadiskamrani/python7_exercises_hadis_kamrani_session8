def create_profile(name,age,**kwargs):
    esm = name
    sen = age
    
    print(esm)
    print(sen)
    print(**kwargs)
    print(len(**kwargs))
    dictionary = {**kwargs, "name":esm, "age": sen}
    print(dictionary)
    
    if "city" in dictionary:
        print(dictionary["city"])
            
    if "email" not in dictionary:
        print("email not provided")
        
    return dictionary
   
        
    
    