def printLine(length= 50):
    print(f"+{'-'*length}+")
    
def printCenter(text: str):
    print("|"+ text.center(50) + "|")

def printLeft(text: str):
    print("| " + text.ljust(49) + "|")
