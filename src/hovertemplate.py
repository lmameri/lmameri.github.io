
def get_hovertemplate_barchart():
    style_barchart = "<span>Date de publication : </span>" + \
        "<b>%{x} </b>" + "<br><span>Nombre de publications : </span>" + \
        "<b>%{y}</b>" + "<extra></extra>"
    return style_barchart


def get_hovertemplate_funnel():
    style_funnel = "<span>Mot-clé : </span>" + \
        "<b>%{y} </b>" + "<br><span>Nombre de publications : </span>" + \
        "<b>%{x}</b>" + "<extra></extra>"
    return style_funnel


def get_hovertemplate_heatmap_keywords():
    style_heatmap_keywords = "<span>Date de publication : </span>" + \
        "<b>%{x} </b>" + "<br><span>Mot-clé : </span>" + \
        "<b>%{y}</b>" + "<br><span>Nombre : </span>" + \
        "<b>%{z} </b>" + "<extra></extra>"
    return style_heatmap_keywords


def get_hovertemplate_heatmap_nb_pubs(unit):
    if unit == 'year':
        style_heatmap_nb_pubs = "Année : %{x|%Y} <br>Média : %{y} </br>Nombre de publications : %{z}<extra></extra>"
    else:
        style_heatmap_nb_pubs = "Mois et Année : %{x} <br>Média : %{y} </br>Nombre de publications : %{z}<extra></extra>"
    return style_heatmap_nb_pubs


def get_hovertemplate_linechart():
    style_linechart = "<span>Période : </span>" + \
        "<b>%{x}</b>" + "<br><span>Nombre d'abonnés : </span>" + \
        "<b>%{y}</b>" + "<extra></extra>"
    return style_linechart

def get_hovertemplate_histogram(info):
    style_histogram = '<br><b>Nombre de publications : </b> %{y:} ' + '<br><b>' + info + '</b>: %{x}<br> <extra></extra>'
    return style_histogram

