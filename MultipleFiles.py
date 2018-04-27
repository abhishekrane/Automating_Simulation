import os

#change the working directory
os.chdir("C:/Users/arane/Desktop/abhi")
#Giving path to the file containing the names of the file
filepath = 'C:/Users/arane/Desktop/abhi/inputfile.txt'

#Making new directory to store the output
os.mkdir("C:/Users/arane/Desktop/abhi/output")
fp = open(filepath)

#Rading the file and looping over
for line in fp:
   filename = line.rstrip('\n')
#Command to execute
   cmd = 'lmp_serial.exe < {file} > output/{optFile}'.format(file=filename,optFile=filename)

   os.system(cmd)

