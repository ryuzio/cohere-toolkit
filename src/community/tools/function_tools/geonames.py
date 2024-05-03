import os
from typing import Any, Dict

import requests

from community.tools import BaseFunctionTool


class GeoNamesFunctionTool(BaseFunctionTool):
    geonames_username = os.environ.get("GEONAMES_USERNAME")
    geonames_base_url = "https://secure.geonames.org/searchJSON"

    def __init__(self):
        self.username = self.geonames_username
        self.base_url = self.geonames_base_url

    @classmethod
    def is_available(cls) -> bool:
        return cls.geonames_username is not None

    def call(self, parameters: Dict[str, str], **kwargs: Any) -> Dict[str, Any]:
        to_query = {
            "username": self.username,
            "q": parameters.get("name", ""),
            "country": parameters.get("country", None),
            "maxRows": 1,
            "orderBy": "relevance",
        }
        result = self._query_geonames(to_query)
        print(result)
        return {"result": result, "text": result}

    def _query_geonames(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        resp = requests.post(self.base_url, data=payload, timeout=60)
        geonames = resp.json().get("geonames", [])

        return geonames[0] if geonames else {}
