import plotly.express as px
import preprocess
import plotly.graph_objects as go
import hovertemplate
import pandas as pd

df_insta = pd.read_csv('src/data/poly-Instagram-2011-2020.csv')
media_list=df_insta['compte'].unique()

COLORS = ['rgb(243, 231, 155)', 'rgb(248, 160, 126)', 'rgb(206, 102, 147)', 'rgb(92, 83, 165)']

def get_barchart():
    fig = go.Figure()

    df_photo,df_video,df_album,df_igtv = preprocess.preprocess_barchart()

    fig.add_traces([
    go.Bar( hovertemplate= hovertemplate.get_hovertemplate_barchart(), visible= True, name='Photo', x=df_photo['date'], y=df_photo['count'], marker={'color': COLORS[0]}),
    go.Bar(hovertemplate= hovertemplate.get_hovertemplate_barchart(), visible= True,name='Video',x=df_video['date'], y=df_video['count'], marker={'color': COLORS[1]}),
    go.Bar(hovertemplate= hovertemplate.get_hovertemplate_barchart(),visible= True,name='Album', x=df_album['date'], y=df_album['count'],marker={'color': COLORS[2]}),
    go.Bar(hovertemplate= hovertemplate.get_hovertemplate_barchart(),visible= True,name='IGTV', x=df_igtv['date'], y=df_igtv['count'],marker={'color': COLORS[3]})
    ])
    
    button_list = []

    button_list.append(dict(
        args=[{'visible': [True]*4 + [False] * 128}], label='Vue générale', method='update'
    ))
    
    for media in media_list:
        df_photo,df_video,df_album,df_igtv = preprocess.preprocess_barchart_account(media)
        fig.add_traces([
            go.Bar( hovertemplate= hovertemplate.get_hovertemplate_barchart(),visible= False,name='Photo', x=df_photo['date'], y=df_photo['count'],marker={'color': COLORS[0]}),
            go.Bar(hovertemplate= hovertemplate.get_hovertemplate_barchart(),visible= False,name='Video',x=df_video['date'], y=df_video['count'],marker={'color': COLORS[1]}),
            go.Bar(hovertemplate= hovertemplate.get_hovertemplate_barchart(),visible= False,name='Album', x=df_album['date'], y=df_album['count'],marker={'color': COLORS[2]}),
            go.Bar(hovertemplate= hovertemplate.get_hovertemplate_barchart(),visible= False,name='IGTV', x=df_igtv['date'], y=df_igtv['count'],marker={'color': COLORS[3]})])
    
    for i in range(1, len(media_list)+1):
        temp = [False] * 132
        temp[i*4 : i*4+3] = [True,True,True,True]
        button_list.append(dict(
            args=[{'visible': temp}], label=media_list[i-1], method='update'
        ))

    fig.update_layout(
        updatemenus=[
            dict(buttons=button_list, direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=1,
            xanchor="left",
            y=0.5,
            yanchor="top"
            ),          
        ])

    fig.update_layout(
    barmode='stack', title='Fréquence de publication des médias francophones',legend_title="Type de plublication",
    xaxis_title="Date de publication",yaxis_title="Fréquence de publication",
    annotations=[
        dict(text="Liste des médias", x=1.1, xref="paper", y=0.6, yref="paper",
                             align="left", showarrow=False),
    ])
    return fig