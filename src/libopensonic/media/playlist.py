"""
This file is part of py-opensonic.

py-opensonic is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-opensonic is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with py-opensonic.  If not, see <http://www.gnu.org/licenses/>
"""

from .media_base import MediaBase, get_key
from .song import Song

class Playlist(MediaBase):
    def __init__(self, info):
        self._name = info['name']
        self._comment = get_key(info, 'comment')
        self._owner = get_key(info, 'owner')
        self._public = get_key(info, 'public')
        self._song_count = info['songCount']
        self._created = info['created']
        self._changed = info['changed']
        self._duration = info['duration']
        self._cover_id = get_key(info, 'coverArt')
        self._songs = []
        if 'entry' in info:
            for entry in info['entry']:
                self._songs.append(Song(entry))
        self._allowed_users = get_key(info, 'allowedUser')
        super().__init__(info)

    name = property(lambda s: s._name)
    comment = property(lambda s: s._comment)
    owner = property(lambda s: s._owner)
    public = property(lambda s: s._public)
    song_count = property(lambda s: s._song_count)
    created = property(lambda s: s._created)
    changed = property(lambda s: s._changed)
    duration = property(lambda s: s._duration)
    songs = property(lambda s: s._songs)
    cover_id = property(lambda s: s._cover_id)
