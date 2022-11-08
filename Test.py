list1 = [[1,2],[3,3],[5,7]]
list2 = [[1,2],[3,3],[5,5],[1,2],[4,66]]
i=0

for i in list1:
     while i in list2:
        list2.remove(i)



print(list2)
