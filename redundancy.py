import os

# Show the current available files in the directory
print()
print('Here are your available files:')
print()
txt_file_list = []

for file in os.listdir("../Redundancy_Duck"):
    if file.endswith(".txt"):
        print(os.path.join(file))
        txt_file_list.append(os.path.join(file))

print()
first_file_name = input("Enter file 1's name: ")
second_file_name = input("Enter file 2's name: ")

print()
if first_file_name not in txt_file_list or second_file_name not in txt_file_list:
    # Throw up error if names don't match files
    print("File name doesn't match. Be sure to include the extension 'txt'.")
else:
    first_list = []
    second_list = []
    with open(first_file_name) as f:
        for line in f:
            first_list.append(line)

    print(first_list)

    with open(second_file_name) as f:
        for line in f:
            second_list.append(line)

    print(second_list)
