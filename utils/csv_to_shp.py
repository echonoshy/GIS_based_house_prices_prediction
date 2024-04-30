import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# 读取 CSV 文件
df = pd.read_csv("data/housing.csv")

# 创建 GeoDataFrame
gdf = gpd.GeoDataFrame(
    df.drop(['longitude', 'latitude'], axis=1),  # 移除原始经纬度列
    geometry=[Point(xy) for xy in zip(df.longitude, df.latitude)],  # 创建几何列
    crs="EPSG:4326"  # 设置坐标参考系统
)

# 导出为 Shapefile
gdf.to_file("data/housing_data_with_attributes.shp")

# 如果需要验证或查看数据
print(gdf.head())
