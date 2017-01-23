

def nested_sum (nested_list):
    acc = 0
    for element in nested_list:
        acc += sum(element)

    return acc

acc_sum = nested_sum([[1,2],[3],[4,5,6]])
print(acc_sum)
