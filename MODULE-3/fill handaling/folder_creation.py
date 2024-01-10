import os
if os.path.exists("myfolder"):
    print("already exists")
else:
    os.mkdir("myfolder")
    print("created")
#for delete folder os.rmdir("foldername")