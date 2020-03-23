class TitleBasics:
    def __init__(self, dict):
        self._id = dict['tconst']
        self.tconst = dict['tconst']
        self.titleType = dict['titleType']
        self.primaryTitle = dict['primaryTitle']
        self.originalTitle = dict['originalTitle']
        self.isAdult = int(dict['isAdult'])
        self.startYear = None if dict['startYear'] == "\\N" else int(
            dict['startYear'])
        self.endYear = None if dict['endYear'] == "\\N" else int(
            dict['endYear'])
        self.runtimeMinutes = None if dict['runtimeMinutes'] == "\\N" else int(
            dict['runtimeMinutes'])
        self.genres = [] if dict['genres'] == "\\N" else dict['genres'].split(
            ",")

    @staticmethod
    def dict_to_object(list):
        objects = []
        for item in list:
            objects.append(TitleBasics(item))

        return objects
