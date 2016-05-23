import urllib
import re

PLACEHOLDER = 'https://m.facebook.com/story.php?story_fbid={0}&id={1}&_rdr'
SOL = 'video_redirect\/\?src\='
EOL = '\&amp\;'

ascii_map = {'%3A': ':', '%2F': '/', '%3F': '?', '%3D': '=', '%26': '&'}


def get_latest_video(user_api, page):
    profile = user_api.get_object(page)
    videos = user_api.get_connections(profile['id'], 'videos', limit=1)
    return [video['id'] for video in videos['data']]


def get_video_ids(user_api, page):
    profile = user_api.get_object(page)
    videos = user_api.get_connections(profile['id'], 'videos', limit=5)
    return [video['id'] for video in videos['data']]


def get_9gag_gifs():
    page = urllib.urlopen('http://9gag-rss.com/api/rss/get?code=9GAG')
    gifs = re.findall(r'&lt;source src="(.*?)" type="video/mp4"&gt;', page.read())
    return [gif for gif in gifs]


def get_facebook_video_mp4_link(video_id, page_id):
    connection_url = PLACEHOLDER.format(video_id, page_id)
    connection = urllib.urlopen(connection_url)
    html = connection.read()
    mp4_link = re.findall('{0}(.*?){1}'.format(SOL, EOL), html, re.DOTALL)[0]

    for key in ascii_map:
        mp4_link = mp4_link.replace(key, ascii_map[key])

    return mp4_link
