#Assignment2
#Adam Gronowski
#20051808
#Subset Sum
#I certify that this submission contains my own work


import operator
import math
from random import randrange
import numpy as np
import matplotlib.pyplot as plt

class Set:
    def __init__(self):
        self.elements = set()
        self.sum = 0

#Part 1 of assignment
#tests BFI and
def testing_part1():
    print('testing with BFI:')
    print('')

    S = {1, 2, 3}
    print("S = " + str(S))
    # target value in set
    BFI_Subset_Sum(S, 2)

    # target value is the sum of the entire set
    BFI_Subset_Sum(S, 6)

    # no subset that sums to the target value
    BFI_Subset_Sum(S, 7)

    # other
    BFI_Subset_Sum(S, 5)

    print('')
    S = {1, 2, 4, 8}
    print("S = " + str(S))
    # target value in set
    BFI_Subset_Sum(S, 8)
    # target value is the sum of the entire set
    BFI_Subset_Sum(S, 15)
    # no subset that sums to the target value
    BFI_Subset_Sum(S, 16)
    # other
    BFI_Subset_Sum(S, 13)

    print('')
    print('testing with HS:')
    print('')
    S = {1, 2, 3}
    print("S = " + str(S))
    # target value in set
    HS_Subset_Sum(S, 2)
    # target value is the sum of the entire set
    HS_Subset_Sum(S, 6)
    # no subset that sums to the target value
    HS_Subset_Sum(S, 7)
    # other
    HS_Subset_Sum(S, 5)

    S = {1, 2, 4, 8}
    print("S = " + str(S))
    # target value in set
    HS_Subset_Sum(S, 8)
    # target value is the sum of the entire set
    HS_Subset_Sum(S, 15)
    # no subset that sums to the target value
    HS_Subset_Sum(S, 16)
    # other
    HS_Subset_Sum(S, 13)




# modified is set to True when called by HS_Subset Sum
# this results in all subsets being found rather than stopping when there is a match
# no_ouput supresses the print statements
def BFI_Subset_Sum(S, k, modified=False, no_output=False):

    S = S.copy()
    empty_set = Set()
    subsets = []
    subsets.append(empty_set)

    #x is the number of operations
    x = 0

    n = len(S)
    for i in range(n):
        s_i = S.pop()
        x += 1

        subsets_length = len(subsets)
        for j in range(subsets_length):
            old_u = subsets[j]
            new_u = Set()
            new_u.elements = old_u.elements|{s_i}
            new_u.sum = old_u.sum + s_i

            if new_u.sum == k:
                if not no_output:
                    print("subset found that sums to " + str(k) + ":")
                    print(new_u.elements)
                return False, x
            subsets.append(new_u)
            x += 6

    if not modified:
        if not no_output:
            print("no subset found that sums to " + str(k))
    return subsets, x

# no_output suppresses the print statements
def HS_Subset_Sum(S,k,no_output=False):
    # x is number of operations
    x = 0

    S = S.copy()
    # Split S into 2
    S_left = set()
    S_length = len(S)
    for i in range(S_length//2):
        S_left.add(S.pop())
        x += 1
    S_right = S

    # return if k is in left subset
    subsets_left, y = BFI_Subset_Sum(S_left,k,True,no_output)
    x += y
    if not subsets_left:
        return x

    # return if k is in right subset
    subsets_right, y = BFI_Subset_Sum(S_right, k, True,no_output)
    x += y
    if not subsets_right:
        return x

    # sort the two subsets


    subsets_left.sort(key=operator.attrgetter('sum'))
    t = len(subsets_left)
    x += int(3 * t * math.log2(t))

    subsets_right.sort(key=operator.attrgetter('sum'))
    x += int(3*t* math.log2(t))
    t = len(subsets_right)

    i = 0
    length_l = len(subsets_left)
    j = len(subsets_right)-1

    while i < length_l and j > 0:
        if subsets_left[i].sum + subsets_right[j].sum == k:
            x += 2
            if not no_output:
                print("subset found that sums to " + str(k) + ":")
                print(subsets_left[i].elements|subsets_right[j].elements)
            return x
        elif subsets_left[i].sum + subsets_right[j].sum > k:
            x += 2
            j -= 1
        else:
            i += 1

    if not no_output:
        print('no subset found that sums to ' + str(k))
    return x

# Part2 of Assignment
# calculates average number of operations for BFI and HS
# Creates a table and plots
def testing_part2():
    rows, cols = (12, 5)
    table = [[0 for i in range(cols)] for j in range(rows)]
    index = 0

    for n in range(4,16):

        BFI_operations = 0
        HS_operations = 0

        for i in range(20):
            # create set of n random integers
            S = set()
            for j in range(n):
                random = randrange(50)
                while random in S:
                    random = randrange(50)
                S.add(random)

            #create set of 15 random integers
            K = set()
            for k in range(15):
                random = randrange(n*50)
                while random in K:
                    random = randrange(n*50)
                K.add(random)

            BFI_operations_set = 0
            HS_operations_set = 0
            for k in range(15):
                target = K.pop()
                subsets, y = BFI_Subset_Sum(S,target,False,True)
                BFI_operations_set += y
                z = HS_Subset_Sum(S,target,True)
                HS_operations_set += z

            BFI_operations += BFI_operations_set // 15
            HS_operations += HS_operations_set // 15

        BFI_operations = BFI_operations // 20
        HS_operations = HS_operations_set // 20

        table[index][0] = n
        table[index][1] = BFI_operations
        table[index][2] = HS_operations
        table[index][3] = int(10*(2**n))
        table[index][4] = int(5*n*(2**(n/2)))
        index += 1

        print('n = ' + str(n) +', number of BFI operations: ' + str(BFI_operations))
        print('n = ' + str(n) +', number of HS operations: ' + str(HS_operations))

    table = np.array(table)
    x_axis = table[:,0]
    BFI = table[:,1]
    HS = table[:,2]
    O2n = table[:,3]
    On2n2 = table[:,4]

    np.set_printoptions(suppress=True)
    print(table[:,:3])

    marker = "*--"

    plt.plot(x_axis, BFI, marker, label='BFI')
    plt.plot(x_axis, HS, marker, label='HS')
    plt.legend(loc='best')
    plt.xticks(x_axis)
    plt.xlabel('n')
    plt.ylabel('Number of operations')
    plt.title('Comparison of BFI and HS')
    plt.show()

    plt.plot(x_axis, BFI, marker, label='BFI')
    plt.plot(x_axis, O2n, marker, label=r'10*$2^n$')
    plt.legend(loc='best')
    plt.xticks(x_axis)
    plt.xlabel('n')
    plt.ylabel('Number of operations')
    plt.title('Time complexity of BFI')
    plt.show()

    plt.plot(x_axis, HS, marker, label='HS')
    plt.plot(x_axis, On2n2, marker, label=r'$5n*2^{\frac{n}{2}}$')
    plt.legend(loc='best')
    plt.xticks(x_axis)
    plt.xlabel('n')
    plt.ylabel('Number of operations')
    plt.title('Time complexity of HS')
    plt.show()

testing_part1()
testing_part2()
