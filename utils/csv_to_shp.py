import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Load CSV file
df = pd.read_csv("data/housing.csv")

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(
    df.drop(['longitude', 'latitude'], axis=1),  # Remove the original longitude and latitude columns
    geometry=[Point(xy) for xy in zip(df.longitude, df.latitude)],  # Create geometry column
    crs="EPSG:4326"  # Set coordinate reference system
)

# Export to Shapefile
gdf.to_file("data/housing_data_with_attributes.shp")

# To verify data
print(gdf.head())
