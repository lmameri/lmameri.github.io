import pandas as pd 
import numpy as np

df_insta = pd.read_csv('src/data/poly-Instagram-2011-2020.csv')
df_insta['date'] = pd.to_datetime(df_insta['date'])

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
    print('a')
    print(df)
    months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Jui', 'Aou', 'Sep', 'Oct', 'Nov', 'Déc' ]
    df['Mois']= [months[month-1] for month in df['Mois_nb'].tolist()]
    df_months = pd.DataFrame (months, columns = ['Mois'])
    df_medias = pd.DataFrame (media_list, columns = ['compte'])
    df=df_months.merge(df.merge(df_months,how='right',on='Mois',sort='False'))# We double merge to keep the order
    print('b')
    print(df)
    df= df.groupby(['compte','Mois'],sort=False).size().unstack(fill_value=0)
    df=df.merge(df_medias,how='right',on='compte',sort='False').fillna(0)
    for month in months:
        if month not in df.columns.tolist():
            df[month]=0 
    print('c')
    print(df)
    df = pd.DataFrame(df, columns=months)
    df = df[df.columns.tolist()].applymap(np.int64)
    print('f')
    print(df)
    return df

def preprocess_heatmap():
    # colonnes  ['compte', 'pseudo', 'followers', 'date', 'type', 'likes', 'commentaires', 'vues', 'url', 'lien', 'photo', 'titre']
    df = df_insta
    df = df[['compte','date']] # only keep these two columns
    media_list=df['compte'].unique()
    return df,media_list

def preprocess_barchart():
    df_insta['date'] = (df_insta['date']).dt.strftime("%Y-%m")
    df = df_insta[['date','type']]
    df['count'] = 1
    print(df)
    df = df.groupby(['date', 'type'])['count'].count().reset_index()
    df_photo = df.loc[df['type'] == 'Photo']
    df_video = df.loc[df['type'] == 'Video']
    df_album = df.loc[df['type'] == 'Album']
    df_igtv = df.loc[df['type'] == 'IGTV']
    return df_photo,df_video,df_album,df_igtv

# if __name__ == "__main__":
#     preprocess_barchart()
    
#df,media_list=preprocess_heatmap()
#df_count_yearly = get_nbpubs_yearly(df)
#print(df_count_yearly)
#df_count_monthly = get_nbpubs_monthly(df, 2019, media_list)
#print('Count')
#print(df_count_monthly) 



