import plotly.graph_objects as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import plotly.express as px

# read and extract longitude, latitude, altitude, and e_density from ISS data
df = pd.read_csv("ISS_SP_FPMU_20200911_20200912_20200913_20200914_half.csv")
# df = df[df["SUNLIGHT_%"] != 0]
latitude = df.iloc[:,1].values   #float64
longitude = df.iloc[:,2].values
altitude = df.iloc[:,3].values
e_density = df.iloc[:,4].values

# making the plot
fig = go.Figure(go.Scattergeo(
        lon = longitude,
        lat = latitude,
        mode = 'markers',
        marker = dict(
            size = 15,
            opacity = 0.08,
            reversescale = True,
            autocolorscale = False,

            colorscale = 'hot',
            cmin = 1e+10,
            color = e_density,
            cmax = e_density.max(),
            colorbar_title="Electron density [m-3]"
        )
))
fig.update_geos(projection_type="orthographic")

fig.update_layout(width= 1000, height=600, margin={"r":0,"t":0,"l":0,"b":0})
fig.write_html("index.html")
fig.show()
