import os

# Create a function to work with the specified files
def create_file_list(folder):
    file_list = os.listdir(folder) #Getting a list of file names in a folder
    merget_file_list = [] #Creating a list to store the contents of files
    for file in file_list:
        with open(folder + '/' + file) as _temp_file: # Read the files one by one
            merget_file_list.append([file, 0, []]) # Add the file name, the value for the number of lines, and the list for the file contents to the list
            for line in _temp_file:
                merget_file_list[-1][2].append(line.strip()) #Adding the contents of the file to the list line by line
                merget_file_list[-1][1] += 1 #Increasing the value for the number of rows
    # Return a list with the contents of the files, pre-sorted by the value of the number of lines            
    return sorted(merget_file_list, key=lambda x: x[1], reverse=False)

# Create a function to record the final file
def craete_merget_file(folder, filename):
    with open(filename + '.txt', 'w+') as merget_file: # Open the final file named "filename".txt
        merget_file.write(f'Даны файлы:\n')
        for file in create_file_list(folder):
            merget_file.write(f'Название файла: {file[0]}\n') # Write the names of the initial files to the final file
            merget_file.write(f'Количество строк: {file[1]}\n') # Write the number of lines of the initial files to the final file
            for string in file[2]:
                merget_file.write(string + '\n') # Write the contents of the initial files line by line to the final file
            merget_file.write('\n')
    return print('Файл создан')

craete_merget_file('txt', 'merget_file')