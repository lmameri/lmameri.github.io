import preprocess
import plotly.graph_objects as go

style = "<span>Date de publication: </span>" + \
        "<b>%{x} </b>" +  "<br><span>Mot-clé: : </span>" + \
        "<b>%{y}</b>" + "<br><span>Nombre: </span>" + \
        "<b>%{z} </b>" +  "<extra></extra>"

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
                    hoverongaps = False,colorscale='sunset',
                    hovertemplate = "Année : %{x} <br>Média : %{y} </br>Nombre de publications : %{z}<extra></extra>"))
    
    # Add heatmap monthly traces for each year
    for year in data.columns.to_list():
        fig.add_trace(go.Heatmap(visible=False,
                        z=preprocess.get_nbpubs_monthly(df, year,medias).values,
                        x=months,
                        y=medias,
                        hoverongaps = False,colorscale='sunset',
                        hovertemplate = "Mois : %{x} <br>Média : %{y} </br>Nombre de publications : %{z}<extra></extra>"))

    fig.update_yaxes(tickvals=medias)
    fig.update_layout(title='Nombre de publications par média par année')
    
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="down",
                x=1.25,
                y=1,
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
    fig.update_layout(dragmode=False,xaxis_title="Période de publication",yaxis_title="Médias")
    return fig


def get_heatmap_keywords(data_heatmap_bykeywords,data_heatmap_bytime):
    fig = go.Figure()

    title_map = 'Métriques du TOP 50 des mots clés'

    trace_heatmap=go.Heatmap(customdata= ['by_keywords'],
                            z=data_heatmap_bykeywords['nb_likes'], 
                            x=data_heatmap_bykeywords['date'], 
                            y=data_heatmap_bykeywords['mot'],
                            colorscale='sunset', hovertemplate=style, hoverongaps=False)


    fig.add_trace(trace_heatmap)
    

    fig.update_layout(
        updatemenus=[
                       dict(
                type="buttons",
                direction="left",
                x=0.5,
                y=1.05,
                showactive=True,
                buttons=list(
                    [
                        dict(
                            label="Par score TF IDF",
                            method="update",
                            args=[{"customdata": ['by_keywords'], "z": [data_heatmap_bykeywords['nb_likes']] , "x": [data_heatmap_bykeywords['date']] , "y": [data_heatmap_bykeywords['mot']]}],
                        ),
                        dict(
                            label="Par ordre d'apparition dans le temps",
                            method="update",
                             args=[{"customdata": ['by_date'], "z": [data_heatmap_bytime['nb_likes']] , "x": [data_heatmap_bytime['date']] , "y": [data_heatmap_bytime['mot']]}],
                        ),
                       
                    ]
                ),
            ),
            dict(
                type="buttons",
                direction="left",
                x=1,
                y=1.05,
                showactive=True,
                buttons=list(
                    [
                        dict(
                            label="Nombre de likes",
                            method="update",
                            args=[{"z": [update_zaxis_likes(fig,data_heatmap_bykeywords,data_heatmap_bytime)]}],
                        ),
                        dict(
                            label="Nombre de commentaires",
                            method="update",
                            args=[{"z": [update_zaxis_comments(fig, data_heatmap_bykeywords, data_heatmap_bytime)]}],
                        ),
                        dict(
                            label="Nombre de vues",
                            method="update",
                            args=[{"z": [update_zaxis_views(fig, data_heatmap_bykeywords, data_heatmap_bytime)]}],
                        ),
                       
                    ]
                ),
            ),

        ]
    )

    fig.update_layout(xaxis_title="Date de publication",yaxis_title="Mots clés",
    annotations=[
        dict(text="Métriques : ", x=0.6, xref="paper", y=1.04, yref="paper",
                             align="left", showarrow=False),
        dict(text="Classement des mots clés : ", x=0, xref="paper", y=1.04, yref="paper",
                             align="left", showarrow=False),
    ])

    fig.update_layout(dragmode=False, plot_bgcolor='rgba(0, 0, 0,0)', xaxis=dict(showgrid=False,  zeroline=False), yaxis=dict(showgrid=True,  zeroline=False),
    height=1000)
    fig.update_layout(title=title_map)

    return fig

def update_zaxis_likes(fig,data_heatmap_bykeywords,data_heatmap_bytime):
    if(fig['data'][0]['customdata'][0] == 'by_keywords'):
        return data_heatmap_bykeywords['nb_likes']
    if(fig['data'][0]['customdata'][0] == 'by_date'):
        return data_heatmap_bytime['nb_likes']

def update_zaxis_comments(fig,data_heatmap_bykeywords,data_heatmap_bytime):
    if(fig['data'][0]['customdata'][0] == 'by_keywords'):
        return data_heatmap_bykeywords['nb_commentaires']
    if(fig['data'][0]['customdata'][0] == 'by_date'):
        return data_heatmap_bytime['nb_commentaires']

def update_zaxis_views(fig,data_heatmap_bykeywords,data_heatmap_bytime):
    if(fig['data'][0]['customdata'][0] == 'by_keywords'):
        return data_heatmap_bykeywords['nb_vues']
    if(fig['data'][0]['customdata'][0] == 'by_date'):
        return data_heatmap_bytime['nb_vues']



#'rgb(243, 231, 155)'
