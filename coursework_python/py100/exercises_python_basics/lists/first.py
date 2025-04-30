def first(my_list):
    if not my_list:
        return ''
    else:
        return my_list[0]

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))
