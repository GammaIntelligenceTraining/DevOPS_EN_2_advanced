# temp_celcius = 100

# print('Strictly under boiling:', temp_celcius < 100)
# print('At or below boiling:', temp_celcius <= 100)
# print('Equal:', temp_celcius == 100)
# print('Not equal:', temp_celcius != 100)

# score = 80
# port = 8080

# print('Chained score range:', 80 <= score < 100)
# print('Port range:', 1024 < port < 65535)

# sum_float = 0.1 + 0.2
# print('Safe float compare:', round(sum_float, 4) == 0.3)

# current_leader = 'Bob'
# print('PEP 8 CHECK:', current_leader == None)
# print('PEP 8 CHECK:', current_leader is not None)
# print(not True)

# print(not 100 > 0)

# print('JACK'.isupper())
# name = 'jack'
# user_input = input("Say your name: ")
# print(name.lower() == user_input.lower())

# warning_count = 0
# high_priority_alert = False
# name = input('Name? ')

# if not name:
#     name = 'stranger'
# print(f"Hello {name}")

# # if name:
# #     print(f'Hello {name}')
# # else:
# #     print("Hello stranger")

# if warning_count > 0:
#     high_priority_alert = True
#     print(f'{warning_count} warnings. Alert triggered.')

# print(f"Alert state: {high_priority_alert}")

age = -80

# if 0 < age < 12:
#     print('Child')
# elif age < 18:
#     print('Teenager')
# elif age < 65:
#     print('Adult')
# elif age < 120:
#     print('Senior')
# else:
#     print('Incorrect age')

# if 0 < age < 120:
#     if age < 12:
#         print('Child')
#     elif age < 18:
#         print('Teenager')
#     elif age < 65:
#         print('Adult')
#     elif age < 120:
#         print('Senior')
# else:
#     print('Incorrect age')

# if 0 < age < 12:
#     print('Child')
# if 12 <= age < 18:
#     print('Teenager')
# if 18 <= age < 65:
#     print('Adult')
# if 65 <= age < 120:
#     print('Senior')
# if 0 > age > 120:
#     print('Incorrect age')

# x = 100

# if x > 5:
#     print("x > 5")
# if x > 20:
#     print("x > 20")
# if x == 100:
#     print("x == 100")

# num = 15

# if num % 3 == 0 and num % 5 == 0:
#     print("FIZZBUZZ")
# elif num % 3 == 0:
#     print("FIZZ")
# elif num % 5 == 0:
#     print("BUZZ")


# server_record = ["db-01.internal", 5432, True, 1.85, [10, [100, 200, 300], 20, 30], None]

# # print(server_record[1])
# # print(len(server_record))
# # print(server_record[4][1][1])
# print(server_record[1:2])

extra_course = "physics"

courses = ["math", "english", "programming", extra_course, "history"]

# print(courses[3])
# courses.append('art')
# # courses.insert(0, 'art')
# print(courses[3])
# print(courses)

# courses.extend(['art', 'estonian'])
# print(courses)
# if "math" in courses:
#     courses.remove("math")
# popped = courses.pop(0)
# print(courses)
# print(popped)

# text = "Hello people of planet Earth. How are you?"
# print(text.split(". "))


# server_string = 'srv-db01-nginx-v10'
# print(server_string.split("-"))

# print([1, 2, 3] + [4, 5, 6])

# *a, b, rest, d = [1, 2, 3, 4, 5]
# print(a, b)
# print(rest)
# print(d)

# x = [3, 4, 5]
# # y = [1, 2, *x, 6]
# # print(y)

# print(*x)

# for num in range(0, 100, 10):
#     print(num ** 2)

# for num1 in range(10):  # 10
#     for num2 in range(10):  # 10 * 10 = 100
#         for num3 in range(10):  # 10 * 10 * 10 = 1000
#             print(num1, num2, num3)

names = ['Jack', 'Bob', 'Sarah']
scores = [76, 65, 80]

student_data = []

# for index in range(len(names)):
#     print(f"{names[index]}: {scores[index]}")

# for index in range(len(names)):
#     student_data.append([names[index], scores[index]])


# for student in student_data:
#     print(student[0], student[1])


# for name, score in student_data:
#     print(name, score)


numbers = [1, 4, 6, 3, 8, 9, 10, 15, 14, 13]

for num in numbers.copy():
    if num % 2 == 1:
        numbers.remove(num)
    print(num)