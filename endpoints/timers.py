from .base import Resource


class Timers(Resource):
    def start(self, id_):
        return self._post('/timers', {'task': id_})

    def current(self):
        return self._get('/timers/current')

    def stop(self):
        return self._delete('/timers/current', data=None)
