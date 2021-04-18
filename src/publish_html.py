import plotly.io as pio
import preprocess 
import heatmap
import line_chart
import test_button

#                               DEFINE VIZS

# Viz 1 - Heatmap par media / en commentaire pour l'instant 
#df_heatmap, media_list = preprocess.preprocess_heatmap()
#df_count_yearly = preprocess.get_nbpubs_yearly(df_heatmap)
#fig_heatmap_yearly = heatmap.get_heatmap_yearly(df_count_yearly,df_heatmap)

# Viz 2 - Heatmap par mots-clés/Symboles

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
    #f.write(fig_heatmap_yearly.to_html(full_html=False))
    #f.write(fig_test.to_html(full_html=False))
    #f.write(fig_test_button.to_html(full_html=False))
    #f.write(fig_line_chart.to_html(full_html=False))

    f.close()