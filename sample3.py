numbers = [1, 2, 3, 4, 5]
print("Original numbers:", numbers)

new_numbers = input("Enter numbers to add to the list, separated by commas: ")
new_numbers_list = new_numbers.split(",")

for num in new_numbers_list:
    numbers.append(int(num))

print("Updated numbers:", numbers)
