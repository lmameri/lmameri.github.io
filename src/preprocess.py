import pandas as pd
import numpy as np

df_insta = pd.read_csv('src/data/poly-Instagram-2011-2020.csv')
df_insta['date'] = pd.to_datetime(df_insta['date'])


# Get number of publications per media per year
def get_nbpubs_yearly(df_initial):
    df = df_initial.copy()
    df['date'] = df['date'].dt.year
    df = df.rename(columns={"date": "year"})
    df = df.groupby(['compte', 'year']).size().unstack(fill_value=0)
    df.columns = pd.date_range(
        start='6/15/2011', end='6/15/2020', freq=pd.DateOffset(years=1))
    df.replace(0, np.nan, inplace=True)
    df = df.reindex(index=df.index[::-1])
    return df


# Get number of publications per media per month for a given year
def get_nbpubs_monthly(df_initial):
    df = df_initial.copy()
    df['date'] = pd.to_datetime(df['date'])
    df['date'] = df['date'].values.astype('datetime64[M]')
    df = df.groupby(['date', 'compte']).size().to_frame(
        'nb_pubs').reset_index()
    days_of_year = pd.date_range(
        start='1/1/2011', end='31/12/2020').to_frame(index=False, name='date')
    days_of_year['date'] = days_of_year['date'].values.astype('datetime64[M]')
    days_of_year['date'] = days_of_year.drop_duplicates(
        subset=['date'], keep='first')
    days_of_year = days_of_year[days_of_year['date'].notnull()].reset_index()
    df = days_of_year.merge(df, on='date', how='left').fillna(
        0).astype({'nb_pubs': int})
    df = pd.pivot_table(df, index="compte", columns="date",
                        values="nb_pubs").iloc[1:]
    df = df.reindex(index=df.index[::-1])
    return df


def preprocess_heatmap():
    # colonnes  ['compte', 'pseudo', 'followers', 'date', 'type', 'likes', 'commentaires', 'vues', 'url', 'lien', 'photo', 'titre']
    df = df_insta.copy()
    df = df[['compte', 'date']]  # only keep these two columns
    media_list = df['compte'].unique()
    return df, media_list


# recupere les donnees necessaires pour le barchart
def preprocess_barchart():
    df = (df_insta[['date', 'type']]).copy()
    df['date'] = pd.to_datetime(df['date']).dt.strftime("%Y-%m")
    df['count'] = 1
    df = df.groupby(['date', 'type'])['count'].count().reset_index()
    df_photo = df.loc[df['type'] == 'Photo']
    df_video = df.loc[df['type'] == 'Video']
    df_album = df.loc[df['type'] == 'Album']
    df_igtv = df.loc[df['type'] == 'IGTV']
    return df_photo, df_video, df_album, df_igtv


# recupere les donnees necessaires pour le barchart par media
# paramètres : le nom du média
def preprocess_barchart_account(account):
    df = (df_insta.loc[df_insta['compte'] == account]).copy()
    df['date'] = pd.to_datetime(df['date']).dt.strftime("%Y-%m")
    df['count'] = 1
    df = df.groupby(['date', 'type'])['count'].count().reset_index()
    df_photo_account = df.loc[df['type'] == 'Photo']
    df_video_account = df.loc[df['type'] == 'Video']
    df_album_account = df.loc[df['type'] == 'Album']
    df_igtv_account = df.loc[df['type'] == 'IGTV']
    return df_photo_account, df_video_account, df_album_account, df_igtv_account


def preprocess_linechart():
    df = df_insta.copy()
    df['date'] = (df['date']).dt.strftime("%Y-%m")
    df = df.groupby(['compte', 'date'])['followers'].max(
    ).reset_index().rename(columns={'followers': 'MaxFollowers'})
    media_list = df['compte'].unique()
    return df, media_list


def preprocess_histogram():
    data = df_insta.copy()
    data = data[['compte', 'followers', 'likes', 'commentaires', 'vues']]
    data['likes'].loc[(data['likes'] > 1500)] = 1500
    data['followers'].loc[(data['followers'] > 500000)] = 500000
    data['vues'].loc[(data['vues'] > 10000)] = 10000
    return data
