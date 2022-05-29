from django.http import QueryDict
import json
from rest_framework import parsers

class MultipartJsonParser(parsers.MultiPartParser):

    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(
            stream,
            media_type=media_type,
            parser_context=parser_context
        )
        print(1, result.data["shop"])
        data = {}
        # find the data field and parse it
        data = json.loads(result.data["shop"])
        print(2)
        qdict = QueryDict('', mutable=True)
        qdict.update(data)
        return parsers.DataAndFiles(qdict, result.files)