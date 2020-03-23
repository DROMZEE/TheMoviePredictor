class NameBasics:
    def __init__(self, dict):
        self._id = dict['nconst']
        self.nconst = dict['nconst']
        self.primaryName = dict['primaryName']
        self.birthYear = None if dict['birthYear'] == "\\N" else int(
            dict['birthYear'])
        self.deathYear = None if dict['deathYear'] == "\\N" else int(
            dict['deathYear'])
        self.primaryProfession = dict['primaryProfession'].split(",")
        self.knownForTitles = dict['knownForTitles'].split(",")

    @staticmethod
    def dict_to_object(list):
        objects = []
        for item in list:
            objects.append(NameBasics(item))

        return objects
