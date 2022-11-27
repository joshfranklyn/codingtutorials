# %%
import numpy as np
import matplotlib.pyplot as plt

plt.plot(np.linspace(0, 10))
# %%

path = "C:\\Users\\Josh\\Downloads\\WCC_Suburb_Boundaries.geojson"
import geopandas as gpd

gdf = gpd.read_file(path)

# %%
import contextily as cx
fig, ax = plt.subplots(figsize=(10, 10))

gdf = gdf[gdf['suburb'] == 'Newtown']

gdf = gdf.to_crs('EPSG:2193')
gdf.plot(ax=ax, edgecolor='black', alpha=0.4)


geom = list(gdf['geometry'])
for i, name in enumerate(list(gdf['suburb'])):
    centroid = geom[i].centroid
    ax.text(x=centroid.x, y=centroid.y, s=name, size=8)

cx.add_basemap(ax, crs='EPSG:2193', source=cx.providers.OpenStreetMap.Mapnik)

ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Map of Wellington Suburbs')

'''

path = "C:\\Users\\Josh\\Downloads\\kx-nz-building-outlines-GPKG\\nz-building-outlines.gpkg"

buildings = gpd.read_file(path)

buildings_newtown = gpd.clip(buildings, gdf)

buildings_newtown.plot(ax=ax, color='purple', alpha=0.5)

'''
# %%
print("hi")
# %%
