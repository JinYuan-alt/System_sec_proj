import random, string
letters = string.ascii_lowercase
final_str = []
seshid=""
beta_str = ''.join(random.choice(letters) for i in range(8))
for i in range(len(beta_str)):
    final_str.append(beta_str[i])
for i in range(len(final_str)):
    if (i + 1) % 2 == 0 and final_str[i] != final_str[-1]:
        final_str.insert(random.randint(0, 9),i)
for i in range(len(final_str)):
    temp=final_str[i]
    seshid=seshid+str(temp)

print("Random string of random length","is:", seshid)