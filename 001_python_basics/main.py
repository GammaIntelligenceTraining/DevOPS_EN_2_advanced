port_str = "8080"
ratio_str = "0.85"

# STRINGS | str()
# INTEGER | int()
# FLOAT | float()
# BOOLEAN | bool()
# NoneType | None

# print(type(ratio_str))
# print(str(21313) + 'hello')
# print(int(port_str))
# print(int(float(ratio_str)))

# FALSE VALUES
# STRING -> ''
# INTEGER -> 0
# FLOAT -> 0.0
# \, ', "

# name = "Jack"
# surname = "Smith"
# age = 20

# greeting = f"I am {name.upper()} {surname.lower()}.\n\tI am {age + 200} years old."
# print(greeting)

# host = "srv-prd-db-02"
    #   0123456789.....
    #      -5-4-3-2-1

# [START:END:STEP]

# print(len(host))
# print(host[-1])
# print(host[0:3])

# print('db-03' in host)

# host = ' **  drv-mdf-db-02 *    '
# host = host.strip(' *')
# print('jACK SMITH'.title())

# a, b = 100, 200

# a = 10
# b = 20.0

# print(a + a + a + 2000 + b)
# print(a - b + 2 - 10)
# print((a + b) * 10)

# print(b / 3)
# print(b // 3)  # int()
# print(10 % 3)  # 3 + 3 + 3 + 1

# print(10 ** 2)
# print((20 * 2) ** 5)
# print(144 ** 0.5)

total_bytes = 34359742654
bytes_in_gb = 1024 ** 3
print(f"{total_bytes / bytes_in_gb:.0f}")

free_ram = 8.0
pod_ram = 2.5
deployable = int(free_ram // pod_ram)
headroom = free_ram % pod_ram
print(deployable)
print(headroom)

free_ram %= pod_ram