import plotly.io as pio
import preprocess 
import heatmap
import line_chart
import barchart
import test_button
import funnel
import nlp_preprocess

#                               DEFINE VIZS

# Viz 1 - Heatmap par media / en commentaire pour l'instant 
#df_heatmap, media_list = preprocess.preprocess_heatmap()
#df_count_yearly = preprocess.get_nbpubs_yearly(df_heatmap)
#fig_heatmap_yearly = heatmap.get_heatmap_yearly(df_count_yearly,df_heatmap)

# Viz 2 - Heatmap par mots-clés/Symboles
data_heatmap, data_funnel = nlp_preprocess.execute_preprocess(50,2018,1,2018,12)
fig_heatmap_likes = heatmap.get_heatmap_keywords('likes', data_heatmap)
fig_heatmap_commentaires = heatmap.get_heatmap_keywords('commentaires',data_heatmap)
fig_heatmap_vues = heatmap.get_heatmap_keywords('vues',data_heatmap)
fig_funnel = funnel.get_funnel(data_funnel)

# Viz 3 - Line chart
#fig_line_chart = line_chart.get_linechart(data)

# Viz 4 - Bar chart
df_photo,df_video,df_album,df_igtv = preprocess.preprocess_barchart()
fig_barchart = barchart.get_barchart(df_photo, df_video, df_album, df_igtv)
# Viz 5 - Histogrammes

# Viz des tests a retirer avant soumission (exemple extrait des tutoriels plotly)
#fig_test = heatmap.get_heatmap_test()
#fig_test_button = test_button.test_button()
#pio.write_html(fig_test_button, file="pages/test_button.html", auto_open=True)


#                          INSERT VIZS IN THE HTML PAGE

# Ajouter vos visualisations ici 
# Sous le format f.write(fig_NOM_DE_VOTRE_FIG.to_html(full_html=False))
with open('index.html', 'w') as f:
    #f.write(fig_heatmap_yearly.to_html(full_html=False))
    f.write(fig_heatmap_likes.to_html(full_html=False))
    f.write(fig_heatmap_commentaires.to_html(full_html=False))
    f.write(fig_heatmap_vues.to_html(full_html=False))
    f.write(fig_barchart.to_html(full_html=False))
    f.write(fig_funnel.to_html(full_html=False))
    #f.write(fig_test.to_html(full_html=False))
    #f.write(fig_test_button.to_html(full_html=False))
    #f.write(fig_line_chart.to_html(full_html=False))

    f.close()