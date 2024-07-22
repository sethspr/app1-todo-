# transforming list of strings to list comprehension

filenames = ["1.doc", "1.report", "1.presentation"]

# transform "1.doc" to "1-doc.txt" with concatenation
filenames = [filename.replace(".", "-") + ".txt" for filename in filenames]

print(filenames)
