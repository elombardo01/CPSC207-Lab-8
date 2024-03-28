#Emme and Leena
#Lab 8 part C

string = "SPAM!HelloSPAM! worldSPAM!"

def replace_substring(remove,replace):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(remove)] == remove:
            index += len(remove)
            output.append(replace)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))

replace_substring("SPAM!",":)")
