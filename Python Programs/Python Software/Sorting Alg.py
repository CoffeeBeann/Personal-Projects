def insertion_sort(list):
    for index in range(1,len(list)):
        i = index - 1
        value = list[i]
        while i>=0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i = i - 1
            else:
                break



        
