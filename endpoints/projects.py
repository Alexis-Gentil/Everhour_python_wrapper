from .base import Resource


class Projects(Resource):
    def list(self):
        return self._get('/projects')

    def get(self, id_):
        return self._get('/projects/{0}'.format(id_))

    def tasks(self, id_):
        return self._get('/projects/{0}/tasks'.format(id_))
