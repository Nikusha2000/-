#1

full_name = 'ada lovelance'
name_parts = full_name.split()

first_initial = name_parts[0][0]
last_initial = name_parts[1][0]

print(f"Your initials are: a. l.' {first_initial.upper()}. {last_initial.upper()}.")


#2
word = 'python'
reversed_word = word[::-1]
print("the reversed word is:", reversed_word)


#3
sentence = input("put the sentence: ")
word_to_replace = input("i want to replace: ")
new_word = input("with what?: ")

updated_sentence = sentence.replace(word_to_replace, new_word)
print(updated_sentence)


