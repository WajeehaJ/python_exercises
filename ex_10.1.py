def add_all(n_list):
    """
    function to sum the nested lists.
    """
    sum_nl = 0
    for i in range(len(n_list)):
        for s in n_list[i]:
            sum_nl  +=  s
    return sum_nl



#Creating two different list to
# test the summation of nested lists
n_list = [[1, 2], [2,3]]
n_list2 = [[1, 2], [2,3], [4, 5, 6]]

total = add_all(n_list)
print total

total2 = add_all(n_list2)
print total2


