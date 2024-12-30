import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Sales= [200, 220, 225, 275, 280, 320, 350, 350, 400, 420, 465, 470]
Profit= [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]

plt.xlabel("Sales")
plt.ylabel("Profit")

plt.scatter(Sales, Profit)
plt.show()