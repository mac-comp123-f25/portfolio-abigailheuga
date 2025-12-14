def remove_all(value, lst):
    while lst.count(value) > 0:
        lst.remove(value)

t_list = [1, 2, 3, 2, 4, 2, 5]
remove_all(2, t_list)
print(t_list)