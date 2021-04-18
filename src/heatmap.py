import plotly.express as px
import plotly.graph_objects as go
import preprocess


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