# instalar pip install --upgrade google-api-python-client

from googleapiclient.discovery import build

youTubeApiKey="GOOGLE_API_CREDENCIAIS"
youtube = build('youtube','v3', developerKey=youTubeApiKey)

playlistId = 'PLBogheOqVjI-J4iPPteanK4Ft-pRBUnKj'
playlistName = 'Todos os Videos'
nextPage_token = None

# mostra a playlist de videos
playlist_videos = []

while True:
  res = youtube.playlistItems().list(part='snippet', playlistId = playlistId, maxResults=50, pageToken=nextPage_token).execute()
  playlist_videos += res['items']
  
  nextPage_token = res.get('nestPageToken')

  if nextPage_token is None:
    break

# mostra o numero total de videos na playlist
print("numero total de videos na playlist", len(playlist_videos))
videos_ids = list(map(lambda x: x['snippet']['resourceId']['videoId'], playlist_videos))
print(videos_ids)

# mostra o status do video. numero de like, deslike, views, entre outras informações
stats = []

for video_id in videos_ids:
  res = youtube.videos().list(part='statistics', id=video_id).execute()
  stats += res['items']

print(stats)

#extraindo as informações
videos_title = list(map(lambda x: x['snippet']['title'], playlist_videos))
url_thumbnails = list(map(lambda x: x['snippet']['thumbnails']['high']['url'], playlist_videos))
published_date = list(map(lambda x: str(x['snippet']['publishedAt']), playlist_videos))
video_description = list(map(lambda x: x['snippet']['description'], playlist_videos))
videoid = list(map(lambda x: x['snippet']['resourceId']['videoId'], playlist_videos))

### Dataframe
from datetime import datetime 
import pandas as pd

extraction_date = [str(datetime.now())]*len(videos_ids)

playlist_df = pd.DataFrame({'title':videos_title,
      'video_id':videoid,
      'video_description':video_description,
      'published_date':published_date,
      'extraction_date':extraction_date,
      'likes':liked,
      'dislikes':disliked,
      'views':views,
      'comment':comment,
      'thumbnail': url_thumbnails})
      
playlist_df.head()
