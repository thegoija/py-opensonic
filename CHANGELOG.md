##3.0.6

Objects missing required fields now report a warning using the warnings module instead of raising a
KeyError.

##3.0.5

Fat fingered a release...

##3.0.3

Give most objects a to_dict() method for easier dumping of values

##3.0.2

Acutally bump _version.py

##3.0.1

Remove accidental print statement in search3 return path, fix song parsing

##3.0.0

Use new media.Playlist object for interacting with playlists. All status only returns now return True on success.

##2.0.1

Fix result parsing in search3, allow for empty artist, album, or song field.

## 2.0.0

Create objects for many of the returns from the api end points and rewored Connection object to use these new classes.

## 1.0.1

Python packaging learning curve. The previous version seems to have built empty
libraries, hopefully this has fixed the problem.

## 1.0.0

Initial release of forked library with Open Subsonic endpoint extensions supported.
