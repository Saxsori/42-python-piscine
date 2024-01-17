import math

ft_dict = {
    None : "Nothing", 
    math.nan : "Cheese", 
    0 : "Set", 
    "" : "Empty",  
    False : "Fake", 
}

def NULL_not_found(object: any) -> int:
    if type(object) == float and math.isnan(object):
        object = math.nan
    if (object in ft_dict):
        print(ft_dict[object] + ": " + str(object) + " " + str(type(object)))
    else:
        print("Type not found")
    return 1