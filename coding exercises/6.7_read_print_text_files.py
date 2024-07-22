filenames = ['6_7_a.txt', '6_7_b.txt', '6_7_c.txt']

for files in filenames:
    file = open(files, 'r')
    print(file.read())

# Ardit solution
# filenames = ['6_7_a.txt', '6_7_b.txt', '6_7_c.txt']
#
# for filename in filenames:
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)