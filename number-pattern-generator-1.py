print("==== Number pattern Generator ====")

n=int(input("Enter number of rows:"))

print("\n 1. Increasing pattern")
print("2.. Repeated number pattern")

choice =input("Choose pattern:")

if choice =="1":
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()

elif choice=="2":
    for i in range(1,n+1):
        for j in range(i):
           print(i,end="")

        print()
else:
    print("Invalid choice!")