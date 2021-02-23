first_class = int(input())
second_class = int(input())
third_class = int(input())

desk_1 = (first_class % 2) + (first_class // 2)
desk_2 = (second_class % 2) + (second_class // 2)
desk_3 = (third_class % 2) + (third_class // 2)

print(desk_1 + desk_2 + desk_3)
