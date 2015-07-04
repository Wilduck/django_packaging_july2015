import json

import requests


def get_a_kitten():
    '''
    Retrieve a kitten from the Awww subreddt via Reddit's API.
    '''
    kitten_url = "http://www.reddit.com/r/Awww/search/.json"
    payload = {'q': 'kitten', 'sort': 'new', 'limit': 100}
    response = requests.get(kitten_url, params=payload)
    raw_json_response = json.loads(response.content.decode("utf8"))
    data_list = raw_json_response['data']['children']
    kitten_results = list(map(lambda x: x['data'], data_list))

    # sometimes you get self posts, we want to filter those out...
    kittens = [k for k in kitten_results if k['thumbnail'] != 'self']
    return random.choice(kittens)


def kitten_view(request, *args, **kwargs):
    '''
    Render the kitten.html template with a random kitten from the
    Awww subreddit.
    '''
    the_kitten = get_a_kitten()
    # render the kitten template with the kitten we got
    return render_to_response(
        "kitten.html", {'the_kitten': the_kitten},
        context_instance=RequestContext(request))
