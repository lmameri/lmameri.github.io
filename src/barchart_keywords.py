import plotly.express as px
import preprocess
import plotly.graph_objects as go
import hovertemplate

WIDTH = 1000
HEIGHT = 1100

# permet la realisation du barchart avec plotly
# paramètres : 1 dataframe des mots cles triees par importance et 1 dataframe des mots cles triees par ordre d apparition


def get_barchart(data_barchart_by_keywords, data_barchart_by_time):
    fig = go.Figure()

    colors = ['rgb(92, 83, 165)' for x in data_barchart_by_keywords['mot']]
    marker = {"color": colors, "line": {"color": colors}}
    connector = {"line": {"color": "rgb(191, 88, 95)"}}
 
    trace_bar = go.Bar(
        y=data_barchart_by_keywords['mot'],
        x=data_barchart_by_keywords['nb_occurences'],
        orientation='h', marker=dict(color='rgb(92, 83, 165)'), hovertemplate=hovertemplate.get_hovertemplate_barchart()
    )

    fig.add_traces(trace_bar)

    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="left",
                x=0.7,
                y=1.05,
                showactive=True,
                buttons=list(
                    [
                        dict(
                            label="Par score TF-IDF",
                            method="update",
                            args=[{"x": [data_barchart_by_keywords['nb_occurences']], "y": [
                                data_barchart_by_keywords['mot']]}]
                        ),
                        dict(
                            label="Par ordre d\'apparition dans le temps",
                            method="update",
                            args=[{"x": [data_barchart_by_time['nb_occurences']], "y": [
                                data_barchart_by_time['mot']]}]
                        )
                    ]
                )
            )
        ]
    )

    fig.update_layout(dragmode=False,
                      autosize=False,
                      width=WIDTH,
                      height=HEIGHT,
                      plot_bgcolor='rgba(0,0,0,0)',
                      xaxis_title="Nombre d'occurences",
                      yaxis_title="Mots clés",
                      title='Nombre de publication par mots clés',
                      annotations=[
                          dict(text="Classement des mots clés : ", x=0, xref="paper", y=1.05, yref="paper",
                               align="left", showarrow=False),
                      ]
                      )

    return fig
