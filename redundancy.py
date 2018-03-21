import os

# Introduction
print('\nThis program allows two text files full of words to be combined \n' +
        'into one text file while eliminating duplicates. \n\n' +
        'Hit enter to continue')
input()

# Show the current available files in the directory
print('Here are your available files: \n')

txt_file_list = []
print('_' * 50)
for file in os.listdir():
    if file.endswith(".txt"):
        print(os.path.join(file))
        txt_file_list.append(os.path.join(file))
print('_' * 50 +'\n')

first_file_name = (input("Enter file 1's name: ")).strip()
second_file_name = (input("Enter file 2's name: ")).strip()
print()

# Throw up error if names don't match files
if first_file_name not in txt_file_list or second_file_name not in txt_file_list:
    print("File name doesn't match. Be sure to include the extension 'txt'. \n")

# If it matches
else:
    # warning
    print('These two files will be combined and outputted into a file named ' +
    'final_list.txt. \nfinal_list.txt will be overwritten if it already exists. \n')

    proceed = input('Would you like to continue? (y/n) ')
    print()

    if(proceed == 'y'):
        # Fill up the two lists
        first_list = set()
        second_list = set()

        with open(first_file_name) as f:
            for line in f:
                first_list.add(line.lower())

        with open(second_file_name) as f:
            for line in f:
                second_list.add(line.lower())

        # Get rid of duplicates
        final_list = list(first_list | second_list)
        final_list.sort()

        # Write the two lists to the same file while getting rid of duplicates
        with open('final_list.txt', 'w') as f:
            for noun in final_list:
                f.write(str(noun))

        print('final_list.txt successfully created \n')
