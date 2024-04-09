# Open a file in write mode ('w')
with open('example.txt', 'w') as f:
    # Write content into the file
    f.write('Hello, this is a sample file!\n')
    f.write('This is another line in the file.\n')

print("File created successfully.")

# You can also use different modes with the open() function depending on your requirements:

# 'r': Open for reading (default).
# 'w': Open for writing, truncating the file first.
# 'x': Open for exclusive creation, failing if the file already exists.
# 'a': Open for writing, appending to the end of the file if it exists.
# 'b': Binary mode.
# 't': Text mode (default).
# '+': Open for updating (reading and writing).