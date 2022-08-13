import json
import matplotlib.pyplot as plt
import os
import sys
import glob
import re

# creidts https://stackoverflow.com/questions/29916065/how-to-do-camelcase-split-in-python
def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    tab = [m.group(0) for m in matches]
    ret = ""
    for a in tab:
        ret = ret + a[0].upper() + a[1:] + " "
    ret = ret[:-1] + "s"
    return ret

rootDir = input("** Specify the directory where the plot data exist, none for './plotData'.\nName: ")
if len(rootDir) == 0:
    rootDir = "./plotData"
elif not os.path.exists(rootDir):
    print(f"Folder '{rootDir}' doesn't exist.\nExitting...")
    exit(1)

setter = "="
delimiter = ","

variables = {}
variableCounts = {}
maxY = 0

fileName = input("** Specify a file name to be read, none for latest.\nName: ")

if fileName == "":
    print(f"Reading {rootDir} for latest data")

file = os.path.join(rootDir, fileName + ".txt")
if fileName == "":
    files = glob.glob(os.path.join(rootDir, '*.txt'))
    file = max(files, key=os.path.getctime)

fd = open(file)
for line in fd.readlines():
    setVarNames = False
    if len(variables) == 0:
        setVarNames = True
    dataVars = line.split(delimiter)
    for data in dataVars:
        name, value = (data.split(setter))
        value = value.replace("\n", "")
        value = value.replace(",", "")
        
        if setVarNames:
            variables[name] = True
        elif not variables[name]:
            print(f"New variable name encountered '{name}'.\nPlease re-run performance scripts.")
            exit(1)
        
        if not (name in variableCounts):
            variableCounts[name] = []
        
        valueNumber = value
        if "." in valueNumber:
            valueNumber = float(value)
        else:
            valueNumber = int(value)
        variableCounts[name].append(valueNumber)

print(f"Read '{len(variableCounts)}' vars")

print("Creating plot")

timeVar = input(f"** Specify the time variable, none for auto.\nAvailable variable names {list(variables.keys())}.\nVariable Name: ")
if len(timeVar) == 0:
    timeVar = None
elif not variables[timeVar]:
    print(f"Variable name '{timeVar}' doesn't exist.\nExitting...")
    exit(1)
else:
    timeVar = variableCounts[timeVar]
fig, ax = plt.subplots()

for var in variableCounts:
    if timeVar:
        if variableCounts[var] == timeVar:
            continue
        ax.plot(timeVar, variableCounts[var], label = camel_case_split(var))
    else:
        ax.plot(variableCounts[var], label = camel_case_split(var))
    ax.set(xlabel="Ticks", ylabel='Values',
       title='Values across ticks')

ax.grid()
ax.legend()

plt.show()