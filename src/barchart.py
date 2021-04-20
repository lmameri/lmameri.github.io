import plotly.express as px
import preprocess
import plotly.graph_objects as go
import pandas as pd

df_insta = pd.read_csv('src/data/poly-Instagram-2011-2020.csv')
media_list=df_insta['compte'].unique()

def get_barchart():
    fig = go.Figure()

    df_photo,df_video,df_album,df_igtv = preprocess.preprocess_barchart()

    fig.add_traces([
    go.Bar( visible= True, name='Photo', x=df_photo['date'], y=df_photo['count']),
    go.Bar(visible= True,name='Video',x=df_video['date'], y=df_video['count']),
    go.Bar(visible= True,name='Album', x=df_album['date'], y=df_album['count']),
    go.Bar(visible= True,name='IGTV', x=df_igtv['date'], y=df_igtv['count'])
    ])
    

    for media in media_list:
        df_photo,df_video,df_album,df_igtv = preprocess.preprocess_barchart_account(media)
        fig.add_traces([
            go.Bar( visible= False,name='Photo', x=df_photo['date'], y=df_photo['count']),
            go.Bar(visible= False,name='Video',x=df_video['date'], y=df_video['count']),
            go.Bar(visible= False,name='Album', x=df_album['date'], y=df_album['count']),
            go.Bar(visible= False,name='IGTV', x=df_igtv['date'], y=df_igtv['count'])])
            
    fig.update_layout(barmode='stack', title='Fréquence de publication')
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
            y=0.8,
            yanchor="top"
            ),
            
        ])
    return fig