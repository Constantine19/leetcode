class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.lookup:
            self.lookup[key] = []
        self.lookup[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """


"""
inputs = ["TimeMap",    "set",              "get",      "get",      "set",              "get",      "get"],
inputs = [[],           ["foo","bar",1],    ["foo",1],  ["foo",3],  ["foo","bar2",4],   ["foo",4],  ["foo",5]]
output = [null,         null,               "bar",      "bar",      null,               "bar2",     "bar2"]
                        foo: bar, 1         bar         bar         foo:bar2, 4         bar2        
"""

"""
inputs = ["TimeMap",    "set",                  "set",              "get",          "get",          "get",          "get",          "get"]
inputs = [[],           ["love","high",10],     ["love","low",20],  ["love",5],     ["love",10],    ["love",15],    ["love",20],    ["love",25]]
output = [null,         null                    null                low             high            low             low             low]
output = [null,         null,                   null,               "",             "high",         "high",         "low",          "low"]
"""