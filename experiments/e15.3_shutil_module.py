import shutil

'''make a .zip file from the directory ../files. all files in that folder will be put into a .zip filetype.'''

shutil.make_archive("output", "zip", "../files")