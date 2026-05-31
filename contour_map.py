Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.tri as tri
df = pd.read_csv(r"c:\Users\hp\Desktop\XYZ_for_C_and_I_Leasing_Survey.csv", sep= "\t")
df.columns = df.columns.str.strip().str.lower()
df["easting"] = pd.to_numeric(df["easting"], errors="coerce")
df{"northing"] = pd.read_numeric(df["northing"], errors="coerce")
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
df["northing"] = pd._read_numeric(df["northing"], errors="coerce")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    df["northing"] = pd._read_numeric(df["northing"], errors="coerce")
AttributeError: module 'pandas' has no attribute '_read_numeric'
df["northing"] = pd.read_numeric(df[" northing"], errors="coerce")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    df["northing"] = pd.read_numeric(df[" northing"], errors="coerce")
AttributeError: module 'pandas' has no attribute 'read_numeric'. Did you mean: 'to_numeric'?
df["northing"] = pd.to_numeric(df["northing"], errors="coerce")
df["height"] = pd.to_numeric(df["height"], errors="coerce")
df = df.dropna()
plt.figure(figsize= (8.6))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    plt.figure(figsize= (8.6))
  File "C:\Users\hp\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\pyplot.py", line 1041, in figure
    manager = new_figure_manager(
  File "C:\Users\hp\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\pyplot.py", line 551, in new_figure_manager
    return _get_backend_mod().new_figure_manager(*args, **kwargs)
  File "C:\Users\hp\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\backend_bases.py", line 3503, in new_figure_manager
    fig = fig_cls(*args, **kwargs)
  File "C:\Users\hp\AppData\Local\Programs\Python\Python312\Lib\site-packages\matplotlib\figure.py", line 2633, in __init__
    self.bbox_inches = Bbox.from_bounds(0, 0, *figsize)
TypeError: Value after * must be an iterable, not float
>>> plt.figure(figsize= (8, 6))
<Figure size 800x600 with 0 Axes>
>>> triang = tri.triangulation(df["easting"], df["northing"])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    triang = tri.triangulation(df["easting"], df["northing"])
AttributeError: module 'matplotlib.tri' has no attribute 'triangulation'. Did you mean: 'Triangulation'?
>>> triang = tri.Triangulation(df["easting"], df["northing"])
>>> plt.figure(figsize= (8, 6))
<Figure size 800x600 with 0 Axes>
>>> plt.tricontour(triang, df["height"], levels=10)
<matplotlib.tri._tricontour.TriContourSet object at 0x0000019165063050>
>>> plt.tricontourf(triang, df["height"], levels=10)
<matplotlib.tri._tricontour.TriContourSet object at 0x000001916520FCE0>
>>> plt.colorbar(label="Elevation (m)")
<matplotlib.colorbar.Colorbar object at 0x00000191650DB7A0>
>>> plt.xlabel("easting")
Text(0.5, 0, 'easting')
>>> plt.ylabel("northing")
Text(0, 0.5, 'northing')
>>> plt.title("Contour Map of Survey Terrain")
Text(0.5, 1.0, 'Contour Map of Survey Terrain')
>>> plt.savefig("contour_map.png)
...             
SyntaxError: unterminated string literal (detected at line 1)
>>> plt.savefig("contour_map.png")
...             
>>> plt.show()
...             
