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

    fig.update_layout(
        updatemenus=[
            dict(
            buttons=list([
                dict(
                    args=["media", "00"],
                    label="Vue générale",
                    method="restyle"
                ),
                dict(
                    args=["media", "01"],
                    label="24heures",
                    method="restyle"
                ),
                dict(
                    args=["media", "02"],
                    label="BFMTV",
                    method="restyle"
                ),
                dict(
                    args=["media", "03"],
                    label="FRANCE 24",
                    method="restyle"
                ),
                dict(
                    args=["media", "04"],
                    label="L'Orient-Le Jour \ud83d\uddde",
                    method="restyle"
                ),
                dict(
                    args=["media", "05"],
                    label="LCI",
                    method="restyle"
                ),
                dict(
                    args=["media", "06"],
                    label="La Presse",
                    method="restyle"
                ),
                dict(
                    args=["media", "07"],
                    label="La Voix du Nord",
                    method="restyle"
                ),
                dict(
                    args=["media", "08"],
                    label="LaLibre.be",
                    method="restyle"
                ),
                dict(
                    args=["media", "09"],
                    label="Le Dauphin\u00e9 Lib\u00e9r\u00e9",
                    method="restyle"
                ),
                dict(
                    args=["media", "10"],
                    label="Le Devoir",
                    method="restyle"
                ),
                dict(
                    args=["media", "11"],
                    label="Le Figaro \ud83d\uddde",
                    method="restyle"
                ),
                dict(
                    args=["media", "12"],
                    label="Le Journal de Montr\u00e9al",
                    method="restyle"
                ),
                dict(
                    args=["media", "13"],
                    label="Le Matin",
                    method="restyle"
                ),
                dict(
                    args=["media", "14"],
                    label="Le Monde",
                    method="restyle"
                ),
                dict(
                    args=["media", "15"],
                    label="Le Monde Afrique",
                    method="restyle"
                ),
                dict(
                    args=["media", "16"],
                    label="Le Soir",
                    method="restyle"
                ),
                dict(
                    args=["media", "17"],
                    label="Le Soleil de Que\u0301bec",
                    method="restyle"
                ),
                dict(
                    args=["media", "18"],
                    label="Le Temps",
                    method="restyle"
                ),
                dict(
                    args=["media", "19"],
                    label="Lib\u00e9ration",
                    method="restyle"
                ),
                dict(
                    args=["media", "20"],
                    label="Mediapart",
                    method="restyle"
                ),
                dict(
                    args=["media", "21"],
                    label="Ouest-France",
                    method="restyle"
                ),
                dict(
                    args=["media", "22"],
                    label="RTBF",
                    method="restyle"
                ),
                dict(
                    args=["media", "23"],
                    label="RTL",
                    method="restyle"
                ),
                dict(
                    args=["media", "24"],
                    label="RTL info",
                    method="restyle"
                ),
                dict(
                    args=["media", "25"],
                    label="RTS - Radio T\u00e9l\u00e9vision Suisse",
                    method="restyle"
                ),
                dict(
                    args=["media", "26"],
                    label="Radio France Internationale",
                    method="restyle"
                ),
                dict(
                    args=["media", "27"],
                    label="Radio-Canada Information",
                    method="restyle"
                ),
                dict(
                    args=["media", "28"],
                    label="SudOuest",
                    method="restyle"
                ),
                dict(
                    args=["media", "29"],
                    label="TF1 Le JT",
                    method="restyle"
                ),
                dict(
                    args=["media", "30"],
                    label="TVA Nouvelles",
                    method="restyle"
                ),
                dict(
                    args=["media", "31"],
                    label="Tribune de Gen\u00e8ve",
                    method="restyle"
                ),
                dict(
                    args=["media", "32"],
                    label="franceinfo",
                    method="restyle"
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