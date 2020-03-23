class TitleAkas:
    def __init__(self, dict):
        self.titleId = dict['titleId']
        self.ordering = int(dict['ordering'])
        self.title = dict['title']
        self.region = None if dict['region'] == '\\N' else dict['region']
        self.language = None if dict['language'] == '\\N' else dict['language']
        self.types = None if dict['types'] == '\\N' else dict['types']
        self.attributes = None if dict['attributes'] == '\\N' else dict['attributes']
        self.isOriginalTitle = None if dict['isOriginalTitle'] == '\\N' else int(
            dict['isOriginalTitle'])

    @staticmethod
    def dict_to_object(list):
        objects = []
        for item in list:
            objects.append(TitleAkas(item))

        return objects
