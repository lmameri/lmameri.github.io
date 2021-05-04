import pandas as pd
import numpy as np
import plotly.express as px
from plotly import graph_objs as go
from preprocess import preprocess_histogram

WIDTH = 1000
HEIGHT = 500


def histogram_plotting(information, nb_bins=50):
    data_needed = preprocess_histogram()
    if information == 'commentaires':
        data_needed = data_needed[data_needed['commentaires'].notna()]
        data_needed[information] = data_needed[information].astype(int)

    step = int((data_needed[information].max() -
               data_needed[information].min()) / nb_bins)
    min_hist = data_needed[information].min()
    max_hist = data_needed[information].max()
    media_list = data_needed['compte'].unique()

    def histogram_media(media):
        if media == 'all':
            data_needed_media = data_needed.copy()
        else:
            data_needed_media = data_needed.loc[data_needed['compte'] == media].copy(
            )

        hist = np.histogram(data_needed_media[information], bins=range(
            min_hist, max_hist + step * 2, step))
        labels = []
        for i, j in zip(hist[1][0::1], hist[1][1::1]):
            if j <= max_hist:
                labels.append('{} - {}'.format(i, j))
            else:
                labels.append('> {}'.format(i))

        data = go.Bar(x=labels,
                      y=hist[0], hovertemplate='<br><b>Nombre de publications:</b>: %{y:} ' +
                                               '<br><b>' + information +
                      ':</b>: %{x}<br> <extra></extra>',
                      visible=True if media == 'all' else False, marker={'color': 'rgb(92, 83, 165)'})

        return data

    data = []
    data.append(histogram_media('all'))
    for media in media_list:
        data.append(histogram_media(media))

    fig = go.Figure(data=data)

    fig.update_xaxes(
        tickmode='array',
        tickvals=[0, int(nb_bins / 2), nb_bins],
        ticktext=["0 - {step}".format(step=step), "{mid_0} - {mid_1}".format(mid_0=step * int(nb_bins / 2),
                                                                             mid_1=step * int(nb_bins / 2) + step),
                  "> {max_hist}".format(max_hist=max_hist)],

        tickangle=45
    )

    fig.update_layout(title_text='Distribution du nombre de {information} dans les publications'.format(
        information=information))

    list_scroll = []

    list_scroll.append(dict(
        args=[{'visible': [True] + [False] * 32}], label='Vue générale', method='update'
    ))

    for i in range(0, len(media_list)):
        temp = [False] * 33
        temp[i + 1] = True
        list_scroll.append(dict(
            args=[{'visible': temp}], label=media_list[i], method='update'
        ))

    fig.update_layout(updatemenus=[dict(buttons=list_scroll, direction="down",
                                        pad={"r": 10, "t": 10},
                                        showactive=True,
                                        x=0.7,
                                        xanchor="left",
                                        y=1.24,
                                        yanchor="top"
                                        )],
                      xaxis_title="{information}".format(
                          information=information),
                      yaxis_title="Nombre de publications"
                      )
    #fig.update_layout(yaxis_title="Fréquence des publications")
    fig.update_layout(autosize=False, width=WIDTH, height=HEIGHT)
    return fig
