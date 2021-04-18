import plotly.express as px
import preprocess
import plotly.graph_objects as go


def get_funnel(df):
    fig = go.Figure(go.Funnel(
    y = df['mot'],
    x = df['count']))
    return fig