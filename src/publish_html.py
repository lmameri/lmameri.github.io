import preprocess 
import heatmap
import line_chart
import barchart
import barchart_keywords
import nlp_preprocess
import histogram
import descriptions_helper as dh

#                               DEFINE VIZS

# Viz 1 - Heatmap par media 
df_heatmap, media_list = preprocess.preprocess_heatmap()
df_count_yearly = preprocess.get_nbpubs_yearly(df_heatmap)
df_count_monthly=preprocess.get_nbpubs_monthly(df_heatmap)
fig_heatmap_yearly = heatmap.get_heatmap_yearly(df_count_yearly,df_count_monthly)

# Viz 2 - Heatmap par mots-clés/Symboles
data_heatmap_by_keywords, data_heatmap_by_time, data_barchart_by_keywords,data_barchart_by_time = nlp_preprocess.execute_preprocess(50,2018,1,2020,12)
fig_heatmap_likes = heatmap.get_heatmap_keywords(data_heatmap_by_keywords,data_heatmap_by_time)
fig_barchart_keywords = barchart_keywords.get_barchart(data_barchart_by_keywords,data_barchart_by_time)

# Viz 3 - Line chart
df_linechart, media_list=preprocess.preprocess_linechart()
fig_linechart=line_chart.get_linechart(df_linechart,media_list)

# Viz 4 - Bar chart
fig_barchart_publications = barchart.get_barchart()


# Viz 5 - Histogrammes
fig_hist_likes = histogram.histogram_plotting("likes")
fig_hist_followers = histogram.histogram_plotting("commentaires")
fig_hist_vues = histogram.histogram_plotting("vues")

#                          INSERTION OF VIZS IN THE HTML PAGE

with open('index.html', 'w') as f:

    f.write(dh.get_title())
    f.write(dh.get_intro_text())

    f.write(dh.get_heatmap_nbpubs_text())
    f.write(fig_heatmap_yearly.to_html(full_html=False))

    f.write(dh.get_heatmap_keywords_text())
    f.write(fig_heatmap_likes.to_html(full_html=False))

    f.write(dh.get_barchart_keywords_text())
    f.write(fig_barchart_keywords.to_html(full_html=False))

    f.write(dh.get_barchart_text())
    f.write(fig_barchart_publications.to_html(full_html=False))

    f.write(dh.get_linechart_text())
    f.write(fig_linechart.to_html(full_html=False))

    f.write(dh.get_histograms_text())
    f.write(fig_hist_likes.to_html(full_html=False))
    f.write(fig_hist_followers.to_html(full_html=False))
    f.write(fig_hist_vues.to_html(full_html=False))

    f.close()