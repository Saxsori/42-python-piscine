ft_dict = {
    "list" : "List", 
    "tuple" : "Tuple", 
    "set" : "Set", 
    "dict" : "Dict", 
}

def all_thing_is_obj(object: any) -> int:
    ft_type = type(object)
    if (type(object).__name__ in ft_dict):
        print(ft_dict[type(object).__name__] + " : {}".format(ft_type))
    else:
        if (type(object).__name__ == "str"):
            print(object + " is in the kitchen : {}".format(ft_type))
        else:
            print("Type not found")
    return 42