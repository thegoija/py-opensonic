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


def get_key(item, key):
    """
    Quality of life helper function to give the keyed value if it exists,
    None otherwise.
    """
    return item[key] if key in item else None


class Cover:
    def __init__(self, my_type, my_bytes):
        self._type = my_type
        self._bytes = my_bytes
    type = property(lambda s: s._type)
    bytes = property(lambda s: s._bytes)


class MediaBase:
    """
    Base class for media items, this class should not be used directly
    """
    def __init__(self, info):
        """
        The Media class consolidates fields and methods common to all "Media" things
        (e.g. Songs, Albums, Artists, Podcasts, etc)

        info:dict                           A dict from the JSON response to any get request
                                            Must contain fields 'id' and 'coverArt'
        """
        self._id = info['id']
        self._cover_id = get_key(info, 'coverArt')
        self._cover = None

    def to_dict(self):
        return {'id': self._id, 'coverId': self.cover_id}
    
    id = property(lambda s: s._id)
    cover_id = property(lambda s: s._cover_id)

    def unpack_cover(self, res):
        """
        Cache the actual cover for this media

        res: HttpResponse object            The response object we got back from getCoverArt
        """
        self._cover = Cover(res.info().getheader('Content-Type'), bytearray(res.read()))
    cover = property(lambda s: s._cover, unpack_cover)
