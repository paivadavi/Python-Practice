#Create 10 files, named file1.txt, file2.txt and so on till file10.txt. The files should contain the number corresponding to their name. 
#So, file1.txt should contain one line with number 1, file2.txt — one line with number 2 and so on.

file_template = "file"
for i in range(1, 11):
    file_name = "{}{}{}".format("file", str(i), ".txt")
    with open(file_name, 'w') as current_file:
        current_file.write(str(i))
       
#Problem encountered on JetBrainsAcademy
