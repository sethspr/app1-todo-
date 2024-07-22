contents = ["Hello", "Hello", "Hello"]

filenames = ["6_6_doc.txt", "6_6_report.txt", "6_6_presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../coding exercises/{filename}", "w")
    file.write(content)


# Ardit solution
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for filename in filenames:
#     file = open(filename, 'w')
#     file.write("Hello")
#     file.close()