import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`
countries_list = ["Brazil", "China", "India", "United States", "United Kingdom", "Germany"]

def clean_data(covid_df):
    columns = ["date", "location", "total_cases_per_million", "total_deaths_per_million", "population_density", "population", "gdp_per_capita"]
    covid_df = covid_df[columns]
    covid_df = covid_df[covid_df["location"].isin(countries_list)]
    covid_df = covid_df.dropna()
    
    return covid_df


def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart
    covid_df = pd.read_csv("data/covid_data.csv")
    covid_df = clean_data(covid_df)
    covid_df.sort_values('date', inplace=True)
    
    graph_one = []    
    graph_two = []
    for country in countries_list:
      x_val = covid_df[covid_df['location'] == country].date.tolist()
      y_val_graph_one = covid_df[covid_df['location'] == country].total_cases_per_million.tolist()
      graph_one.append(
          go.Scatter(
          x = x_val,
          y = y_val_graph_one,
          mode = 'lines',
          name = country
          )
      )
    
      y_val_graph_two = covid_df[covid_df['location'] == country].total_deaths_per_million.tolist()
      graph_two.append(
          go.Scatter(
          x = x_val,
          y = y_val_graph_two,
          mode = 'lines',
          name = country
          )
      )
          
    layout_one = dict(title = 'Total Cases per Million in 2020',
                xaxis = dict(title = 'Date'),
                yaxis = dict(title = 'Total Cases per Million'),
                )

    layout_two = dict(title = 'Total Deaths per Million in 2020',
                xaxis = dict(title = 'Date'),
                yaxis = dict(title = 'Total Deaths per Million')
                       )

# second chart plots ararble land for 2015 as a bar chart    
    graph_three = []
    covid_df.sort_values('population_density', ascending=False, inplace=True)
    graph_three.append(
      go.Bar(
      x = covid_df.location.tolist(),
      y = covid_df.population_density.tolist(),
      )
    )

    layout_three = dict(title = 'Countries Population Density',
                xaxis = dict(title = 'Countries',),
                yaxis = dict(title = 'Population Density'),
                )
    
    graph_four = []
    covid_df.sort_values('gdp_per_capita', ascending=False, inplace=True)
    graph_four.append(
      go.Bar(
      x = covid_df.location.tolist(),
      y = covid_df.gdp_per_capita.tolist(),
      )
    )

    layout_four = dict(title = 'Countries GDP per Capita',
                xaxis = dict(title = 'Countries',),
                yaxis = dict(title = 'GDP per Capita'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures