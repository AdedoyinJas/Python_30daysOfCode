boss = []
def list_taker(test):
    try:
        for i in test:
            if i not in boss:
                boss.append(i)
        return "The list after removing duplicates : " + str(boss)

    except Exception as e:
        print ("You entered the wrong value" , e)

    
    
print(list_taker(3))

