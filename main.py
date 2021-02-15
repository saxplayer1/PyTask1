def reverse_min_max(my_list):
    first_max_ind = 0
    mx = my_list[0]
    mn = my_list[0]
    last_min_ind = 0
    for i in range(len(my_list)):
        if my_list[i] > mx:
            mx = my_list[i]
            first_max_ind = i
        if my_list[i] <= mn:
            mn = my_list[i]
            last_min_ind = i
    if first_max_ind < last_min_ind:
        a = first_max_ind
        b = last_min_ind
    else:
        a = last_min_ind
        b = first_max_ind
    for i in range(1, (b - a) // 2):
        t = my_list[a + i]
        my_list[a + i] = my_list[b - i]
        my_list[b - i] = t


if __name__ == '__main__':
    lst = [2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 3, 4, 5]
    print(lst)
    reverse_min_max(lst)
    print(lst)
