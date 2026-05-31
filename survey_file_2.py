Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

== RESTART: C:\Users\hp\AppData\Local\Programs\Python\Python312\survey_work.py =
  name   code      easting     northing  height
0  PT3  TBM 1  552259.2208  711597.7376  2.9056
1  PT4  TBM 2  552229.2222  711602.4282  3.0913
2  PT5  TBM 3  552224.6523  711614.1755  3.1762
3  PT6     Wf  552223.5226  711589.8118  2.7054
4  PT7     GL  552257.2591  711623.2985  2.7559
Distance between first two points = 30.36 meters
point 114 to point 115 = 36.12 meters
Total Survey Line distance = nan meters
df["easting"] = pd.to_numeric(df["easting"], errors="coerce")
df["northing"] = pd.to_numeric(df["northing"], errors="corce")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    df["northing"] = pd.to_numeric(df["northing"], errors="corce")
  File "C:\Users\hp\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\tools\numeric.py", line 183, in to_numeric
    raise ValueError("invalid error value specified")
ValueError: invalid error value specified
df["northing"] = pd.to_numeric(df["northing"], errots="coerce")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    df["northing"] = pd.to_numeric(df["northing"], errots="coerce")
TypeError: to_numeric() got an unexpected keyword argument 'errots'
df["northing"] = pd.to_numeric(df["northing"], errors="coerce")
df = df.dropna(subset=["easting", "morthing"])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    df = df.dropna(subset=["easting", "morthing"])
  File "C:\Users\hp\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\frame.py", line 7789, in dropna
    raise KeyError(np.array(subset)[check].tolist())
KeyError: ['morthing']
df = df.dropna (subset=["easing", "northing"])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    df = df.dropna (subset=["easing", "northing"])
  File "C:\Users\hp\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\frame.py", line 7789, in dropna
    raise KeyError(np.array(subset)[check].tolist())
KeyError: ['easing']
df = df.dropna(subset=["easting", "northing"])
import math
total_distance =
SyntaxError: invalid syntax
total_distance = 0
for i in range(len(df)-1):
    x1 = df["easting"][i]
    y1= df["northing"][i]
    x2 = df["easting"][i+1]
    y2 = df["northing"][i+1]
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    total += d

    
Traceback (most recent call last):
  File "<pyshell#17>", line 7, in <module>
    total += d
NameError: name 'total' is not defined
total_distance += d
print("Total Survey Line distance:", round(total_distance, 2), "meters")
Total Survey Line distance: 30.36 meters
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import as Axes3D
SyntaxError: invalid syntax
from mpl_toolkits.mplot3d import Axes3D
>>> df["easting"] = pd.to_numeric(df)["easting"], errors="coerce")
SyntaxError: unmatched ')'
>>> df["easting"] = pd.to_numeric(df["easting"], errors="coerce")
>>> df["northing"] = pd.to_numeric(df["northing"], errors="coerce")
>>> df["height"] = pd.to_numeric(df["height"], errors="coerce")
>>> df = df.dropna(subset=["easting", "northing", "height"])
>>> fig = plt.figure()
>>> ax = fig.add_subplot(111, projection='3d')
>>> ax.scatter(
...     df["easting"],
...     df["northing'],
...        
SyntaxError: unterminated string literal (detected at line 3)
>>> ax.scatter(
...     df["easting"]
...     df["northing"]
...     
SyntaxError: '(' was never closed
>>> ax.scatter(
...     df["easting"],
...     df["northing"],
...     df["height"]
...     )
...     
<mpl_toolkits.mplot3d.art3d.Path3DCollection object at 0x0000022ADC47EBD0>
>>> ax.set_xlabel("easting")
...     
Text(0.5, 0, 'easting')
>>> ax.set_ylabel("northing")
...     
Text(0.5, 0.5, 'northing')
>>> ax.set_zlabel("height")
...     
Text(0.5, 0, 'height')
>>> plt.title("3D Terrain Model")
...     
Text(0.5, 0.92, '3D Terrain Model')
>>> plt.savefig("3d_terrain_png")
...     
>>> plt.show()
...     
