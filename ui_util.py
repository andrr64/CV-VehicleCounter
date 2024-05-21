def printLine(length= 50):
    print(f"+{'-'*length}+")
    
def printCenter(text: str, length = 50):
    print("|"+ text.center(length) + "|")

def printLeft(text: str, length = 50):
    print("| " + text.ljust(length-1) + "|")
