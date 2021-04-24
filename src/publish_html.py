import plotly.io as pio
import preprocess 
import heatmap
import line_chart
import barchart
import test_button
import funnel
import nlp_preprocess
import histogram

#                               DEFINE VIZS

# Viz 1 - Heatmap par media / en commentaire pour l'instant 
df_heatmap, media_list = preprocess.preprocess_heatmap()
df_count_yearly = preprocess.get_nbpubs_yearly(df_heatmap)
fig_heatmap_yearly = heatmap.get_heatmap_yearly(df_count_yearly,df_heatmap)

# Viz 2 - Heatmap par mots-clés/Symboles
data_heatmap_by_keywords, data_heatmap_by_time, data_funnel_by_keywords,data_funnel_by_time = nlp_preprocess.execute_preprocess(50,2018,1,2020,12)
fig_heatmap_likes = heatmap.get_heatmap_keywords(data_heatmap_by_keywords,data_heatmap_by_time)
fig_funnel = funnel.get_funnel(data_funnel_by_keywords,data_funnel_by_time)

# Viz 3 - Line chart
#fig_line_chart = line_chart.get_linechart(data)
df_linechart, media_list=preprocess.preprocess_linechart()
fig_linechart=line_chart.get_linechart(df_linechart,media_list)

# Viz 4 - Bar chart
fig_barchart = barchart.get_barchart()


# Viz 5 - Histogrammes
fig_hist_likes = histogram.histogram_plotting("likes")
fig_hist_followers = histogram.histogram_plotting("followers")
fig_hist_vues = histogram.histogram_plotting("vues")


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
    f.write(fig_funnel.to_html(full_html=False))
    f.write(fig_barchart.to_html(full_html=False))
    f.write(fig_linechart.to_html(full_html=False))
    f.write(fig_hist_likes.to_html(full_html=False))
    f.write(fig_hist_followers.to_html(full_html=False))
    f.write(fig_hist_vues.to_html(full_html=False))
    f.close()
