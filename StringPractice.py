"""s = input("input Python source code name :")
if s.endswith(".py"):
    print("Good")
else:
    print("Bad") """

s = "www.naver.com"
print(s.replace("com", "co.kr"))

s = "www.naver.co.kr"
print(s.find(".kr"))

s = "Let it be, let it be, let it be"
print(s.rfind("let"))

s = "www.naver.co.kr"
print(s.count("."))

s = " Hello, World! "
print(s.strip())

s = "######this is example######"
print(s.strip("#"))

s = "######this is example######"
print(s.lstrip("#"))
print(s.rstrip("#"))

s = "Welcome to python"
print(s.split())

s = "Hello, World!"
print(s.split(","))

email = "kskslr@naver.com"
print(email.split("@"))

print(",".join(["apple", "banana", "cherry"]))
print("-".join("010.2326.5569".split(".")))

address = input("Enter your address: ")
id, domain = address.split("@")

print("ID: ", id)
print("Domain: ", domain)


sentence = input("input String:")
table = {"alpha":0, "digit":0, "space":0}

for i in sentence:
    if i.isalpha():
        table["alpha"] += 1
    elif i.isdigit():
        table["digit"] += 1
    elif i.isspace():
        table["space"] += 1

print(table)