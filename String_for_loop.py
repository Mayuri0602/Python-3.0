# Count capital and small letters
data="REGex"
count_upper=0
count_lower=0
for i in data:
    if i.isupper():
     count_upper+=1
    elif i.islower():
       count_lower+=1
print(f"Upper count = {count_upper} and Lower count = {count_lower}")       
     

# Reverse the string
data = "regex"                                  # positive index with step value -1
for i in range(-1,-len(data)-1,-1):
    print(data[i],end="")


# Reverse the string
data = "radhey"                                  # positive index with step value -1
for i in range(len(data)-1,-1,-1):
    print(data[i],end="")


# Reverse the string 
data = "mayank" 
reverse_data =""
for i in data:
    reverse_data = i + reverse_data   
print(reverse_data)


# Check if the string is pallindrome or not. 
data = "eve"
check = ""
for i in range(len(data)-1,-1,-1):
    check += data[i]
if data == check:
    print("Pallindrome")
else:
    print("Not Pallindrome")    


# Remove duplicate characters from a string
data = "madam"
data_2 = ""
for i in range(0,len(data)):
    if data[i] not in data_2:
        data_2 += data[i]
print(data_2)            


# Filter digits from a string
data = "abc123"
data_2 = ""
for i in range(0,len(data)):
    if not data[i].isdigit() :
        data_2 += data[i]
print(data_2)         


# Count number of vowels in a string
data = "mayuri"
count = 0
for i in range(0,len(data)):
    if data[i] in 'aeiouAEIOU':
       count+=1
print(count)


# Remove white space from a string
data = "abc 123"
remove_space = "" 
for i in range(0,len(data)):
    if not data[i]==" ":
     remove_space = remove_space + data[i]
print(remove_space)