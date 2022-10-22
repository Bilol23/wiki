# car = 'fer' if True else 'tiko'

##########################################
# a = int(input('Enter first number : ')) 
# b = int(input('Enter second number : ')) 
# c = int(input('Enter third number : ')) 
# largest = 0 
# if a > b and a > c: 
#     largest = a 
# if b > a and b > c: 
#     largest = b 
# if c > a and c > b: 
#     largest = c 
# print(largest, "is the largest of three numbers.")


# a2 = [i**2 for i in range(1,11)]

# a2 = [i for i in range(1,100) if i % 2 == 0]
# print(a2)


# my_pets = ['macentosh', 'acer','lenovo','asus','mac','samsung']
# qq = list(map(lambda x: x*2, my_pets))
# print(qq)

# circe_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.50013]
# print(list(map(round, circe_areas, range(len(circe_areas)))))

# list1 = [3, 5, 4, 8, 6, 33, 22, 18, 76, 1]
# result = list(filter(lambda x: (x%2 != 0) , list1))
# print(result)

# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

# def student(o4ko):
#     return o4ko > 75

# balls = list(filter(student, scores))

# print(balls)


###############################################

# mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']

# def filter_vowels(letter):
#     vowels = ["мак"]
#     return True if letter in vowels else False

# filtered_vowels = filter(filter_vowels, mixed)

# # converting to tuple
# vowels = tuple(filtered_vowels)
# print(vowels)

###################################
string = ("анна", "жанна", "rewire", "madam", "freer", "anutuna", "kiosk")
# joining characters of reversed string one by one
reversed_string = ''.join(reversed(string))
if reversed_string == string:
    print(string," is Palindrome")
else:
    print(string,"Not a Palindrome")
    