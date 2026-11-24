nums = [5, 2, 8, 1, 9, 3]

print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(nums.count(8))
print(nums.index(9))

print(sorted(nums))
nums.sort()
print(nums)
nums.reverse()
print(nums)

a = [1, 2, 3]
b = [4, 5]
print(a + b)
print(a * 2)
print(3 in a)

for n in nums:
    print(n)

for i in range(len(nums)):
    print(i, nums[i])

squares = [n * n for n in range(1, 6)]
print(squares)
