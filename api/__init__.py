import orjson
import requests

TWITCH_CLIENT_ID = ""
TWITCH_SECRET = ""
def getToken ():
    data = requests.post (
        f'https://id.twitch.tv/oauth2/token?client_id={TWITCH_CLIENT_ID}&client_secret={TWITCH_SECRET}&grant_type=client_credentials'
    )
    data = orjson.loads(data.text)
    token = data['access_token']
    return token

def user_request (id : str):
    token = getToken()
    headers = {
        'Authorization': f'Bearer {token}',
        f'Client-ID': '{TWITCH_CLIENT_ID}'
    }
    response = requests.get (url=f"https://api.twitch.tv/helix/users?login={id}", headers=headers)
    return orjson.loads(response.text)

def stream_request (id):
    token = getToken()
    headers = {
        'Authorization': f'Bearer {token}',
        f'Client-ID': '{TWITCH_CLIENT_ID}'
    }
    response = requests.get (url = f"https://api.twitch.tv/helix/streams?user_login={id}", headers=headers)
    return orjson.loads(response.text)