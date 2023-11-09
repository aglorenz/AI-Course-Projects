def sort_list_by_len(string_list):
    string_list.sort(key=len)
    return string_list

print(sort_list_by_len(["seventeen", "one", "two", "three", "four"]))