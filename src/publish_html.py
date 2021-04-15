import plotly.io as pio
import preprocess 
import heatmap
import test_button


df_heatmap, media_list = preprocess.preprocess_heatmap()
df_count_yearly = preprocess.get_nbpubs_yearly(df_heatmap)
df_count_monthly = preprocess.get_nbpubs_monthly(df_heatmap, 2012,media_list) # exemple annee
fig_heatmap_yearly = heatmap.get_heatmap_yearly(df_count_yearly)

fig_test = heatmap.get_heatmap_test()
fig_test_button = test_button.test_button()
pio.write_html(fig_test_button, file="pages/test_button.html", auto_open=True)