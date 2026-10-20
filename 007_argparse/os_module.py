import os

# print(os.getcwd())
# print(os.listdir())

# os.makedirs("test\\test\\test")

# os.removedirs("test\\test")
# os.rename("demo.txt", "example.txt")
# os.rename("example.txt", "python\\data.txt")

# print(os.stat("data.txt").st_size)

# info = os.walk("python")

# for dirpath, dirnames, filenames in info:
#     print('-' * 30)
#     print(f"Current path     : {dirpath}")
#     print(f"Directories      : {dirnames}")
#     print(f"Files            : {filenames}")

# print(os.environ.get("database_password"))

disc = "C:\\"
folder = "temp\\"

file_path = os.path.join(disc, folder, "sample.txt")
print(file_path)

# print(os.path.basename('/somedir/dir2\\sample'))
# print(os.path.dirname('/somedir/dir2\\sample'))
# print(os.path.split('/somedir/dir2/sample.txt'))

os.chdir("../")
print(os.path.exists('temp/data.txt'))

print(os.path.isdir("pythons"))
print(os.path.isfile("data.txt"))


print(os.getcwd())

print(os.path.splitext("data/sample"))