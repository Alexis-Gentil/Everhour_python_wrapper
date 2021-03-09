from .base import Resource


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
