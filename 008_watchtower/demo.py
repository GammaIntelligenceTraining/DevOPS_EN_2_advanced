import subprocess

res = subprocess.run(["python", "version"])

print(res.returncode)