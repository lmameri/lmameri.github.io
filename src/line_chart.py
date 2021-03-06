import plotly.graph_objects as go
import preprocess
import hovertemplate


WIDTH = 1000
HEIGHT = 500


def get_linechart(df, media_list):
    fig = go.Figure()
    button_list = []
    button_list.append(
        dict(args=[{'opacity': [1]*32}], label='Vue générale', method='restyle'))

    for i in range(0, len(media_list)):
        fig = fig.add_trace(go.Scatter(
            x=df.loc[df['compte'] == media_list[i]]['date'],
            y=df.loc[df['compte'] == media_list[i]]['MaxFollowers'],
            mode="lines",
            name=media_list[i],
            hovertemplate=hovertemplate.get_hovertemplate_linechart()))
        temp = [0.1] * (len(media_list)+1)
        temp[i] = [1]
        button_list.append(
            dict(args=[{'opacity': temp}], label=media_list[i], method='restyle'))

    fig.update_layout(
        title="Nombre maximal d'abonnés par mois pour chaque média",
        xaxis_title='Mois-Année',
        yaxis_title="Nombre d'abonnés",
        updatemenus=[
            dict(
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=1.35,
                    y=1.15,
                    buttons=button_list
            )
        ]
    )
    fig.update_layout(autosize=False, width=WIDTH, height=HEIGHT)
    return fig
