def shut_down(s):
    if s == 'yes':
        return "Shutting down"
    elif s == 'no':
        return "Shutdown aborted"
    else:
        return "Sorry"
        
s = raw_input("Enter 'yes' or 'no':\n")

print shut_down(s)
