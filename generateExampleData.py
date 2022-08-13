import random
import json
import os
import sys

agreement = input("WARNING!\nThis script will remove every file in the current directory and generate new ones\nAre you sure you are in the plotData folder?\n(Y/n): ")
if agreement != "y" and len(agreement) != 0:
    exit()

print("Proceeding...")

selfFileName = sys.argv[0]
print(f"Removing files except {selfFileName}")

for root, subFolders, files in os.walk("."):
    for file in files:
        if file != selfFileName:
            os.remove(file)

dataCount = random.randint(300, 600)
print(f"Generating {dataCount} files with random data")

f = open("data.txt", "w")
for i in range(dataCount):
    f.write(f"tick={(i +5 )* 5},itemCount={random.randint(0, 1024)},vehicleCount={random.randint(0, 2048)},tpsCount={random.random() * 62.5}\n")
f.close()

print("All done!")