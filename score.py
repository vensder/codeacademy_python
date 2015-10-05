

def finish_score(score):
    #order is important!
    tickets = 10 * score
    if score >= 10:
        tickets += 10
    elif score >= 7:
        tickets += 7
    return tickets


score = int(raw_input("input score:\n"))

print finish_score(score)




