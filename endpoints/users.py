from .base import Resource


class Users(Resource):
    def me(self):
        return self._get('/users/me')

    def time(self, id_='me'):
        return self._get('/users/{0}/time'.format(id_))
