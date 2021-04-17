import pandas as pd 


# Get number of publications per media per year
def get_nbpubs_yearly(df_initial):
    df = df_initial.copy()
    df['date']=df['date'].dt.year
    df = df.rename(columns={"date": "year"})
    df= df.groupby(['compte','year']).size().unstack(fill_value=0)
    return df

# Get number of publications per media per month for a given year
def get_nbpubs_monthly(df_initial, year,media_list):
    df = df_initial.copy()
    df = df[df['date'].dt.year==year]
    df['date']=df['date'].dt.month
    df = df.rename(columns={"date": "Mois_nb"})
    months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Jui', 'Aou', 'Sep', 'Oct', 'Nov', 'Déc' ]
    df['Mois']= [months[month-1] for month in df['Mois_nb'].tolist()]
    df_months = pd.DataFrame (months, columns = ['Mois'])
    df_medias = pd.DataFrame (media_list, columns = ['compte'])
    df=df_months.merge(df.merge(df_months,how='right',on='Mois',sort='False'))# We double merge to keep the order
    #print(df)
    #df=df.merge(df_medias,how='right',on='compte',sort='False')# We double merge to keep the order
    #print('test avec media')
    #print(df)
    df= df.groupby(['compte','Mois'],sort=False).size().unstack(fill_value=0)
    return df

def preprocess_heatmap():
    # colonnes  ['compte', 'pseudo', 'followers', 'date', 'type', 'likes', 'commentaires', 'vues', 'url', 'lien', 'photo', 'titre']
    df = pd.read_csv('src/data/poly-Instagram-2011-2020.csv')
    df = df[['compte','date']] # only keep these two columns
    df['date'] = pd.to_datetime(df['date'])
    media_list=df['compte'].unique()
    return df,media_list
    
#df,media_list=preprocess_heatmap()
#df_count_yearly = get_nbpubs_yearly(df)
#print(df_count_yearly)
#df_count_monthly = get_nbpubs_monthly(df, 2019, media_list)
#print('Count')
#print(df_count_monthly) 



