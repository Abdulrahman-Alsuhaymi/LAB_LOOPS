for i in range(45, 211):
    if i == 100:
        continue
    if i == 205:
        break
    print (i)

print("--"*20)

while True:
    answer = input("what is the product of 7 * 24? ")
    if int(answer) == 168:
        print("You answered this Question correctly") 
        break
    else:
        print("Your Answer is wrong try again..")
    
print("--"*20)


n = int(input("Enter a positive number: "))

even_sum = 0
for i in range(1,n + 1):
    if i % 2 == 0:
        even_sum += i

print(f"The sum of even numbers between 1 and {n} is {even_sum}")
        
        
    

    
