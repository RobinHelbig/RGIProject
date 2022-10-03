import os
directory = 'BBC News Summary'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    print(filename)
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)