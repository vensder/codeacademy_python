def fruit_color(fruit):
    if fruit == 'apple':
        return 'red'
    elif fruit == 'banana':
        return 'yellow'
    elif fruit == 'pear':
        return 'green'
    elif fruit == 'orange' or fruit == 'lemon':
        return fruit
    else:
        return "unknown"
        

fruit = raw_input ("Input fruit name:\n")

print fruit + " has " + fruit_color(fruit) + " color."


