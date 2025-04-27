#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 2025

@author: braden
"""
import numpy as np
import matplotlib.pyplot as plt
file = "900_20por_110-120_1hr_(.30-.42speed)"
filecsv = file + ".csv"

def find_skiprows(filecsv):
  """Finds the amount of rows to skip on the CSV file for data analysis.

  This function starts by opening the data file in read mode. It then begins reading 
  each line of the data file, keeping track of the line it is on, and adding the 
  content of the 2nd column of the line it is on to a list of strings. After adding a 
  string to the list, it then checks to see if that string says "Calibration 
  complete." If it does, it then knows that it has reached the row where data will 
  start to be analyzed and therefore how many rows need to be skipped in data 
  analysis.

  Args:
    filename: A string with the name of the data file being analyzed.

  Returns:
    rows: The amount of rows before it reached the string "Calibration complete."

  Raises:
    ValueError: If "Calibration complete." is not found within the data file.
  """
  with open(filecsv, 'r') as file:
    for i, line in enumerate(file):
      columns = line.strip().split(",")
      if len(columns) > 1 and columns[1].strip() == "Calibration complete.":
        rows = i + 1
        return rows
  raise ValueError("'Calibration complete.' not found in second column")

skiprows = find_skiprows(filecsv)

pressuredata = np.loadtxt(filecsv, delimiter=",", skiprows = skiprows, usecols=[2])

average = np.mean(pressuredata)

time = list(range(1, len(pressuredata) +1)) #creates list of 1 second intervals to plot differential pressure against

plt.plot(time, pressuredata)
plt.text(0.5*len(time), average+1.5, f"Average = {average:.5} Pa")
plt.xlabel("Time (s)")
plt.ylabel("Differential Pressure (Pa)")
plt.title("Differential Pressure for 900x20por 120mm")
plt.savefig(file+".png")
