
def day_to_be_out(depth):
    height = 0
    days = 0
    while True:
        height +=8
        days += 1
        if depth <= height: 
            break
        else:
            height -=3
    return days

print(day_to_be_out(17))
    