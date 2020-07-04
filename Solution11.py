file_name = 'README.txt'
print(f'The sample file name is: {file_name}')
print(f'The extension of file is: {file_name[-4:]}') # slicing the extension of file assuming that the extension of file has 3 letter.
new_filename = file_name[:len(file_name)-4] # slicing the filename excluding its extension.
print(f'The name of the file without extension: {new_filename}')