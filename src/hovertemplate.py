
def get_hovertemplate_barchart():
    style_barchart = "<span>Date de publication: </span>" + \
        "<b>%{x} </b>" +  "<br><span>Nombre de publication: : </span>" + \
        "<b>%{y}</b>" +  "<extra></extra>"
    return style_barchart

def get_hovertemplate_funnel():
    style_funnel = "<span>Mot-clé: </span>" + \
        "<b>%{y} </b>" +  "<br><span>Nombre de publications: : </span>" + \
        "<b>%{x}</b>" + "<extra></extra>"
    return style_funnel
    
def get_hovertemplate_heatmap_keywords():
    style_heatmap_keywords = "<span>Date de publication: </span>" + \
        "<b>%{x} </b>" +  "<br><span>Mot-clé: : </span>" + \
        "<b>%{y}</b>" + "<br><span>Nombre: </span>" + \
        "<b>%{z} </b>" +  "<extra></extra>"
    return style_heatmap_keywords
