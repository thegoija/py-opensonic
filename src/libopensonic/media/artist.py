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
from .album import Album

class ArtistInfo:
    """
    Holds extra (optional) artist info
    """
    def __init__(self, info):
        self._biography = get_key(info, 'biography')
        self._mb_id = info['musicBrainzId']
        self._small_url = get_key(info, 'smallImageUrl')
        self._med_url = get_key(info, 'mediumImageUrl')
        self._large_url = get_key(info, 'largeImageUrl')
    
    biography = property(lambda s: s._biography)
    mb_id = property(lambda s: s._mb_id)
    small_url = property(lambda s: s._small_url)
    med_url = property(lambda s: s._med_url)
    large_url = property(lambda s:s._large_url)


class Artist(MediaBase):
    """
    A subsonic Artist
    """
    def __init__(self, info):
        """
        Builds an Artist object

        info:dict                   A dict from the JSON response to getArtist
                                    Must contain fields for MedaiBase and 'name',
                                    'starred, 'albumCount', and 'album' though 'album'
                                    is a list and can be an empty one
        """
        self._album_count = get_key(info, 'albumCount')
        self._starred = get_key(info, 'starred')
        self._name = info['name']
        self._info = None
        self._albums = []
        if 'album' in info:
            for entry in info['album']:
                self._albums.append(Album(entry))
        super().__init__(info)

    album_count = property(lambda s: s._album_count)
    starred = property(lambda s: s._starred)
    name = property(lambda s: s._name)
    albums = property(lambda s: s._albums)
    info = property(lambda s: s._info)
