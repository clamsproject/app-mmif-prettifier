"""app.py

Application to format the MMIF input.

"""


from clams.serve import ClamsApp
from clams.restify import Restifier
from mmif.serialize import *


class Prettifier(ClamsApp):

    def setupmetadata(self):
        return {
            "name": "MMIF Prettifier",
            "app": 'https://apps.clams.ai/tokenizer',
            "app_version": "0.0.1",
            "tool_version": "0.0.1",
            "mmif-spec-version": "0.2.1",
            "mmif-sdk-version": "0.2.0",
            "clams-version": "0.1.3",
            "description": "This tool takes MMIF input and formats it.",
            "vendor": "Team CLAMS",
            "requires": [],
            "produces": []
        }

    def sniff(self, mmif):
        # this mock-up method always returns true
        return True

    def annotate(self, mmif):
        self.mmif = mmif if type(mmif) is Mmif else Mmif(mmif)
        return self.mmif.serialize(pretty=True)


if __name__ == "__main__":

    app = Prettifier()
    service = Restifier(app)
    service.run()
