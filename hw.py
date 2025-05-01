import os
sd=input("Do you want to shutdown your computer?(yes or no): ")
if sd=="no":
    exit()
else:
     os.system("shutdown /s /t 1")