import re

log = "Failed login for admin from 10.0.0.5 at 04:34. Error 403."

# r"" - is a raw string, python will ignore formating


# match = re.search(r"\d{3}", log)
# print(match.group())

# numbers = re.findall(r"\d+", log)
# print(numbers)

# ip_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
# matches = ip_pattern.findall(log)
# test = re.compile(r"\w ")
# matches = test.findall(log)

# sentence = "start here and end here"

# pattern = r"^start \w+$"
# matches = re.findall(pattern, sentence)

# pattern = r"ha\b"
# matches = re.finditer(pattern, "ha haha hahaha.")

# for match in matches:
#     print(match)

# color_string = "Hex value for red is #ff0000, #HH99LL, #GGFFFF, #GGUUKK"

# matches = re.findall(r"#[^0-9A-Fa-f]{6}", color_string)
# print(matches)

# # . ^ $ * + ? { } [ ] \ | ( )  -> MUST BE ESCAPED
# text = "The IP is [192.168.1.1]. Did it fail? (Yes/No)"

# print("Found bracket:", re.search(r"\[192", text))
# print("Found question mark:", re.search(r"\?", text))
# print("Found parenthes:", re.search(r"\(Yes/No\)", text))

# contact_string = "Please reach me to devops-team@company.com for support."

# email_pattern = r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+"
# emails = re.findall(email_pattern, contact_string)
# print(emails)

# log = "Failed login for admin from 10.0.0.5 at 04:34. Error 403. login admin"
# # # pattern = r"([01]\d|2[0-3]):([0-5]\d)"
# pattern = r"LOGIN(?= for)"

# matches = re.finditer(pattern, log, re.I)
# print(matches)
# print(type(matches))

import sys

# print(f"Platform: {sys.platform}")
# print(f"Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

# if sys.version_info < (3, 15):
#     sys.exit("CRITICAL: Python 3.10 or higher")

# print("GOOD BYE")

# print(f"Python: {sys.executable}")

# is_venv = sys.prefix != sys.base_prefix
# if not is_venv:
#     sys.stderr.write("[WARNING] Venv is not activated")

# large_data = [x for x in range(1000000)]
# print(f"List memory size: {sys.getsizeof(large_data) / 1024 /1024} mb")
# # print(large_data)

# generator_data = (x for x in range(1000000))
# print(f"Generator memory size: {sys.getsizeof(generator_data) / 1024 /1024} mb")

# for num in generator_data:
#     print(num)

# import time

# print(f"Script Name: {sys.argv[0]}")
# print(f"CLI arguments: {sys.argv[1:]}")

# sys.stdout.write("PAYLOAD")
# time.sleep(2)
# sys.stdout.flush()
# sys.stdout.write("WORKING")
# time.sleep(2)
# sys.stdout.flush()

data = [
    {
        "make": "Audi",
        "model": "A6",
        "color": "red",
        "mileage": 10000
    },
    {
        "make": "BMW",
        "model": "540i",
        "color": "black",
        "mileage": 25000
    },
    {
        "make": "VW",
        "model": "Passat",
        "color": "green",
        "mileage": 40000
    },
]

# def filter_red(car):
#     return car["color"] == "red"

filtered = filter(lambda car: car["color"] == "red", data)
for x in filtered:
    print(x)

mapped = map(lambda car: f"{car["make"]} {car["model"]} is {car["color"]}", data)

for x in mapped:
    print(x)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mapped = map(lambda num: {"num": num, "square": num ** 2, "cube": num ** 3}, nums)
for num in mapped:
    print(num)
