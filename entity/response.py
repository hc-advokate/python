from typing import List, Dict
from enum import Enum


class Response(str):
    code: int = 200
    msg: str = ""
    data: None = None


def response(item: Response):
    return item
