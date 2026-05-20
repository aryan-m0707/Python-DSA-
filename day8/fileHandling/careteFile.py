import logging
logging.basicConfig(filename='newfile.txt', level=logging.DEBUG)
try:
    a = int(input('Enter the value for a: '))
    b = int(input('Enter the value for b: '))
    print(a/b)
except (ZeroDivisionError, ValueError) as message:
    print(message)
    logging.exception(message)
print("Logging level is set up, Check 'newFile.txt' for log details.")