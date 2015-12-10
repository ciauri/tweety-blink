from tweepy import OAuthHandler, API


def authenticate(credentials):
    auth = OAuthHandler(credentials['c-key'], credentials['c-secret'])
    auth.set_access_token(credentials['a-token'],credentials['a-token-secret'])
    return API(auth, wait_on_rate_limit=True)