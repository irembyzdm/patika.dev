# Question-1
# 1- Write a function that flattens a list. Its elements can consist of multi-layered lists (such as [[3],2]) or non-scalar data. For example:
# sample input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# sample output: [1,'a','cat',2,3,'dog',4,5]

ornek_liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten_list(ornek_liste):
    flattened = []
    for item in ornek_liste:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

output_1 = flatten_list(ornek_liste)
print(output_1)


# Question-2
# 2- Write a function that reverses the elements in the given list. If the elements inside the list also contain the list, reverse their elements as well. For example:
# sample input: [[1, 2], [3, 4], [5, 6, 7]]
# sample output: [[[7, 6, 5], [4, 3], [2, 1]]

ornek_liste_2 = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(ornek_liste_2):
    reversed_list = []
    for item in ornek_liste_2[::-1]:
        if isinstance(item, list):
            reversed_list.append(reverse_list(item))
        else:
            reversed_list.append(item)
    return reversed_list

output_2 = reverse_list(ornek_liste_2)
print(output_2)