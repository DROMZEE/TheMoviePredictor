class TitleEpisode:
    def __init__(self, dict):
        self.tconst = dict['tconst']
        self.parentTconst = None if dict['parentTconst'] == "\\N" else dict['parentTconst']
        self.seasonNumber = None if dict['seasonNumber'] == "\\N" else int(
            dict['seasonNumber'])
        self.episodeNumber = None if dict['episodeNumber'] == "\\N" else int(
            dict['episodeNumber'])

    @staticmethod
    def dict_to_object(list):
        objects = []
        for item in list:
            objects.append(TitleEpisode(item))

        return objects
