friuts = ["apple" , "banana" , "cherry" ]

friuts.add("orange")
print(friuts)

friuts.remove("banana")
print(friuts)

friuts.remove("banana")
print(friuts)

friuts.discard("grape")
print(friuts)

remove_item = friuts.pop()
print(remove_item)
print(friuts)

friuts.clear()
print(friuts)