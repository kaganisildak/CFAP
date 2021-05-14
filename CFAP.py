HOSTNAME = "git.company.com"

class AddHeader:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        if HOSTNAME in flow.request.host:
            flow.request.headers["cf-access-token"] = "TOKEN"
            
addons = [
    AddHeader()
]
