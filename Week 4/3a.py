def sort_hhh(input_listing):
    list1 = []
    list2 = []

    for words in input_listing:
        if words[0] == "H" or words[0] == "h":
            list1.append(words)
        else:
            list2.append(words)

    return sorted(list1)+sorted(list2)


input_list = ['Bougainvillea', 'Orchids', 'Hibiscus', 'Frangipani', 'Honeysuckle']
print(sort_hhh(input_list))