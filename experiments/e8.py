# 'with' context manager

# do not need 'r' as second argument because open() defaults to mode='r'
with open("../files/doc.txt", "r") as file:
    file.read()