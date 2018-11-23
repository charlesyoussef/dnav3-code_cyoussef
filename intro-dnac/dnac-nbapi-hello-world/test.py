import sys

def main():
    if len(sys.argv) > 1:
        print("Number of args is: " + str(len(sys.argv)))
        print(sys.argv[0])
        print(sys.argv[1])
    else:
        print("you must enter some args.")

if __name__ == '__main__':
    main()
