class TitleCrew:
    def __init__(self, dict):
        self.tconst = dict['tconst']
        self.directors = None if dict['directors'] == "\\N" else dict['directors'].split(
            ',')
        self.writers = None if dict['writers'] == "\\N" else dict['writers'].split(
            ',')

    @staticmethod
    def dict_to_object(list):
        objects = []
        for item in list:
            objects.append(TitleCrew(item))

        return objects
