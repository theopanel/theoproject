
def try_me():
    x = input('What do you want to eat for lunch ? ')
    if x.lower() == "kebab" or x.lower() == "burger":
        return "Do some sport instead you lazyyy"
    else:
        return "Good choice!"

if __name__ == "__main__":
    print(try_me())
