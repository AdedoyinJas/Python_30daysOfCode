def mode(my_list):
    try:
        d_list = set(my_list)
        appearance = {a: my_list.count(a) for a in d_list}
        max_appearance = max(appearance.values())
        for key in appearance:
            if appearance[key] == max_appearance:
                return key
    
    except:
        return "You've entered a string"
          
print(mode([5,5,4,4,5,6]))