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
from . import song

class AlbumInfo:
    def __init__(self, info):
        self._notes = get_key(info, 'notes')
        self._mb_id = get_key(info, 'musicBrainzId')
        self._small_url = get_key(info, 'smallImageUrl')
        self._med_url = get_key(info, 'mediumImageUrl')
        self._large_url = get_key(info, 'largeImageUrl')
    
    notes = property(lambda s: s._notes)
    mb_id = property(lambda s: s._mb_id)
    small_url = property(lambda s: s._small_url)
    med_url = property(lambda s: s._med_url)
    large_url = property(lambda s:s._large_url)        


class Album(MediaBase):
    def __init__(self, info):
        self._parent = get_key(info, 'parent')
        self._album = get_key(info, 'album')
        self._title = get_key(info, 'title')
        self._name = info['name']
        self._is_dir = get_key(info, 'isDir')
        self._song_count = info['songCount']
        self._created = info['created']
        self._duration = info['duration']
        self._play_count = get_key(info, 'playCount')
        self._artist_id = get_key(info, 'artistId')
        self._artist = get_key(info, 'artist')
        self._year = get_key(info, 'year')
        self._genre = get_key(info, 'genre')
        self._starred = get_key(info, 'starred')
        self._played = get_key(info, 'played')
        self._user_rating = get_key(info, 'userRating')
        self._songs = []
        self._info = None
        if 'song' in info:
            for entry in info['song']:
                self._songs.append(song.Song(entry))
        super().__init__(info)

    parent = property(lambda s: s._parent)
    album = property(lambda s: s._album)
    title = property(lambda s: s._title)
    name = property(lambda s: s._name)
    is_dir = property(lambda s: s._is_dir)
    song_count = property(lambda s: s._song_count)
    created = property(lambda s: s._created)
    starred = property(lambda s: s._starred)
    duration = property(lambda s: s._duration)
    play_count = property(lambda s: s._play_count)
    artist_id = property(lambda s: s._artist_id)
    artist = property(lambda s: s._artist)
    year = property(lambda s: s._year)
    played = property(lambda s: s._played)
    user_rating = property(lambda s: s._user_rating)
    genre = property(lambda s: s._genre)
    songs = property(lambda s: s._songs)
    mb_id = property(lambda s: s._info.mb_id if s._info is not None else '')

    def set_info(self, info):
        self._info = AlbumInfo(info)
    info = property(lambda s: s._info, set_info)
