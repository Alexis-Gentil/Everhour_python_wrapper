import requests

from endpoints.base import EVERHOUR_API_URL
from endpoints.users import Users
from endpoints.tasks import Tasks
from endpoints.team import Team
from endpoints.timers import Timers
from endpoints.projects import Projects
from endpoints.webhooks import Webhooks


class Everhour:
    def __init__(self, token):
        self.session = requests.Session()
        self.session.get(EVERHOUR_API_URL)
        self.session.headers.update({
            'X-Api-Key': token,
            'X-Accept-Version': '1.2',
            'Content-Type': 'application/json'
        })

    @property
    def users(self):
        return Users(self)

    @property
    def task(self):
        return Tasks(self)

    @property
    def team(self):
        return Team(self)

    @property
    def timers(self):
        return Timers(self)

    @property
    def projects(self):
        return Projects(self)

    @property
    def webhooks(self):
        return Webhooks(self)
