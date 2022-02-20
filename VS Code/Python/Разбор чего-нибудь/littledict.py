from collections import defaultdict

example_dict = {}
example_dict["возраст"] = [10]
example_dict["возраст"].append(15)


print(example_dict)



from collections import defaultdict
d = defaultdict(list)
d["a"].append(1)
d["b"].append(2)
d["c"].append(3)
d["c"].append(10)

print(d)