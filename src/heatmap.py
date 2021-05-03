import preprocess
import plotly.graph_objects as go
import hovertemplate

WIDTH_HEATMAP_YEARLY = 1000
HEIGHT_HEATMAP_YEARLY =  700
WIDTH_HEATMAP_KEYWORDS = 1500
HEIGHT_HEATMAP_KEYWORDS =  1100


# Generate the heatmap representing the number of publications per year
def get_heatmap_yearly(df_yearly, df_monthly):
    medias = df_yearly.index.to_list()

    # create figure
    fig = go.Figure()

    # Add heatmap yearly trace
    fig.add_trace(go.Heatmap(visible=True,
                             z=df_yearly.values,
                             x=df_yearly.columns,
                             y=df_yearly.index,
                             hoverongaps=False, colorscale='sunset',
                             hovertemplate=hovertemplate.get_hovertemplate_heatmap_nb_pubs('year')))

    # Add heatmap monthly traces for each year
    fig.add_trace(go.Heatmap(visible=False,
                             z=df_monthly.values,
                             x=df_monthly.columns,
                             y=df_monthly.index,
                             hoverongaps=False, colorscale='sunset',
                             hovertemplate=hovertemplate.get_hovertemplate_heatmap_nb_pubs('month')))

    fig.update_yaxes(tickvals=medias)
    fig.update_layout(title='Nombre de publications par média par année')

    # Define buttons
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="left",
                x=1.25,
                y=1.1,
                showactive=True,
                buttons=list(
                    [
                        dict(
                            label="Vues globales annuelles",
                            method="update",
                            args=[{"visible": [True, False]}],
                        ),
                        dict(
                            label="Vues globales mensuelles ",
                            method="update",
                            args=[{"visible":  [False, True]}],
                        ),
                    ]
                ),
            )
        ]
    )
    fig.update_layout(dragmode=False,
                      plot_bgcolor='rgba(0, 0, 0,0)',
                      xaxis_title="Période de publication",
                      yaxis_title="Médias",
                      yaxis_nticks=len(medias),
                      xaxis_dtick='M12',
                      xaxis_ticklabelmode='period')
    fig.update_layout(autosize=False,width=WIDTH_HEATMAP_YEARLY,height=HEIGHT_HEATMAP_YEARLY)
	
    return fig


# permet de tracer la heatmap des mots cles 
# paramètres :  1 dataframe des mots cles triees par importance et 1 dataframe des mots cles triees par ordre d apparition  
def get_heatmap_keywords(data_heatmap_bykeywords,data_heatmap_bytime):
    fig = go.Figure()

    title_map = 'Métriques du TOP 50 des mots clés'

    trace_heatmap=go.Heatmap(customdata= ['by_keywords'],
                            z=data_heatmap_bykeywords['nb_likes'], 
                            x=data_heatmap_bykeywords['date'], 
                            y=data_heatmap_bykeywords['mot'],
                            colorscale='sunset', hovertemplate=hovertemplate.get_hovertemplate_heatmap_keywords(), hoverongaps=False)


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
                            args=[{"z": [update_zaxis(fig,data_heatmap_bykeywords,data_heatmap_bytime, 'nb_likes')]}],
                        ),
                        dict(
                            label="Nombre de commentaires",
                            method="update",
                            args=[{"z": [update_zaxis(fig, data_heatmap_bykeywords, data_heatmap_bytime, 'nb_commentaires')]}],
                        ),
                        dict(
                            label="Nombre de vues",
                            method="update",
                            args=[{"z": [update_zaxis(fig, data_heatmap_bykeywords, data_heatmap_bytime, 'nb_vues')]}],
                        ),
                       
                    ]
                ),
            ),

        ]
    )

    fig.update_layout( xaxis_title="Date de publication",
                    yaxis_title="Mots clés",
                    title=title_map, 
                    autosize=False,
                    width=WIDTH_HEATMAP_KEYWORDS,
                    height=HEIGHT_HEATMAP_KEYWORDS,
                    plot_bgcolor='rgba(0, 0, 0,0)',
                    xaxis=dict(showgrid=False,  zeroline=False),
                    yaxis=dict(showgrid=True,  zeroline=False),
                    annotations=[
                        dict(text="Métriques : ", x=0.6, xref="paper", y=1.04, yref="paper",
                                            align="left", showarrow=False),
                        dict(text="Classement des mots clés : ", x=0, xref="paper", y=1.04, yref="paper",
                                            align="left", showarrow=False),
                    ]
                    )
    return fig


# permet de updater l'axe des z lorsqu'on clique sur le bouton likes 
# paramètres :  la heatmap (fig),  1 dataframe des mots cles triees par importance et 1 dataframe des mots cles triees par ordre d apparition  
def update_zaxis(fig, data_heatmap_bykeywords, data_heatmap_bytime, metric):
    if(fig['data'][0]['customdata'][0] == 'by_keywords'):
        return data_heatmap_bykeywords[metric]
    if(fig['data'][0]['customdata'][0] == 'by_date'):
        return data_heatmap_bytime[metric]

