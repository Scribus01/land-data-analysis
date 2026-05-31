import pandas as pd
import matplotlib.pyplot as plt

#load survey data
df = pd.read_csv(r"c:\Users\hp\Desktop\land_project\XYZ_for_C_and_I_Leasing_Survey.csv", sep="t")

# clean columns names
df.columns =df.columns.str.replace(",","", regex=False)\
                      .str.replace(",","", regex=False)\
                      .str.strip()\
                      .str.lower()\



#plot survey points
plt.scatter(df["easting"], df("nothing"])
plt.title("land survey map")
plt.xlabel("Easting")
plt.ylabel("Northing")
plt.grid()
plt.show()

                
