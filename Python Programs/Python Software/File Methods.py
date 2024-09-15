# Append ('a') / Write ('w')

append_info = '\n Inforamtion' # '\n' Adds New Line
appendFile = open('test.txt', 'a')
appendFile.write(append_info)

# Reading ('r')

readMe = open('test.txt', 'r').read()
print(readMe)

# Other Method

readMe = open('test.txt', 'r').readlines() # Turns Text Into List By Properties
print(readMe)
