import plotly.express as px
import preprocess
import plotly.graph_objects as go

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
    fig = go.Figure(data=go.Heatmap(
                    z=[[1, None, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                    y=['Morning', 'Afternoon', 'Evening'],
                    hoverongaps = False))
    return fig


def get_heatmap_keywords(metric, df):
    if(metric == 'likes'):
        temp = df['nb_likes']
        title_map = 'Nombre de likes pour les mots les plus fréquents'
    if(metric == 'commentaires'):
         temp = df['nb_commentaires']
         title_map = 'Nombre de commentaires pour les mots les plus fréquents'
    if(metric == 'vues'):
        temp = df['nb_vues']
        title_map = 'Nombre de vues pour les mots les plus fréquents'
    fig = go.Figure(data=go.Heatmap(z=temp.fillna(0), x=df['date'], y=df['mot'],colorscale='sunset'))
    fig.update_layout(title=title_map, plot_bgcolor='rgba(0, 0, 0,0)',
    xaxis=dict(showgrid=False,  zeroline=False),
        yaxis=dict(showgrid=False,  zeroline=False),)
    return fig


#'rgb(243, 231, 155)'