# CREATE FILES WITH CONTENTS BY ZIP() METHOD VIA TWO LISTS IN FOR LOOP

contents = ["All carrots are to be sliced julienne style",
            "The carrots were reported as sliced",
            "The presentation of the cuts are acceptable"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)

# a = "this is a test of how to breakup " \
#      "a string into several lines"
#
# print(a)