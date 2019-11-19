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

