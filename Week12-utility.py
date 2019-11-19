#*github repo url*
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
