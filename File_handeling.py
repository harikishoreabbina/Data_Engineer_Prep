# FILE HADLING
# it is used to Read, Write, and change data in files and helps to maintain data beyond execution.
# so in this the code will open the files, make some changes as needed and closes it.

#"r "mode
with open("File_handling example.txt","r") as file1:  # "with" helps to open the file and close it safely.
    content = file1.read() # this will read the file and we are storing it in "content" variable
    print(content)
    
    

with open("C:/Users/Harik/Desktop/F_H_Example 2.txt", "r") as file2: # use the entire path to open the file with forward slashes
    content2 = file2.read()
    print(content2)
    
# 2nd method

path = r"C:\Users\Harik\Desktop\F_H_Example 2.txt" # we are giving the file path before the main code and using its variable
        #r"" is a raw string, it tells the python  to treat special chars(/,\ as normal characters not like \n or \t)
with open(path,"r") as file3:
    content3 = file3.read()
    print(content3)
    
#"w" mode    
    
with open("File_handeling example.txt","w") as file1: # a new file will be created after the execution
    file1.write("this is the new  text")
    print(file1)
    # 'w' is the write mode, it will write the new data to a file
    # or it will overwrite the exesting data in the file

#path = r"C:\Users\Harik\Desktop\F_H_Example 2.txt" 
#with open(path,"w") as file1: # a new file will be created after the execution
#   file1.write("this is the new  text")
#    print(file1)


# "a" mode is used to add new data to the end of the old data with out any changes
# "a" mode adds the new data "w" mode rewrites the old data
with open("File_handeling example.txt","a") as file4:
    file4.write("\nI will become the king of the pirates")