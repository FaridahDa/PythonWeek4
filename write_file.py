our_file = open("pelican.txt", "a")
num = our_file.write("A wonderful bird is the pelican,\n")
num = our_file.write("His bill holds more than his belican.\n")
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I’m damned if I see how the helican.\n"]

# write lines methods
for i in lines:
    num = our_file.write(i)
