import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Sales= [200, 220, 240, 275, 300, 320]
Profit= [50, 60, 65, 80, 90, 100]

plt.xlabel("Sales")
plt.ylabel("Profit")

plt.bar(Sales, Profit, color=['Red','Blue','Green','Violet','Orange'], width= 4)
plt.show()
