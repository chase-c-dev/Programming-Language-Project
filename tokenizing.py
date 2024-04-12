# This file contains the functions for tokenizing which breaks down structures of the codes and identifies all the individual components 

def tokenize(srcCode): # tokenizes all the input code
    tokenizingDict = { # dictionary contains all tokens for relevant elements
        "(" : "LPAREN",
        ")" : "RPAREN",
        "0" : "NUMB",
        "1" : "NUMB",
        "2" : "NUMB",
        "3" : "NUMB",
        "4" : "NUMB",
        "5" : "NUMB",
        "6" : "NUMB",
        "7" : "NUMB",
        "8" : "NUMB",
        "9" : "NUMB",
        "+" : "PLUS",
        "*" : "TIMES",
    }
    
    num_holder = ""
    num_index = 0

    list = []
    i = 0
    srcCode += " " # add an empty string to the end to counteract the length-1
    while i < len(srcCode)-1:
        if srcCode[i] != " ":
            #print(i)
            if srcCode[i+1] != " " and tokenizingDict[srcCode[i]] == "NUMB" and tokenizingDict[srcCode[i+1]] == "NUMB": # if statement checks to see if a number is multiple digits
                num_index = i
                while srcCode[num_index] != " " and tokenizingDict[srcCode[num_index]] == "NUMB" and num_index != len(srcCode): # stores full number in a string
                    num_holder += srcCode[num_index]
                    num_index += 1
                        
                list.append([num_holder, tokenizingDict[srcCode[i]]]) # assigns string containing number greater than 1 digit to one index in the resulting list
                i = num_index

                num_holder = "" # reset temp variables
                num_index = 0   # reset temp variables

            else:
                list.append([srcCode[i], tokenizingDict[srcCode[i]]]) # adds element to list: srcCode[i] is the element and tokenizingDict is the token
        i += 1

    return list