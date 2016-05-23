import sys
import time
sys.path.append('/Users/eSQuiRe-x/workspace/eSQuire-Online/src/python')
from eSQuireContentPublishers.facebook_publisher import *
from eSQuireWebScraper.spider import *

app_ids = {
    'esq': '1745121949103438'
}

app_secrets = {
    'esq': '8f53dce746a720bdd75494d950760fb8'
}

page_ids = {
    'me': '712515915465086',
    'esq': '304898056281525'
}

short_live_tokens = {
    'me': 'EAAYzLd3dtU4BALIqLeia9ZBbaZCNcAoGu7ZCTshYtjUM4x9AK6SeSZAXRqrcNZC83qUZC9uQPb4Kwc6o6sNVB3xhhLl2AjanKQI6SbR3wDI6TNQDFpWZBFnW8IUPJwSeDlRfncsgznr0Ds961Xk11ZBg76kH3ppB6z3vXOOyTQY03gZDZD',
    'esq': 'EAAYzLd3dtU4BAE88GXZATY6qptNgsWKb8JyjXLztCGLw4i65qV2tBExSTJNIhprr1O0uX7xqPSMWtcvmv4FnzKTTzRid0OiGNV3SxbqEvK89qNnEOFSjFJdYGy32Qh6UCfeErAZCWyci03PBEqz8RZBDTnJJiZCZBQbr3aYg5o1SHStnC2Glo'
}

long_lived_tokens = {
    'me': 'EAAYzLd3dtU4BAJUZAuJdGl2DqqdabLCBZCdmp3Jf0fnyVMU9gR7ngrmcIPV7DWJNj79fqD7q9X7fiXmUA3h7WxPasEGYqkBccKb7KZBNwdRdTFVFMI6nV4KP3Wlxu6OetuFMQ27BIJimCMSq2gdzrIRcghXGdYZD',
    'esq': 'EAAYzLd3dtU4BAKfV6QPj7dIuA9K1rLSzVs6JZBJjALhJg25nsi4xKoNruZAbM99ZCXZAmW2hZBNTGI53i84qRcQE0x5OcCThI194jOmgdyOaH78q1Nub3qZBpRTwZCZAELcYDnzbsJO4rDdw40zjKNHFzRn4EZCBbvL7CgNPQArkdIQZDZD'
}

pages = {
    'ladbible': '199098633470668',
    'theladbiblevideo': '973302952725209',
    'theladbibleoz': '175750359224528',
    'uniladtech': '1673693016241746',
    'viralhog': '1425176327751701',
    'uniladmag': '146505212039213',
    'uniladtech': '1673693016241746',
    'viralvideouk': '574863922524116',
    'capotesbrasileiros': '769759129712228',
    'peopleareawesome': '305140869535098',
    'fortafyfans': '513404865420527',
    'ads30mMiami': '417086318349420',
    'ommhumor': '863794063647518'
}

my_graph = get_user_api(long_lived_tokens['me'])

EMAIL_RECEIVED = False


def get_latest_email():
    return 'test'


def check_inbox():
    pass


def daemon():
    while True:
        check_inbox()

        if EMAIL_RECEIVED:
            EMAIL_RECEIVED = False

            email = get_latest_email()
            link = get_latest_video(my_graph, page)
            print link
            time.sleep(30)


for page in pages:
    continue
    print 'Scraping {0} for videos !'.format(page)
    videos = get_latest_video(my_graph, page)

    for index, vid in enumerate(videos):
        link = get_facebook_video_mp4_link(vid, pages[page])
        print 'Sending email! {0}/{1}'.format(index+1, len(videos))
        send_email(page=page, link=link)
        r = random.randint(1, 60)
        print 'Email sent! Sleeping for {0} seconds'.format(r)
        time.sleep(r)


antiban = {1: api_like_posts(my_graph, 'LeoMessi'),
           2: api_comment_on_posts(my_graph, 'redbull', 'laaaythal')}

