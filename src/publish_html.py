import plotly.io as pio
import preprocess 
import heatmap
import line_chart
import test_button
import nlp_preprocess

#                               DEFINE VIZS

# Viz 1 - Heatmap par media
df_heatmap, media_list = preprocess.preprocess_heatmap()
df_count_yearly = preprocess.get_nbpubs_yearly(df_heatmap)
df_count_monthly = preprocess.get_nbpubs_monthly(df_heatmap, 2012,media_list) # exemple annee
fig_heatmap_yearly = heatmap.get_heatmap_yearly(df_count_yearly)

# Viz 2 - Heatmap par mots-clés/Symboles
data_heatmap_likes, data_heatmap_commentaires, data_heatmap_vues = nlp_preprocess.execute_preprocess(50,2018,1,2018,12)
fig_heatmap_likes = heatmap.get_heatmap_keywords('likes', data_heatmap_likes)
fig_heatmap_commentaires = heatmap.get_heatmap_keywords('commentaires',data_heatmap_commentaires)
fig_heatmap_vues = heatmap.get_heatmap_keywords('vues',data_heatmap_vues)

# Viz 3 - Line chart
#fig_line_chart = line_chart.get_linechart(data)

# Viz 4 - Bar chart

# Viz 5 - Histogrammes

# Viz des tests a retirer avant soumission (exemple extrait des tutoriels plotly)
#fig_test = heatmap.get_heatmap_test()
#fig_test_button = test_button.test_button()
#pio.write_html(fig_test_button, file="pages/test_button.html", auto_open=True)


#                          INSERT VIZS IN THE HTML PAGE

# Ajouter vos visualisations ici 
# Sous le format f.write(fig_NOM_DE_VOTRE_FIG.to_html(full_html=False))
with open('index.html', 'w') as f:
    f.write(fig_heatmap_yearly.to_html(full_html=False))
    f.write(fig_heatmap_likes.to_html(full_html=False))
    f.write(fig_heatmap_commentaires.to_html(full_html=False))
    f.write(fig_heatmap_vues.to_html(full_html=False))
    #f.write(fig_test.to_html(full_html=False))
    #f.write(fig_test_button.to_html(full_html=False))
    #f.write(fig_line_chart.to_html(full_html=False))

    f.close()