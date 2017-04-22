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
```
$ python transmitter.py magnet:?xt=urn:btih:02ca77a6a047fd37f04337437d18f82e61861084&dn=archlinux-2017.04.01-x86_64.iso&tr=udp://tracker.archlinux.org:6969&tr=http://tracker.archlinux.org:6969/announce
```

### OS X ###
If you're running OS X, you can use the included transmitter.app when opening magnet links from the browser.

Here is the AppleScript needed to create transmitter.app in case you need to rebuild the application:
```
on open location this_URL
	set transmitter to container of (path to me)
	do shell script "python " & transmitter & "/transmitter/transmitter.py " & this_URL
end open location
```

