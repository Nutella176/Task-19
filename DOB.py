#Read data from DOB.txt
open_file = open('DOB.txt', 'r', encoding = 'utf-8')
data = open_file.readlines()

#Use a for loop and split data line to get names and surnames only
#Join to remove commas and brackets and print names
print("Name")
for line in data:
    split_data = line.split()
    name = " ".join(split_data[ : 2])
    print(name)
    
#Use a for loop and split data line to get dates only
#Join to remove commas and brackets and print birth dates
print("\n" "Birthdate")
for line in data:
    split_data = line.split()
    birthdate = (" ".join(split_data[2: ]))
    print(birthdate)
    
open_file.close()
