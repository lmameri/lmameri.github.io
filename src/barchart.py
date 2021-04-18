import plotly.express as px
import preprocess
import plotly.graph_objects as go

def get_barchart(df_photo,df_video,df_album,df_igtv):
    fig = go.Figure(data=[
    go.Bar(name='Photo', x=df_photo['date'], y=df_photo['count']),
    go.Bar(name='Video',x=df_video['date'], y=df_video['count']),
    go.Bar(name='Album', x=df_album['date'], y=df_album['count']),
    go.Bar(name='IGTV', x=df_igtv['date'], y=df_igtv['count'])
    ])

    fig.update_layout(barmode='stack', title='Fréquence de publication')
    
    return fig