# # memory_limit = "800MB"
# # # ValueError

# # try:
# #     mem_int = int(memory_limit)
# # except ValueError as err:
# #     print("Couldn't convert!", err)
# #     mem_int = 512
# # else:
# #     print(mem_int)
# # finally:
# #     print("Good bye!")

# def parse_config(config):
#     try:
#         val = int(config['timeout'])
#         if val > 60:
#             raise Exception
#         print(f"Timeout: {val}")
#     except KeyError:
#         print("Missing timeout key! Using 30.")
#     except ValueError:
#         print("Timeout is not a number! Using 30.")
#     except Exception:
#         print(f"Timeout {val}s is too high. Max 60s. Using 30.")


# parse_config({"host": "web01"})
# parse_config({"timeout": "five seconds"})
# parse_config({"timeout": "15"})
# parse_config({"timeout": "200"})

# f = open("demo.txt", "w")
# print(f.closed)
# while True:
#     pass

# W - write
# A - append
# X - create
# R - read

# with open("demo.txt", "x") as file:
#     file.write("Hello world\n")
#     file.write("Hello planet\n")

# with open("../demo.txt", "w") as file:
#     # for line in file:
#     #     print(line)
#     file.write("OUTSIDE DIRECTORY")

# with open("demo.txt", "r") as file:
#     data = file.read(10)
#     print("1", data)
#     data2 = file.read()
#     print("2", data2)
#     file.seek(0)
#     data3 = file.read()
#     print("3", data3)

# import json

# api_response = '{"status": 200, "host": "web01", "is_authenticated": false}'
# data = json.loads(api_response)
# data["status"] = 404
# with open("api.json", "w") as file:
#     json.dump(data, file, indent=4)

# with open("api.json", "r") as file:
#     data = json.load(file)
# print(data)
# # False = false
# # True = true
# # None = null

# attempts = 5
# while attempts > 0:
#     print("connecting...")
#     print("failed...")
#     attempts -= 1
condition = True
while condition:
    id_code = input("Enter your national id: ")
    if id_code.lower() == 'exit':
        print('Good bye')
        condition = False
    if len(id_code) != 11:
        print("Wrong code! Must be 11 digits long! Try again")
    else:
        while True:
            user_choice = input("1. Tell the gender\n2.Date of birth\n3.Exit\n-")
            if user_choice == "1":
                if int(id_code[0]) % 2 == 0:
                    print("Female")
                else:
                    print("Male")
            elif user_choice == "2":
                print(f"{id_code[5:7]}.{id_code[3:5]}.{id_code[1:3]}")
            elif user_choice == "3":
                condition = False
                break

# while True:
#     user_choice = input("1.Say hello\n2.Repeat\n3.Exit")
#     if user_choice == "1":
#         print("Hello")
#     elif user_choice == "2":
#         continue
#     elif user_choice == "3":
#         break
#     else:
#         print("Wrong choice!")
#     print("END OF WHILE BODY")

# print("POST WHILE MESSAGE")
