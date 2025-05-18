"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("A28177885", None)
        self.API_HASH: str = os.environ.get("95187ed775c3890e46a703dd9d77c66d", None)
        self.SESSION: str = os.environ.get("1BVtsOKEBuydjAgw0UVETv9N_ScgSsQ1Djxmrxyj5qaHJ8dVKxSUepNsZ_Jr4sLD7vApEMRcufAK0V0q_az8PNz0OlYFU8tFZFuU3E3ZCDYKZEDTnCwHGGzJfagkJ9Rq3USP64th7ngtrBX-v9tyBhjlSQvrekEcMyv5IZLU2Qjqxqb6e6NGvUkn9bWo9yUyFpjR1ppx3IHVgfU1XYbdgmwXVRrsPK0fOfcMBcyl7qWb3JGb9_08UJESSugGSgfuyLoMbFk3lQl1K8HNWPUc80P4yZzLi2Q4viFuO-Ik07Bhquh1UhWFljwn6BXPhWKx89Kj06luTtYXK1YvFZvHcLQBsxpXw89M=", None)
        self.BOT_TOKEN: str = os.environ.get("7659302775:AAEkcw_F-XCdj-COOkDa4RWfAoEV8PPmW7M", None)
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("7165187197", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
