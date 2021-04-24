import plotly.express as px
import preprocess
import plotly.graph_objects as go
import pandas as pd

df_insta = pd.read_csv('src/data/poly-Instagram-2011-2020.csv')
media_list=df_insta['compte'].unique()

COLORS = ['rgb(243, 231, 155)', 'rgb(248, 160, 126)', 'rgb(206, 102, 147)', 'rgb(92, 83, 165)']

style = "<span>Date de publication: </span>" + \
        "<b>%{x} </b>" +  "<br><span>Nombre de publication: : </span>" + \
        "<b>%{y}</b>" +  "<extra></extra>"

def get_barchart():
    fig = go.Figure()

    df_photo,df_video,df_album,df_igtv = preprocess.preprocess_barchart()

    fig.add_traces([
    go.Bar( hovertemplate= style, visible= True, name='Photo', x=df_photo['date'], y=df_photo['count'], marker={'color': COLORS[0]}),
    go.Bar(hovertemplate= style, visible= True,name='Video',x=df_video['date'], y=df_video['count'], marker={'color': COLORS[1]}),
    go.Bar(hovertemplate= style,visible= True,name='Album', x=df_album['date'], y=df_album['count'],marker={'color': COLORS[2]}),
    go.Bar(hovertemplate= style,visible= True,name='IGTV', x=df_igtv['date'], y=df_igtv['count'],marker={'color': COLORS[3]})
    ])
    

    for media in media_list:
        df_photo,df_video,df_album,df_igtv = preprocess.preprocess_barchart_account(media)
        fig.add_traces([
            go.Bar( hovertemplate= style,visible= False,name='Photo', x=df_photo['date'], y=df_photo['count'],marker={'color': COLORS[0]}),
            go.Bar(hovertemplate= style,visible= False,name='Video',x=df_video['date'], y=df_video['count'],marker={'color': COLORS[1]}),
            go.Bar(hovertemplate= style,visible= False,name='Album', x=df_album['date'], y=df_album['count'],marker={'color': COLORS[2]}),
            go.Bar(hovertemplate= style,visible= False,name='IGTV', x=df_igtv['date'], y=df_igtv['count'],marker={'color': COLORS[3]})])

    fig.update_layout(
        updatemenus=[
            dict(
            buttons=list([
                dict(
                    args=[{"visible":  [True, True,True,True, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label="Vue générale",
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, True, True,True,True, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[0],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[1],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[2],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[3],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[4],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[5],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[6],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[7],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[8],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[9],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[10],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[11],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[12],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[13],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[14],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[15],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[16],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[17],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[18],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[19],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[20],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[21],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[22],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[23],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[24],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[25],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[26],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[27],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False,False, False,False,False]}],
                    label=media_list[28],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False,False, False,False,False]}],
                    label=media_list[29],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True,False, False,False,False]}],
                    label=media_list[30],
                    method="update"
                ),
                dict(
                    args=[{"visible":  [False, False,False,False, False, False,False,False, False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,False, False,False,False,True, True,True,True]}],
                    label=media_list[31],
                    method="update"
                )
            ]),
            direction="down",
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