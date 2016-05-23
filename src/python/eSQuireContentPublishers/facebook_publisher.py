import facebook
import requests
from requests_toolbelt import MultipartEncoder


VIDEO_GRAPH_PLACEHOLDER = "https://graph-video.facebook.com/{0}?access_token={1}"

LONG_LIVED_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token?' \
                       'client_id={APP_ID}&' \
                       'client_secret={APP_SECRET}&' \
                       'grant_type=fb_exchange_token&' \
                       'fb_exchange_token={EXISTING_ACCESS_TOKEN}'


def get_user_api(token):
    api = facebook.GraphAPI(token)
    return api


def get_page_api(user_api, page_id):
    resp = user_api.get_object('me/accounts')

    for pg in resp['data']:
        if pg['id'] == page_id:
            page_access_token = pg['access_token']
            break
    else:
        raise StandardError

    return facebook.GraphAPI(page_access_token)


def api_post_status(api, status):
    api.put_wall_post(status)


def api_post_image(api, image_src):
    api.put_photo(open(image_src))


def api_post_video(token, id='me', vid_src=None, vid_title=None, vid_desc=None, vid_thumb=None):
    page_videos_path = "{0}/videos".format(id)

    video_file_name = vid_src.split("/")[-1]

    uri = VIDEO_GRAPH_PLACEHOLDER.format(page_videos_path, token)

    data = MultipartEncoder(fields={'title': vid_title,
                                    'description': vid_desc,
                                    'thumb': vid_thumb,
                                    'source': (video_file_name, open(vid_src, 'rb'))})

    r = requests.post(uri, headers={'Content-Type': data.content_type}, data=data)


def api_like_posts(user_api, page):
    profile = user_api.get_object(page)
    posts = user_api.get_connections(profile["id"], "posts", limit=2)

    for index, post in enumerate(posts['data']):
        user_api.put_object(post['id'], 'likes')
        print 'Liked {0}/{1}!'.format(index+1, len(posts['data']))


def api_comment_on_posts(user_api, page, comment):
    profile = user_api.get_object(page)
    posts = user_api.get_connections(profile["id"], "posts", limit=2)
    for index, post in enumerate(posts["data"]):
        user_api.put_comment(post["id"], message=comment)
        print 'Commented {0}/{1}!'.format(index+1, len(posts['data']))
