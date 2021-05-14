HOSTNAME = "git.company.com"
TOKEN_PATH = "token.conf"

class AddHeader:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        if HOSTNAME in flow.request.host:
            flow.request.headers["cf-access-token"] = open(TOKEN_PATH,"r").read()
addons = [
    AddHeader()
]
