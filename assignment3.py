#Adam Gronowski
#20051808
#Assignment 3 for CMPE365
#Huffman Encoding and Decoding for Data Compression

# used for encoding
class Item:
    def __init__(self, l=[], f=0):
        self.list = l
        self.frequency = f

    def __lt__(self, other):
        return self.frequency < other.frequency

# node for the binary search tree used for decoding
class Node:
    def __init__(self, a=''):
        self.ascii_value = a
        self.left = None
        self.right = None

def code_building_module_part1():
    #read in file
    filename = "File1ASCII.txt"

    inputText = open(filename)
    string = inputText.read()
    inputText.close()

    #determine frequencies of each character
    ascii = [ord(c) for c in string]
    frequency_list = [0] * 127
    for i in ascii:
        frequency_list[i] = frequency_list[i] + 1


    #set up list of Items that the Huffman Algorithm will be applied on
    item_list = []
    for i in range(32,127):
        item_list.append(Item([i], frequency_list[i]))
    item_list.append(Item([10], frequency_list[10]))

    item_list.sort()



    #list will contain the code strings
    code_string_list = [''] * 127

    #apply the Huffman Algorithm to all the items
    while len(item_list) > 1:

        newestlist = item_list[0].list + item_list[1].list
        newestFrequency = item_list[0].frequency + item_list[0].frequency
        newestItem = Item(newestlist,newestFrequency)

        for i in item_list[0].list:
            code_string_list[i] = '0' + code_string_list[i]

        for i in item_list[1].list:
            code_string_list[i] = '1' + code_string_list[i]

        item_list.pop(0)
        item_list.pop(0)
        item_list.append(newestItem)
        item_list.sort()

    #generate output file
    outputList = []
    outputList.append(str(10))
    outputList.append(' ')
    outputList.append(code_string_list[10])
    outputList.append('\n')

    for i in range(32,127):
        outputList.append(str(i))
        outputList.append(' ')
        outputList.append(code_string_list[i])
        outputList.append('\n')
    outputString = ''.join(outputList)
    #print(outputString)

    outputFile = open('code_string_dictionary1.txt','w')
    outputFile.write(outputString)
    outputFile.close()


#does same thing as code_building_module _part1() exceot for multiple text files inside a directory
def code_building_module_part2():

    #store the frequencies of all 127 characters
    frequency_list = [0] * 127

    #open all files in the collection
    import os
    script_dir = os.path.dirname(__file__)
    directory_name = 'Canonical Collection 1 '
    dir_path = os.path.join(script_dir,directory_name)
    dirs = os.listdir(dir_path)

    for filename in dirs:
        if filename.endswith('.txt'):
            filepath = os.path.join(dir_path, filename)
            with open(filepath) as input_text:
                string = input_text.read()

            # determine frequencies of each character
            ascii = [ord(c) for c in string]
            for i in ascii:
                frequency_list[i] = frequency_list[i] + 1

    #set up list of Items that the Huffman Algorithm will be applied on
    item_list = []
    for i in range(32,127):
        item_list.append(Item([i], frequency_list[i]))
    item_list.append(Item([10], frequency_list[10]))

    item_list.sort()



    #list will contain the code strings
    code_string_list = [''] * 127

    #apply the Huffman Algorithm to all the items
    while len(item_list) > 1:

        newestlist = item_list[0].list + item_list[1].list
        newestFrequency = item_list[0].frequency + item_list[0].frequency
        newestItem = Item(newestlist,newestFrequency)

        for i in item_list[0].list:
            code_string_list[i] = '0' + code_string_list[i]

        for i in item_list[1].list:
            code_string_list[i] = '1' + code_string_list[i]

        item_list.pop(0)
        item_list.pop(0)
        item_list.append(newestItem)
        item_list.sort()

    #generate output file
    outputList = []
    outputList.append(str(10))
    outputList.append(' ')
    outputList.append(code_string_list[10])
    outputList.append('\n')

    for i in range(32,127):
        outputList.append(str(i))
        outputList.append(' ')
        outputList.append(code_string_list[i])
        outputList.append('\n')
    outputString = ''.join(outputList)
    #print(outputString)

    outputFile = open('code_string_dictionary2.txt','w')
    outputFile.write(outputString)
    outputFile.close()



#read in code_string_dictionary text file and store in list
#helper function used for both encoding and decoding
def create_list_from_dictionary(filename):
    dictionary_list = [''] * 127
    with open(filename) as code_string_dictionary:
        line = code_string_dictionary.readline()
        while line:
            splitLine = line.split()
            if len(splitLine) == 2:
                index = int(splitLine[0])
                dictionary_list[index] = splitLine[1]
            line = code_string_dictionary.readline()

    return dictionary_list

#encodes a single text file
#used for part 1
def encoding_module_part1():
    #read in code string dictionary text file and store in list
    dictionary_list = create_list_from_dictionary('code_string_dictionary1.txt')

    #generate encoded string
    output_list = []

    #File1ASCII.txt
    filename = input("Enter filename of text file to be encoded")
    with open(filename) as input_text:
        for line in input_text:
            for char in line:
                value = ord(char)
                output_list.append(dictionary_list[value])

    #write encoded string to text file
    output_string = ''.join(output_list)
    with open('encoded_text.txt','w') as encoded_text:
        encoded_text.write(output_string)
    print('encoded ' + filename)


# encode a text file
# encodes all files in Data 20191031 directory, used for part 2
def encoding_module_part2():
    #read in code string dictionary text file and store in list
    dictionary_list = create_list_from_dictionary('code_string_dictionary2.txt')


    #create a list of all file names in the Data 20191031 directory
    import os
    script_dir = os.path.dirname(__file__)
    directory_name = 'Data 20191031'
    dir_path = os.path.join(script_dir,directory_name)
    dirs = os.listdir(dir_path)

    #encode each file in the Data 20191031 directory
    for filename in dirs:
        if filename.endswith('.txt'):

            #generate encoded string
            output_list = []

            filepath = os.path.join(dir_path,filename)
            with open(filepath) as input_text:
                for line in input_text:
                    for char in line:
                        value = ord(char)
                        output_list.append(dictionary_list[value])

            #write encoded string to text file
            output_string = ''.join(output_list)
            with open('encoded'+filename ,'w') as encoded_text:
                encoded_text.write(output_string)
            print('encoded ' + filename)




def decoding_module():
    #read in code string dictionary text file and store in list
    dictionary_list = create_list_from_dictionary('code_string_dictionary1.txt')
    # for i in range(len(dictionary_list)):
    #     print(str(i)+ dictionary_list[i])

    root = Node()

    # create binary tree
    dic_length = len(dictionary_list)
    for i in range(dic_length):
        current = root
        sequence = dictionary_list[i]

        length = len(sequence)
        for j in range(length):
            if sequence[j] == '0':
                if not current.left:
                    current.left = Node()
                current = current.left

            elif sequence[j] == '1':
                    if not current.right:
                        current.right = Node()
                    current = current.right

            if j == length-1:
                current.ascii_value = i

    # decode text using the binary tree
    output_text_list=[]
    current = root

    filename = 'encoded_text.txt'

    with open(filename) as encoded:
        for line in encoded:
            for char in line:
                if char == '0':
                    current = current.left
                elif char == '1':
                    current = current.right
                if not current.left and not current.right:
                    output_text_list.append(chr(current.ascii_value))
                    current = root
    # output decoded text
    output_string = ''.join(output_text_list)
    with open('decoded_text.txt','w') as decoded:
        decoded.write(output_string)
    print('decoded ' +filename )

#Part 1
code_building_module_part1()
encoding_module_part1()
decoding_module()
print("")

#Part 2
code_building_module_part2()
encoding_module_part2()
