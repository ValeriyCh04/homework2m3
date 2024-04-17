def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [12, "hi", True]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
values_list_2 = [1, 'hello']
print_params(*values_list_2, 42)

