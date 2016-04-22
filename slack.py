
import urllib

class Slack(object):
    def __init__(self, **kwargs):
        self.status   = kwargs['status']
        self.token    = kwargs['token']
        self.channel  = kwargs['channel']
        self.username = kwargs['username']

    def send(self, exception, message):
        if getattr(exception, 'status', 500) >= self.status:
            data = urllib.parse.urlencode(dict(
                token = self.token,
                channel = self.channel,
                text = message,
                username = self.username,
                ))
            r = urllib.request.urlopen(
                'https://slack.com/api/chat.postMessage', data.encode('utf-8')
                )