from .base import Resource


class Team(Resource):
    def users(self):
        return self._get('/team/users')

    def timers(self):
        return self._get('/team/timers')
