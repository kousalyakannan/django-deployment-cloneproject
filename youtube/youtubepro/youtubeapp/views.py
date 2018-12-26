from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from youtubeapp.forms import SearchForm
from youtubeapp.models import Search
import oauth2client
from oauth2client import tools

import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Create your views here.

class IndexPage(TemplateView):
    template_name = 'index.html'

class SearchCreateView(CreateView):
    redirect_field_name = 'youtubeapp/main.html'
    form_class = SearchForm
    model=Search


DEVELOPER_KEY = 'AIzaSyBhtNyTQMsYbFdIC1Qc1hbQG0LIT8jlAG4'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(request):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
    search_response = youtube.search().list(
        q=request.q,
        part='id,snippet',
        maxResults=request.max
    ).execute()

    videos = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s' % (search_result['snippet']['title']))
            ctx1 = ('\n'.join(videos))
            videos.append('%s' % (search_result['id']['videoId']))
            ctx2 = ('\n'.join(videos))
            mydict = {'title':ctx1,'videoid':ctx2} 
    return render(request,'youtubeapp/main.html',context = mydict)
        
    


#if __name__ == '__main__':
def main(request,pk):
  parser = tools.argparser
  mxRes = 3
  parser.add_argument('--q', help='Search term', default='Srce Cde')
  parser.add_argument('--max', help='Max results')
  parser.add_argument("--key", help="Required API key")

  args = parser.parse_args([])

  if not args.max:
      args.max = mxRes

  try:
    youtube_search(args)
  except HttpError as e:
    print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))


