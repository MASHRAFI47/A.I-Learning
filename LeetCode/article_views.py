import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    arr = views[views['author_id'] == views['viewer_id']]
    arr2 = arr[['author_id']].rename(columns={'author_id': 'id'})
    arr2.sort_values('id', inplace=True)
    arr2.drop_duplicates(subset='id', inplace=True)
    return arr2




# mentor
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    arr = views[ views['author_id']==views['viewer_id']  ]

    arr2 = arr['author_id'].unique()
    arr2 = sorted(arr2)

    return pd.DataFrame({'id':arr2})