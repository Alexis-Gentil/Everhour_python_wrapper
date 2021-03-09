from .base import Resource


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
