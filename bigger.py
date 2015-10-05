

def bigger(first,second):
    print max(first,second)
    return True
    
def string_to_num(num):
    try:
        return int(num)
    except ValueError:
        return float(num)

def answer():
    return 42
        
        
a = raw_input("Input first number:\n")
b = raw_input("Input second number:\n")

a = string_to_num(a)
b = string_to_num(b)

bigger(a,b)

print answer()
