nums = [1, 2, 3, 4, 5, 6, 7] 
print("Sample list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of list numbers:")
print(list(result))