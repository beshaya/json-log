==json_log==

A simple python module to load a file consisting of multiple json entries into an array of dictionaries. This is specifically for files that are not single json objects; if you have a file that is a proper json object, just use json.load()!

Usage:
```
import json_log

data = json_log.load("my_logfile.txt")
```

Alternatively, if you have a very large log file, you may want to work one object at a time.

```
import json_log

file = open("my_logfile.json")
object = json_log.readItem(file)
while object != none:
    doStuff(object)
    object = json_log.readItem(file)
file.close()
```