import plotly.graph_objs as go
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from utils import twminer
# Create instance of Dash object
app = dash.Dash()
# Layout of a web app containing dcc and html objects that yield HTML elements
app.layout = html.Div([
    html.H1(
        children='Twittometer',
        style={'textAlign': 'center','family':'Arial'}
        ),
    dcc.Input(id = 'in_keyword',
              placeholder='type a search term...',
              value = 'FDA',
              type = 'text',
              size = '50'),
    html.Button('search', id='button_search'),
    dcc.Graph(id = 'graph_sentiments')
], style = {'font-family':'Arial'})
# Decorator to program interaction between different web app elements
@app.callback(
    Output('graph_sentiments', 'figure'),
    [Input('button_search', 'n_clicks')],
    [State('in_keyword', 'value')])
# Function called to search for keyword and update the histogram
def take_temperature(n_clicks, value):
    """Get histogram for 1000 or less tweets found for a given keyword"""
    # Get tweets and sentiments for a given keyword
    twresults = twminer(value, 1000)
    # Get number of tweets (can be less than 1000)
    twcount = len(twresults['twt_number'])
    # Create a trace for a histogram with 10 bins for tweet sentiments
    traces = [go.Histogram(
        x = twresults['twt_polarity'],
        nbinsx = 10)]
    # Return dictionary with parameters to update the graph
    return {'data': traces,
        'layout': go.Layout(
            title = (f"Sentiments for {twcount} tweets for {value}"),
            xaxis = {'title': 'sentiments polarity'},
            yaxis = {'title': 'number of tweets'},
            hovermode = 'closest'
        )
    }
if __name__ == '__main__':
    app.run_server()