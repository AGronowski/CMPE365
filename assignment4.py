#Adam Gronowski
#Assignment4 for CMPE365
#Finding the differene between two files using dynamic programming


# map string to integer
def f1(s):
    sum = 0
    for c in s:
        sum = (7*sum + ord(c)) % 10000000
    return sum

# check to see if two lines are equal.
# If integer representations are equal then the lines are compared the traditional way
def isEqual(index1,index2):
    if file1_int[index1] == file2_int[index2]:
        return True
    else:
        if file1_words[index1] == file2_words[index2]:
            return True
        else:
            return False

# Create the 2D array for the dynamic programming algorithm
def LCSL(list,i,j):
    #base cases
    if i == 0 and j == 0:
        if isEqual(0,0):
            return 1
        else:
            return 0
    elif i == 0:
        if j > 0 and list[0][j-1] == 1 or isEqual(0,j):
            return 1
        else:
            return 0
    elif j == 0:
        if i > 0 and list[i-1][0] == 1 or isEqual(i,0):
            return 1
        else:
            return 0

    # general case
    else:
        if isEqual(i,j):
            return 1 + list[i-1][j-1]

        else:
            return max(list[i-1][j-1], list[i-1][j], list[i][j-1])

# Print the output
def output(match, first1,last1,first2,last2):
    file1 = filename1
    file2 = filename2

    if match:
        firstString = "Match:"
    else:
        firstString = "Mismatch:"

    if last1-first1 < 0:
        leftString = file1+ " : " + "None"
    else:
        leftString = file1 + " : <" + str(first1) + " .. " + str(last1) + ">"

    if last2-first2 < 0:
        rightString = file2+ " : " + "None"
    else:
        rightString = file2 + " : <" + str(first2) + " .. " + str(last2) + ">"

    print('{:<15s}{:<40s}{:<20s}'.format(firstString, leftString,rightString))
    print("")

# read in first file, store as both list of strings and integer mapping of the strings
file1_words = []
file1_int = []

filename1 = input('Enter name of first file')

with open(filename1) as input_text:
    for line in input_text:
        file1_words.append(line)
        file1_int.append(f1(line))

# read in second file, store as both list of strings and integer mapping of the strings
file2_words = []
file2_int = []

filename2 = input('Enter name of second file')

with open(filename2) as input_text:
    for line in input_text:
        file2_words.append(line)
        file2_int.append(f1(line))

length1 = len(file1_words)
length2 = len(file2_words)

#create the 2d array
list = []

for i in range(length1):
    list.append([LCSL(list,i,0)])

    for j in range(1,length2):
        list[i].append(LCSL(list,i,j))

#reconstruct the LCM
reconstruction1 = []
reconstruction2 = []

i = length1 - 1
j = length2 - 1
while i > 0 or j > 0:
    if isEqual(i,j):
        reconstruction1.append(i)
        reconstruction2.append(j)
        i = i-1
        j = j-1
    else:

        if list[i][j] == list[i-1][j-1]:
            i = i-1
            j = j - 1

        elif list[i][j] == list[i-1][j]:
            i = i -1
        elif list[i][j] == list[i][j-1]:
            j = j - 1

while i> 0:
    if list[i][0] > 0:
        i -= 1
    elif i+1 < length2:
        reconstruction1.append(i+1)
        reconstruction2.append(0)

while j> 0:
    if list[j][0] > 0:
        j -= 1
    elif j+1 < length1:
        reconstruction1.append(0)
        reconstruction2.append(j+1)
if list[0][0] == 1:
    reconstruction1.append(0)
    reconstruction2.append(0)

reconstruction1.reverse()
reconstruction2.reverse()

length = len(reconstruction1)

#add 1 to each line since lines start at 0, not 1
for i in range(length):
    reconstruction1[i] += 1
    reconstruction2[i] += 1

# for i in reconstruction1:
#     print(i)
# print('')
# for j in reconstruction2:
#     print(j)

i = 0

#initial lines are mismatch
if reconstruction1[0] != 1 or reconstruction2[0] != 1:
    output(False,1,reconstruction1[0]-1,1,reconstruction2[0]-1)

#find which lines match and mismatch
while i < length:
    first1 = reconstruction1[i]
    first2 = reconstruction2[i]

    #consequtive lines are a match
    while i < length-1 and reconstruction1[i+1] == reconstruction1[i] + 1 and reconstruction2[i+1] == reconstruction2[i]+1:
        if i < length-1:
            i += 1

    output(True,first1,reconstruction1[i], first2,reconstruction2[i])
    first1 = reconstruction1[i]+1
    first2 = reconstruction2[i]+1

    # not a match
    if i+1 < length:
        second1 = reconstruction1[i+1]-1
        second2 = reconstruction2[i+1]-1
    #final lines
    else:
        second1 = len(file1_words)
        second2 = len(file2_words)

    #make sure final mismatch is not None
    if (second1 >= first1 and second2 >= first2):
        output(False,first1,second1,first2,second2)
    i += 1


