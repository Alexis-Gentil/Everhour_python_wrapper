import requests
import json

_EVERHOUR_API_URL = 'https://api.everhour.com'


class Resource:
    def __init__(self, api):
        self._api = api
        self._session = api.session

    def _get(self, url):
        return self._session.get(_EVERHOUR_API_URL + url).json()

    def _post(self, url, data):
        return self._session.post(_EVERHOUR_API_URL + url, data=json.dumps(data)).json()

    def _put(self, url, data):
        return self._session.put(_EVERHOUR_API_URL + url, data=json.dumps(data)).json()

    def _delete(self, url, data):
        return self._session.delete(_EVERHOUR_API_URL + url, data=json.dumps(data))


class Users(Resource):
    def me(self):
        return self._get('/users/me')

    def time(self, id_='me'):
        return self._get('/users/{0}/time'.format(id_))


class Tasks(Resource):
    ADD_TIME = "ADD TIME"
    UPDATE_TIME = "UPDATE TIME"
    DELETE_TIME = "DELETE TIME"

    def get(self, id_):
        return self._get('/tasks/{0}'.format(id_))

    def _manage_time(self, action, id_, time, date, user_id=None):
        data = {
            "time": time,  # Time in seconds
            "date": date,  # Date in format AAAA-MM-DD
        }

        if user_id is not None:
            data["user"] = user_id  # User ID

        if action == self.ADD_TIME:
            return self._post('/tasks/{0}/time'.format(id_), data=data)
        if action == self.UPDATE_TIME:
            return self._put('/tasks/{0}/time'.format(id_), data=data)
        if action == self.DELETE_TIME:
            return self._delete('/tasks/{0}/time'.format(id_), data=data)

    def get_time(self, id_):
        return self._get('/tasks/{0}/time'.format(id_))

    def add_time(self, id_, time, date, user_id=None):
        return self._manage_time(self.ADD_TIME, id_, time, date, user_id)

    def update_time(self, id_, time, date, user_id=None):
        return self._manage_time(self.UPDATE_TIME, id_, time, date, user_id)

    def delete_time(self, id_, time, date, user_id=None):
        return self._manage_time(self.DELETE_TIME, id_, time, date, user_id)

    def set_estimate(self, id_, total, type_="overall", users=None):
        data = {
            "total": total,  # Total time in seconds
            "type": type_,    # Type in ["overall", "users"]
        }

        if users:
            data["users"] = users

        return self._put('/tasks/{0}/estimate'.format(id_), data=data)


class Team(Resource):
    def users(self):
        return self._get('/team/users')

    def timers(self):
        return self._get('/team/timers')


class Timers(Resource):
    def start(self, id_):
        return self._post('/timers', {'task': id_})

    def current(self):
        return self._get('/timers/current')

    def stop(self):
        return self._delete('/timers/current', data=None)


class Projects(Resource):
    def list(self):
        return self._get('/projects')

    def get(self, id_):
        return self._get('/projects/{0}'.format(id_))

    def tasks(self, id_):
        return self._get('/projects/{0}/tasks'.format(id_))


class Webhooks(Resource):
    def create(self, target_url, events, project=None):
        data = {
            "targetUrl": target_url,
            "events": events
        }

        if project:
            data["project"] = project

        return self._post('/hooks', data=data)

    def get(self, id_):
        return self._get('/hooks/{0}'.format(id_))

    def update(self, id_, target_url, events, project=None):
        data = {
            "targetUrl": target_url,
            "events": events
        }

        if project:
            data["project"] = project

        return self._put('/hooks/{0}'.format(id_), data=data)

    def delete(self, id_):
        return self._delete('/hooks/{0}'.format(id_), data={})


class Everhour:
    def __init__(self, token):
        self.session = requests.Session()
        self.session.get(_EVERHOUR_API_URL)
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
