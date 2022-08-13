# SDG
Simple Data Grapher (SDG), is a simple Python script to plot values inputted from a .txt file automatically.

## Usage
Install Matplotlib with `pip install matplotlib` or follow the instructions in their website. Put the `graph.py` file somewhere close to where your input exists, and run with `python graph.py`.
You will be prompted with multiple questions for specifying where the input data relies, what the name of the input file is, what the time variable is.

## Input file format
This format is as simple as it gets with human readable, easily modifyable type.
Every single line is a new entry. A line can have multiple variables set with a setter ('=' can be edited.) and concatenated with a delimeter (',' is the current one, can be edited in the script).
A line should contain a time variable so that your input data is more in context with time axis.

Example lines:
```
tick=22495,playerCount=42,bulletCount=332
```
```
time=23.5,stockEconPrice=224.955,delta=3.2
```
