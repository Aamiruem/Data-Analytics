a, b, c = map(int, input().split())
print(max(a, b, c))



# input () → User types: "10 20 30" (returns a string)
# . split () → Splits "10 20 30" into ["10", "20", "30"] (list of strings)
# map (int, ...) → Converts each string to integer: [10, 20, 30]
# a, b, c = ... → Unpacks the list into three variables:
# a = 10
# b = 20
# c = 30
