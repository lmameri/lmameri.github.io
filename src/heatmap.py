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


def get_heatmap_keywords(data_heatmap_bykeywords,data_heatmap_bytime):
    fig = go.Figure()

    title_map = 'Métriques pour les mots les plus fréquents'
    fig.add_traces(go.Heatmap(customdata= ['by_keywords'],z=data_heatmap_bykeywords['nb_likes'], x=data_heatmap_bykeywords['date'], y=data_heatmap_bykeywords['mot'],colorscale='sunset'))
    
    fig.update_layout(
        updatemenus=[
                       dict(
                type="buttons",
                direction="left",
                x=0.2,
                y=1.05,
                showactive=True,
                buttons=list(
                    [
                        dict(
                            label="Affichage par mots clés",
                            method="update",
                            args=[{"customdata": ['by_keywords'], "z": [data_heatmap_bykeywords['nb_likes']] , "x": [data_heatmap_bykeywords['date']] , "y": [data_heatmap_bykeywords['mot']]}],
                        ),
                        dict(
                            label="Affichae par ordre d'apparition",
                            method="update",
                             args=[{"customdata": ['by_date'], "z": [data_heatmap_bytime['nb_likes']] , "x": [data_heatmap_bytime['date']] , "y": [data_heatmap_bytime['mot']]}],
                        ),
                       
                    ]
                ),
            ),
            dict(
                type="buttons",
                direction="left",
                x=0.8,
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

    fig.update_layout(
    annotations=[
        dict(text="Métrique", x=0, xref="paper", y=1.5, yref="paper",
                             align="left", showarrow=False),
        # dict(text="mois début", x=0, xref="paper", y=1.06, yref="paper",
        #                      align="left", showarrow=False),
        # dict(text="annee debut", x=0.25, xref="paper", y=1.07,
        #                      yref="paper", showarrow=False),
        # dict(text="mois fin", x=0.54, xref="paper", y=1.06, yref="paper",
        #                      showarrow=False),
        # dict(text="annee fin", x=0.6, xref="paper", y=1.06, yref="paper",
        #                      showarrow=False)
    ])

    fig.update_layout( plot_bgcolor='rgba(0, 0, 0,0)', xaxis=dict(showgrid=False,  zeroline=False), yaxis=dict(showgrid=True,  zeroline=False),
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