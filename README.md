# transmitter #


### Features ###

This script sends magnet links to a transmission server.


### Usage ###

transmitter.py takes one argument containing the magnet link. The server credentials should be stored in a file called config.json, under the same directory as transmitter.py.

*config.json*
```
{
	"user": "transmission-user",
	"password": "password",
	"host": "host",
	"port": 9091
}
```

command line
```
$ python transmitter.py magnet:?xt=urn:btih:02ca77a6a047fd37f04337437d18f82e61861084&dn=archlinux-2017.04.01-x86_64.iso&tr=udp://tracker.archlinux.org:6969&tr=http://tracker.archlinux.org:6969/announce
```

If you're running OS X, you can use the following applescript in order to create an app which can be used to open magnet links directly from the browser:
```
on open location this_URL
	set transmitter to container of (path to me)
	do shell script "python " & transmitter & "/transmitter/transmitter.py " & this_URL
end open location
```

