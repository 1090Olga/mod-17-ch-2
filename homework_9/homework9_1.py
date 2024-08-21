def apply_all_func(int_list, *functions):
    return {function.__name__: function(int_list)
            for function in functions}


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))