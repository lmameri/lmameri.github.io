import plotly.graph_objects as go
import preprocess
import plotly.graph_objects as go

def get_heatmap_yearly(data,df):
    years = data.columns.to_list()
    years = [str(year) for year in years]
    medias= data.index.to_list()
    months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Jui', 'Aou', 'Sep', 'Oct', 'Nov', 'Déc' ]
    data = data.reindex(index=data.index[::-1])
    # create figure
    fig = go.Figure()

    # Add heatmap yearly trace
    fig.add_trace(go.Heatmap(visible=True,
                    z=data.values,
                    x=years,
                    y=medias,
                    hoverongaps = False,colorscale='Reds'))
    
    
    # Add heatmap monthly traces for each year
    for year in data.columns.to_list()[1:]:
        fig.add_trace(go.Heatmap(visible=False,
                        z=preprocess.get_nbpubs_monthly(df, year,medias).values,
                        x=months,
                        y=medias,
                        hoverongaps = False,colorscale='Reds'))
    
    fig.update_yaxes(tickvals=medias)
    fig.update_layout(title='Nombre de publications par média par année')

    
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                x=0.7,
                y=1.2,
                showactive=True,
                buttons=list(
                    [
                        dict(
                            label="Toutes les années",
                            method="update",
                            args=[{"visible": [True, False, False, False, False, False, False,False,False,False,False]}],
                        ),
                        dict(
                            label="2011",
                            method="update",
                            args=[{"visible":  [False, True, False, False, False, False, False,False,False,False,False]}],
                        ),
                        dict(
                            label="2012",
                            method="update",
                            args=[{"visible":  [False, False, True, False, False, False, False,False,False,False,False]}],
                        ),
                        dict(
                            label="2013",
                            method="update",
                            args=[{"visible":  [False, False, False, True, False, False, False,False,False,False,False]}],
                        ),
                        dict(
                            label="2014",
                            method="update",
                            args=[{"visible":  [False, False, False, False, True, False, False,False,False,False,False]}],
                        ),
                        dict(
                            label="2015",
                            method="update",
                            args=[{"visible":  [False, False, False, False, False, True, False,False,False,False,False]}],
                        ),
                        dict(
                            label="2016",
                            method="update",
                            args=[{"visible":  [False, False, False, False, False, False, True,False,False,False,False]}],
                        ),
                        dict(
                            label="2017",
                            method="update",
                            args=[{"visible":  [False, False, False, False, False, False, False,True,False,False,False]}],
                        ),
                        dict(
                            label="2018",
                            method="update",
                            args=[{"visible":  [False, False, False, False, False, False, False,False,True,False,False]}],
                        ),
                        dict(
                            label="2019",
                            method="update",
                            args=[{"visible":  [False, False, False, False, False, False, False,False,False,True,False]}],
                        ),
                        dict(
                            label="2020",
                            method="update",
                            args=[{"visible":  [False, False, False, False, False, True, False,False,False,False,True]}],
                        ),
                    ]
                ),
            )
        ]
    )
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
