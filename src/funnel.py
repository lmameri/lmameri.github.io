import plotly.express as px
import preprocess
import plotly.graph_objects as go


style = "<span>Mot-clé: </span>" + \
        "<b>%{y} </b>" +  "<br><span>Nombre de publications: : </span>" + \
        "<b>%{x}</b>" + "<extra></extra>"

def get_funnel(data_funnel_by_keywords,data_funnel_by_time):
    fig = go.Figure()

    colors=['rgb(92, 83, 165)' for x in data_funnel_by_keywords['mot']]
    marker = {"color": colors, "line": {"color": colors}}
    connector = {"line": {"color": "rgb(191, 88, 95)"}}
    trace_funnel = go.Funnel( y = data_funnel_by_keywords['mot'], x = data_funnel_by_keywords['nb_occurences'],marker=marker,connector=connector, hovertemplate=style)
    fig.add_traces(trace_funnel)
    

    fig.update_layout(
        updatemenus = [
            dict(
                type="buttons",
                direction="left",
                x=0.5,
                y=1.1,
                showactive=True,
                buttons=list(
                    [
                        dict(
                            label="Par importance",
                            method="update",
                            args=[{"x" : [data_funnel_by_keywords['nb_occurences']] , "y": [data_funnel_by_keywords['mot']]}]
                        ),
                        dict(
                            label="Par date d\'apparition dans le temps",
                            method="update",
                            args=[{"x" : [data_funnel_by_time['nb_occurences']] , "y": [data_funnel_by_time['mot']]}]
                        )
                    ]
                )
            )
        ]
    )
    fig.update_layout(dragmode=False,plot_bgcolor='rgba(0,0,0,0)', xaxis_title="Nombre d'occurences",yaxis_title="Mots clés",title='Nombre de publication par mots clés',
    annotations=[
        dict(text="Classement des mots clés : ", x=0, xref="paper", y=1.05, yref="paper",
                             align="left", showarrow=False),
    ])
    return fig