
#1.Counting the number of elements using a dict
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

count_dict = {}

for word in words:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

print("1) count words:")
print(count_dict)

#2.Merging two dicts

dict1 = {"a": 10,"b": 20,"c": 30}

dict2 = { "b": 200,"c": 300,"d": 400}

merged_dict = {}

for key, value in dict1.items():
    merged_dict[key] = value

for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] = [merged_dict[key], value]
    else:
        merged_dict[key] = value

print("\n2) merged dict:")
print(merged_dict)

#3. dict reverse

original_dict = {'a': 1,'b': 2,'c': 3}

reversed_dict = {}

for key, value in original_dict.items():
    reversed_dict[value] = key

print("\n3) reversed dict:")
print(reversed_dict)

#4. Operations on sets
films1 = {"Inception", "Interstellar", "Joker", "The Matrix", "Dune", "Oppenheimer"}
films2 = {"Joker", "The Matrix", "Parasite", "Interstellar", "The Shawshank Redemption", "Dune"}
common_films = films1 & films2
only_films1 = films1 - films2
only_films2 = films2 - films1
all_films = films1 | films2
print("\n4) operations on sets:")
print("common films:")
print(common_films)
print("\n only films1:")
print(only_films1)
print("\nonly films2:")
print(only_films2)
print("\n all films:")
print(all_films)


