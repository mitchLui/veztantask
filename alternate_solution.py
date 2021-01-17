from collections import Counter

def countString() -> list:
    counter = [[x, y] for x, y in dict(Counter(input("Input string: "))).items()]
    return counter

if __name__ == "__main__":
    counter = countString()
    print(counter)