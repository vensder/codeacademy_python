def is_numeric(numeric):
    type_n = type(numeric)
    return type_n == int or type_n == float


print is_numeric(1)
print is_numeric('sdf')
print is_numeric(2.3)


def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return type(num)

def string_to_num(num):
    try:
        return int(num)
    except ValueError:
        return float(num)

num = raw_input("enter number:\n")

num = string_to_num(num)

print distance_from_zero(num)
