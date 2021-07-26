#     MIT License
#
#      Copyright (c) 2021-present Simon Olofsson
#
#      Permission is hereby granted, free of charge, to any person obtaining a copy
#      of this software and associated documentation files (the "Software"), to deal
#      in the Software without restriction, including without limitation the rights
#      to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#      copies of the Software, and to permit persons to whom the Software is
#      furnished to do so, subject to the following conditions:
#
#      The above copyright notice and this permission notice shall be included in all
#      copies or substantial portions of the Software.
#
#      THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#      IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#      FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#      AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#      LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#      OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#      SOFTWARE.
from pyttman import Feature
from pyttman.core.communication.command import Command
from pyttman.core.communication.models.containers import MessageMixin, Reply
from pyttman.core.parsing.identifiers import CapitalizedIdentifier
from pyttman.core.parsing.parsers import ValueParser, ChoiceParser


class PlayMusic(Command):
    lead = ("play",)

    """
    Define the EntityParser inside the Command class and 
    create fields, named as you want them to be named when
    accessing them through self.entities.get(). 
    """

    class EntityParser(Command.EntityParser):
        song = ValueParser(identifier=CapitalizedIdentifier, prefixes=("play",), span=10)
        artist = ValueParser(identifier=CapitalizedIdentifier, prefixes=("by",), span=2)
        platform = ChoiceParser(choices=("Spotify", "SoundCloud", "YouTubeMusic"))

    def respond(self, message: MessageMixin) -> Reply:
        song = self.entities.get("song")
        artist = self.entities.get("artist")
        platform = self.entities.get("platform")
        return Reply(f"Playing {song} by {artist} on {platform}.")


class MusicFeature(Feature):
    commands = (PlayMusic,)
