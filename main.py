def nth_most_rate(my_list,n):
    if n in my_list:
        res = min(my_list, key=my_list.count)
        print(res)
    else:
        print("out of bound")
my_list = [5,5,4,3,2,1,5,3,4,4,4,2,1]

nth_most_rate(my_list,2)
