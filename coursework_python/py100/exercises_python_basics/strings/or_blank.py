def is_empty_or_blank(string):
    return string.lstrip() == ''

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
