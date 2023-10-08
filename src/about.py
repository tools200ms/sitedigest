
class About:
    NAME = "Sitedigest"
    AUTHOR = "Mateusz Piwek"
    VERSION = "0.0.1 - prelease"

    @staticmethod
    def getAbout():
        return "  Sitedigest - version: %s\n      by %s" % (About.VERSION, About.AUTHOR)

