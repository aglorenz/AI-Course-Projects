def largest_number(number_list):
    largest = number_list[0] # initialize
    for num in number_list:
        if num > largest:
            largest = num
    return largest       

print(largest_number([1, 3, 15, 20]) )

x = max([1, 3, 15, 20])  # faster way
