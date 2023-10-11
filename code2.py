no1= int(input("give me a no"))
strr = str(no1)
list_of_number = list(map(int, strr.strip()))
print(sum(list_of_number))