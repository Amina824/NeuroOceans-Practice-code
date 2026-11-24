colors = ["red", "green"]

colors.append("blue")
print(colors)

colors.extend(["yellow", "black"])
print(colors)

colors.insert(1, "white")
print(colors)

nums = [1, 2, 3, 4, 5]
nums[0] = 100
print(nums)

nums[1:3] = [20, 30]
print(nums)
