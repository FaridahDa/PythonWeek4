read_file = open("pelican.txt").read()
print("type of date is", type(read_file))

pelican_list = []
# 5. Now, write some code that will read the pelican.txt file into a list and then output the number of items within the list.
lines = open("pelican.txt").read().splitlines()
print("the lenths of lines list is: ",len(lines))
# Now use a loop to iterate over and print the contents of the file. Be sure not to include any blank lines in the output.

for i in lines:
    print(i)