# text = "telephone book plane car"

text = "сон машина стол книга девочка"
print(text)
print()
text_list = list(text.split(" "))
text_str = sorted(text_list, key=len)
print(" ".join(text_str))

# print(" ".join(map(str, text_str)))