list_of_symbols = [["(", "[", "{"], [")", "]", "}"]]

def check_if_is_balanced(pattern):
    stack = [] 

    for letter in pattern: 
        if letter in list_of_symbols[0]: 
            stack.append(letter) 
        elif letter in list_of_symbols[1]: 
            index_of_closing_symbol = list_of_symbols[1].index(letter)

            if len(stack) > 0 and list_of_symbols[0][index_of_closing_symbol] \
             == stack[len(stack)-1]: 
                stack.pop() 
            else: 
                return "Is not BALANCED"

    if len(stack) == 0: 
        return "It is BALANCED"
    else: 
        return "Is not BALANCED"
