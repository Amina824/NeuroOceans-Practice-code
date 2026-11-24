name = "amina"


name = "A" + name[1:]
print(name)

del name

a = "good"
b = "morning"
print(a + " " + b)
print(a * 3)

text = "python is fun"
print(text.upper())
print(text.lower())
print(text.title())
print(text.count("n"))
print(text.find("is"))
print("   hi   ".strip())
print(text.startswith("py"))

for ch in "amina":
    print(ch)

count = 0
for ch in "programming":
    if ch in "aeiou":
        count += 1
print(count)
