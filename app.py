import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
from shiny import reactive, render
import pandas as pd
from pathlib import Path

# Load the CSV data file (replace with your actual path)
df = pd.read_csv(Path(__file__).parent / "episodes.csv")

# Inspect the data (optional)
print(df.head())
with ui.sidebar():
    ui.input_selectize(  
        "selected_features",  
        "Select Features:",  
        {"TREE": "Tree", "CLOUDS": "Cloud", "MOUNTAIN": "Mountain"},  
        multiple=True, 
    )
    ui.input_slider("season_range", "Season", min=1, max=15, value=[1, 15])  

@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.n(), density=True)

with ui.card(full_screen=True):
    ui.card_header("Selected Features")
    features = ""
    @render.text  
    def text():
        return str(input.selected_features())

@render.table
def episode_table():
    # Get selected features from input
    selected_features = input.selected_features()

    if selected_features:
        # Filter the dataframe based on selected features
        filtered_df = df[df[selected_features].any(axis=1)]
    else:
        # If no features are selected, show all data
        filtered_df = df
    
    return filtered_df


    
