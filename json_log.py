'''
json_log.py

A dead simple module that reads a file and converts json objects to array elements
Does bracket and quote matching to handle nested objects
'''

import json

diagnostic = False

# Read the entirety of a file as dictionaries
def read(filename):
    file = open(filename)
    contents = [readItem(file)]
    while contents[-1] != None:
        contents.append(readItem(file))
    contents.pop()
    file.close()
    return contents

# Read the next json item from the file
def readItem(file):
    # Read until next '{'
    nextChar = 0
    while nextChar != '{' and nextChar != '':
        nextChar = file.read(1)

    if nextChar == '':
        return None
    # Store until complete
    objectBuilder = ObjectBuilder()
    objectBuilder.addChar(nextChar)
    while not objectBuilder.isComplete() and nextChar != '':
        nextChar = file.read(1)
        objectBuilder.addChar(nextChar)

    if not objectBuilder.isComplete():
        return None
    if diagnostic:
        print objectBuilder.getObject()
    # Parse JSON Object
    return json.loads(objectBuilder.getObject())

# Helper class to keep track of characters that effect where the object ends
class ObjectBuilder:
    def __init__(self):
        self.openBrackets = 0
        self.inQuotes = False
        self.escaped = False
        self.object = ""
        
    # Add a character and keep track of opened brackets
    # (To do so, must be quote-aware, and to do that, must be escape-aware)
    # (This got way more complicated than I hoped)
    def addChar(self, char):
        if self.escaped:
            self.escaped = False
        elif char == '{':
            if not self.inQuotes:
                self.openBrackets += 1
        elif char == '}':
            if not self.inQuotes:
                self.openBrackets -= 1
        elif char == '\\':
            if self.inQuotes:
                self.escaped = True
        elif char == '"':
            self.inQuotes = not self.inQuotes
        self.object += char
            
    def isComplete(self):
        return self.openBrackets == 0
        
    def getObject(self):
        return self.object

if __name__ == '__main__':
    import sys
    testFile = "test.json"
    if len(sys.argv) > 1:
        testFile = sys.argv[1]

    print "Loading " + testFile + ":"
    print read(testFile)