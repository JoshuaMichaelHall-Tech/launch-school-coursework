def starts_with(string, start):
    return string[0:len(start)] == start

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True
