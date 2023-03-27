def exit_na():
    print("exit..na")

def is1():
    data1 = ["apple","strawberry","guava"]
    ask = str(input("Type of fruits: "))
    if ask in data1:
        print("This is a fruit")
    else:
        print("I cannot identify the object")

# Add a loop that continues to ask for input until the user enters "exit"
while True:
    userInput = input("Type any to continue or type 'exit' to exit: ")
    if userInput == "exit":
        exit_na()
        break
    else:
        is1()
