class User(object):
    def __init__(self, fontysId, jobbyId, authToken, refreshToken):
        self.fontysId = fontysId
        self.jobbyId = jobbyId
        self.authToken = authToken
        self.refreshToken = refreshToken

    @staticmethod
    def from_dict(source):
        return User(source['fontysId'], source['jobbyId'],
                    source['authToken'], source['refreshToken'])

    def to_dict(self):
        return dict(
            (key, value)
            for (key, value) in self.__dict__.items()
        )

    def __repr__(self):
        return (
            u'City(fontysId = {}, jobbyId = {}, authToken = {}, refreshToken = {}'
                .format(self.fontysId, self.jobbyId, self.authToken, self.refreshToken)
        )
