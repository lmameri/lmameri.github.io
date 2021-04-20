import plotly.express as px
import preprocess
import plotly.graph_objects as go


def get_funnel(df):
    fig = go.Figure(go.Funnel(
    y = df['mot'],
    x = df['nb_occurences']))

    fig.update_layout(height=1000)
    return fig