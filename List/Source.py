

def cum_sum(li):
    new_li = []
    acc = 0
    for element in li:
        acc += element
        new_li.append(acc)

    return new_li

new_li = cum_sum([1,2,3])
print(new_li)
