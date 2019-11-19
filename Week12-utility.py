#https://github.com/HellosesImMoses/Week12-utility
#Ryan Moses
#CSCI 102 - Section A
#Week 12 - Part A/B

#functions
def PrintOutput(string):
    print('OUTPUT {}'. format(string))

def LoadFile(file_name):
    my_list = []
    with open(file_name, 'r') as file:
        for i in file:
            my_list.append(i.strip('\n'))
        return(my_list)

def UpdateString(base_string, change_string, index):
    my_list = []
    output = ''
    for word in base_string:
        for char in word:
            my_list.append(char)
    my_list[index] = change_string
    output = output.join(my_list)
    print('OUTPUT {}'. format(output))

def FindWordCount(my_list, string):
    counter = 0
    for i in my_list:
        if i.lower() == string.lower():
            counter += 1
    print('OUTPUT {}'. format(counter))

def ScoreFinder(players, scores, name):
    x = 0
    for i in range(len(players)):
        if players[i].lower() == name.lower():
            print('OUTPUT {} got a score of {}'. format(players[i], scores[i]))
            x = 1
    if x == 1:
        pass
    else:
        print('OUTPUT player not found')

def Union(list1, list2):
    output = []
    for i in list1:
        if i not in output:
            output.append(i)
    for i in list2:
        if i not in output:
            output.append(i)
    return output

def Intersection(list1, list2):
    output = []
    for i in list1:
        if i in list2:
            output.append(i)
    return output

def NotIn(list1, list2):
    output = []
    for i in list1:
        if i not in list2:
            output.append(i)
    return output
