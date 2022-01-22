num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list:list):
    odd_list = [i for i in num_list if i%2 != 0]
    return odd_list


print(get_odd_num(num_list))