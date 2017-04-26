scores = {"Bob": 10, "Joe":3, "Jack": 6, "Jane": 15}

print scores.get("Joe", 0)
print scores.get("Jack", 0)
print scores.get("Grace", 0)

graces_dict = {"a":1, "b":2, "c":3}

# .items() returns a list of key, value in tuples form but unpacking 2 item tuple into key and value variables

for key, value in graces_dict.items():
    print "key = {}, value = {}".format(key, value)



for key, value in graces_dict.iteritems():
    print key, value

#.iteritems() returns an object that can be looped over and returns individual (key, value) tuples each time you loop over it. However, it does not return an actual list of these of these items — just an object you can loop over. As such, you can’t print this object to get a full representation, like you would a list, nor can you index it, or use list slicing on it. This type of object, one that you can loop over but isn’t an actual collection, is called a generator — it can “generate” the next item, but it’s not a complete list.






















