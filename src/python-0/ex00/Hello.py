ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


ft_list.remove("tata!")
ft_list.insert(1, "World!")


# tupple can't be modified, so we create a new one, 
# with the same name, but with the new value
ft_tuple = ("Hello", "United Arab Emirates!")

ft_set.remove("tutu!")
ft_set.add("Abu Dhabi!")

ft_dict.update({"Hello" : "42 Abu Dhabi!"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)