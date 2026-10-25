
def mutate_string(string, position, character):
    l = string[:position]+character+string[position + 1:]
    return l
    
    ''' l = list(string)
    l[position] = character
    string = ''.join(l)
    return string'''
    


