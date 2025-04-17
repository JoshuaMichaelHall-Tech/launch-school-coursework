my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_counter = 0
while outer_counter < len(my_list): 
    current_list = my_list[outer_counter]
    inner_counter = 0
    while inner_counter < len(current_list):
        if current_list[inner_counter] % 2 == 0:
            print(current_list[inner_counter])

        inner_counter += 1
        
    outer_counter += 1

