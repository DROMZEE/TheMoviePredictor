import json


class TitlePrincipals:
    def __init__(self, dict):
        self.tconst = dict['tconst']
        self.ordering = int(dict['ordering'])
        self.nconst = dict['nconst']
        self.category = dict['category']
        self.job = None if dict['job'] == '\\N' else dict['job']
        self.characters = None if dict['characters'] == '\\N' else json.loads(
            dict['characters'])

    @staticmethod
    def dict_to_object(list):
        objects = []
        for item in list:
            objects.append(TitlePrincipals(item))

        return objects
