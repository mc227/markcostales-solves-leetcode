outside_variable = 5


def test_function(x):
    global outside_variable
    outside_variable = 2
    y = x + outside_variable
    return y

print(test_function(1))
print(outside_variable)
