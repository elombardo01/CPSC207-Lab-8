#Emme and Leena
#Lab 8 part B

string = "SPAM!HelloSPAM! worldSPAM!"

def remove_substring(remove):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(remove)] == remove:
            index += len(remove)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))

remove_substring("SPAM!")
    
