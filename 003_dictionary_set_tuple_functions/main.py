# # valid_dict = {
# #     "port": 80,
# #     "ip": "10.0.0.1"
# # }

# # print(type(valid_dict))

# # int, float, str, tuple
# # test_dict = {
# #     "string": "string_key",
# #     80.2: "numeric key",
# #     ("10.0.0.1", 22): "SSH"
# # }

# # print(test_dict[("10.0.0.1", 22)])

# nested = {
#     "name": "Jack",
#     "surname": "Smith",
#     "info": {
#         "height": 178,
#         "weight": 92,
#         "eye_color": "blue",
#     },
#     "emails": [
#         "jack.smith@example.com",
#         "jack@company.com",
#     ],
# }

# # print(nested["info"]["height"])
# # print(nested["emails"][0])
# # print(nested.get("infs").get("eye_color"))

# # nested['name'] = "Bob"
# # nested['phone'] = '555-555-5555'

# # print(nested)

# # key = "address"
# # nested[key] = "Tartu mnt. 18"

# # nested.update(name="Bob", phone="555-555-5555")
# # nested.update({"name": "Bob", "phone": "555-555-5555"})

# # del nested['name']
# # x = nested.popitem()
# # print(x)

# # print(nested)

# # for element in nested:
# #     print(nested[element])

# # print(nested.keys())
# # print(nested.values())
# # print(nested.items())

# for val in nested.values():
#     print(val)

# for key, val in nested.items():
#     print(f"KEY: {key}\nVALUE: {val}")

# print(dict([["a", 1], ["b", 2]]))

# x = (1, 2, 3, 4, 5)
# # print(x + (1, 2, 3, 4))
# print(id(x))

# x = list(x)
# print(id(x))

# x.append(7)
# x = tuple(x)
# print(id(x))
# # print(type(x))

# x = 1, 2, 3, 4, 5, 6, 7
# print(x)
# print(type(x))

# empty_lst = []
# empty_lst = list()
# lst_one = [2]

# empty_tuple = ()
# empty_tuple = tuple()
# tuple_one = (1,)

# print(type(tuple_one))

# empty_set = set()
# set_one = {1}
# print(type(empty_set))
# print(type(set_one))

# courses_pool = {'math', 'english', 'math', 'physics', 'programming'}
# print(courses_pool)

# set1 = {'math', 'history', 'physics', 'programming'}
# set2 = {'math', 'estonian', 'physics', 'english'}

# print(set1.intersection(set2))

# print(set1.difference(set2))
# print(set2.difference(set1))

# print(set1.symmetric_difference(set2))

# set1.update({'geography', 'french'})
# set1.discard('mechanics')

# print(set1.issuperset({'math', 'physics'}))
# print({'art', 'physics'}.issubset(set1))

# print(set1 | set2)


# def get_status():
#     print("ONLINE")


# print(get_status())

# def get_status():
#     return "ONLINE"

# print(get_status())


# def odd_or_even(number):
#     if number % 2 == 0:
#         return 'EVEN'
#     else:
#         return 'ODD'


# print(odd_or_even(5))
# print(odd_or_even(6))
# print(odd_or_even())

# def say_hello(name, surname):
#     print(f"Hello {name.title()} {surname.title()}")

# # say_hello("JACK", 'smith')

# people = ["Jack Smith", "Bob Green", "Sarah Gold"]

# for person in people:
#     name, surname = person.split()
#     say_hello(name, surname)


# def add_two_or_three(a, b, c=0):
#     print(a + b + c)


# add_two_or_three(2, 5)
# add_two_or_three(4, 5)


# def unlimited(*c, **kwargs):
#     print(kwargs)
#     print(c)


# unlimited(2, 3, 4, 5, 6, 7, 8, "sum", "max", True, None, name="Jack", b=True, surname="Smith")


a, b, c = 1, 2, 3

people = ["jack", "bob", "sarah"]

def inner():
    global c, b
    a, b = 10, 20
    c += 200
    people = ["simon"]
    print("INNER", a, b, c)

inner()
print("OUTER", a, b, c)

print(people)