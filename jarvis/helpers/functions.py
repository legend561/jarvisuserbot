import os
import re
import time
import urllib.request
import zipfile
from random import choice

import PIL.ImageOps
import requests
from PIL import Image
from telethon.tl.types import Channel, PollAnswer
from validators.url import url


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, "", inputString)
