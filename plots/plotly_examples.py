"""
Various plotly graphs taken from examples on the plotly website.
See: https://plotly.com/python/maps/
"""

import os

import geopandas as gpd
import plotly.express as px


def scatter_plot_geopandas():
    """
    Creates a scatter plot map of cities in the world using code copied from here:
    https://plotly.com/python/scattermapbox/#:~:text=peak_hour-,Basic%20Example%20with%20GeoPandas,-px.scatter_mapbox%20can
    """

    # Get the data that we want to plot
    geo_df = gpd.read_file(gpd.datasets.get_path("naturalearth_cities"))
    # Make the scatter plot using this data
    fig = px.scatter_geo(geo_df,
                         lat=geo_df.geometry.y,
                         lon=geo_df.geometry.x,
                         hover_name="name")

    # Output this plot to a html file in the current working directory, i.e. /plots/scatter_geopandas.html
    output_file = os.path.join(os.getcwd(), "scatter_geopandas.html")
    fig.write_html(output_file)


if __name__ == "__main__":
    print("Creating plotly examples...")
    scatter_plot_geopandas()
