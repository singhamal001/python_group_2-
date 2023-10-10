age_store={}

ram= input("what's your age ram")
shyam=input("what's your age shyam")
gita=input("what's your age gita")


age_store["ram"] = ram
age_store["shyam"] = shyam
age_store["gita"] = gita
max_value = max(age_store,key=age_store.get)
print(max_value,"you are the oldest")
