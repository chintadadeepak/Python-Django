# file handling
# why files?
# during the processing of data, itwill be stored inside 
# the RAM
# but what if we want to store even after the turn-off of CPU
# that'a where files comes into picture for persistent storage

# we have open() to open a file and we need to specify two args
# 1. file path including the extension
# 2. mode --> either read or write mode
# read() will return all the contents of the file
# if you want to read a line then readline() works
# if pass any integer to readline() it will return those many characters
# f = open('code.txt', 'r')
# print(f.read())
# using write(), we can write text on to the file
# if we don't have a file specified in the write(), it will create
# automatically for you
# print(f.readline(5))

# write() will just overwrites the content 
# regardless of the previous content
# if you want to append the data, go with append mode
# nf = open('auto.txt' , 'a')
# nf.write('write over writes the data')
# nf.write('\nnewly appended')

# copying of content using a loop
# loops in files fetches each line at a time
# nf.write('it was created by python')
# print(nf.read())
# same works for image files as well
# but the mode was different
# i.e using binary mode, we can access the files
# for text files, we use charmode
# of = open('code.txt', 'r')
# for line in of:
#     nf.write(line)
# rb --> read binary
# wb --> write binary
pic = open('leetcode.png', 'rb')
clone = open('leetcodeClone.png', 'wb')
for line in pic:
    clone.write(line)