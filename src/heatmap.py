import plotly.express as px
import preprocess


def get_heatmap_yearly(data):
    
    fig = px.imshow(data,
                    labels=dict(color="Publications", x='', y=''),
                    x=data.columns.values,
                    y=data.index.values, color_continuous_scale='Reds', title='Nombre de publications Instagram par médias par année'
                    )
    fig.update_xaxes(tickvals=data.columns.values)
    fig.update_yaxes(tickvals=data.index.values)
    return fig

def get_heatmap_test():
    import plotly.graph_objects as go

    fig = go.Figure(data=go.Heatmap(
                    z=[[1, None, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                    y=['Morning', 'Afternoon', 'Evening'],
                    hoverongaps = False))
    return fig