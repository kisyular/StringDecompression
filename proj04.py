#############################################
#Algorithm
#initiate the variable "decompressed_string" to an empty string
#initiate a while True Loop
#prompt the user to enter a string tocompress
#Quit the program if the user enters an empty string
#Initiate a while loop if user enters string
#find the first bracket and convert it into an integer
#find the other bracket ")"
#find the comma index and convert it to an integer
#find the first number within the parenthesis and convert it to integer
#find the index of the second number within the comma and the last parenthesis
#get the string within the first index and the second index numbers
#find the decompressed string. Given by the string entered plus string within
#update the new string entered to a newer one
#replace the backslash with a new line during printing
#print the decompressed string    

Backslash = "\\"

#initiate the variable "decompressed_string" to an empty string
decompressed_string =""
print()
#initiate a while True Loop
while True:

#prompt the user to enter a string tocompress
    string_entered=input ("\nEnter a string to decompress (example 'to be or not to(13,3)' \
will be decompressed to 'TO BE OR NOT TO BE' see more examples in the pdf attached \
or press 'enter' to quit: ")
    
#Quit the program if the user enters an empty string
    if string_entered=="" :
        print("There is nothing to decompress. The Program has halted")
        break
#Initiate a while loop if user enters string
    while string_entered.find("(") != -1:
        
#find the first bracket and convert it into an integer
        bracket_1st=int(string_entered.find("("))
        
#find the other bracket nd convert to an integer ")"
        sec_bracket=int(string_entered.find(")"))
        
#find the comma index and convert it to an integer
        comma=int(string_entered.find(",", bracket_1st, sec_bracket))
        
# find the first number within the parenthesis and convert it to integer
        index_1st = int(string_entered[bracket_1st+1: comma])
        
# find the index of the second number within the comma and the last parenthesis
        sec_indx=int(string_entered[comma+1 : sec_bracket])
        
#get the string within the first index and the second index numbers
        string_within=string_entered[bracket_1st - index_1st \
        : bracket_1st - index_1st + sec_indx]

#find the decompressed string. Given by the string entered plus string within
        decompressed_string=(string_entered [ : bracket_1st] + string_within)
        
#update the new string entered to a newer one
        string_entered=decompressed_string + string_entered[sec_bracket+1: ]
        
#replace the backslash with a new line during printing
        decompressed_string=string_entered.replace(Backslash, "\n")

#print the decompressed string    
    print("\nYour decompressed string is:" "\n")
    print(decompressed_string)
