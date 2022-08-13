import random
import json
import os
import sys

dataCount = random.randint(300, 600)
print(f"Generating {dataCount} files with random data")

f = open("data.txt", "w")
for i in range(dataCount):
    f.write(f"tick={(i +5 )* 5},itemCount={random.randint(0, 1024)},vehicleCount={random.randint(0, 2048)},tpsCount={random.random() * 62.5}\n")
f.close()

print("All done!")
