sample_list = ["Red", "Green", "White", "Black", "Pink","Yellow"]

new_list = []

for i in range(len(sample_list)):
    if i != 0 and i != 4 and i != 5:
        new_list.append(sample_list[i])

print(new_list)

 