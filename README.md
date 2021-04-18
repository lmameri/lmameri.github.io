Pour ajouter votre visualisation :

1) La créer et avoir une fonction qui la retourne. 
Par exemple : get_heatmap() dans heatmap.py.

2) Importer votre script .py dans publish_html.py et récupérer la viz dans le script publish_html.py entre les lignes 8 et 21 (checker la viz 1 pour un exemple)
Par exemple : 
`fig_heatmap_yearly = heatmap.get_heatmap_yearly(df_count_yearly)`

3) Insérer votre viz après la ligne 32 de publish_html.py.
Sous le format f.write(fig_NOM_DE_VOTRE_FIG.to_html(full_html=False))
Par exemple :     
`f.write(fig_heatmap_yearly.to_html(full_html=False))`

4) Executer le script publish_html.py, cela devrait updater index.html en ajoutant votre viz. Vous pouvez vérifier localement en cliquant sur index.html, ca devrait ouvrir la page dans votre browser par défaut. Il faut exécuter depuis la racine du projet.
`python ./src/publish_html.py`

5) Add, commit, push votre code vers github et attendre quelques minutes pour visualiser la nouvelle page via le lien suivant :
lmameri.github.io/index.html


Go to lmameri.github.io/index.html
to viz page.
