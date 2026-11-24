s = "i am learning python"
words = s.split()
print(words)

data = "apple,banana,mango"
print(data.split(","))

print(" ".join(words))
print("-".join(words))

t = "i like cats, cats are cute"
print(t.replace("cats", "dogs"))
print(t.replace("cats", "dogs", 1))

email = "amina@gmail.com"
user, domain = email.split("@")
print(user)
print(domain)
