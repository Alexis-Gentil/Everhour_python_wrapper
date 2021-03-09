import json

EVERHOUR_API_URL = 'https://api.everhour.com'


class Resource:
    def __init__(self, api):
        self._api = api
        self._session = api.session

    def _get(self, url):
        return self._session.get(EVERHOUR_API_URL + url).json()

    def _post(self, url, data):
        return self._session.post(EVERHOUR_API_URL + url, data=json.dumps(data)).json()

    def _put(self, url, data):
        return self._session.put(EVERHOUR_API_URL + url, data=json.dumps(data)).json()

    def _delete(self, url, data):
        return self._session.delete(EVERHOUR_API_URL + url, data=json.dumps(data))
