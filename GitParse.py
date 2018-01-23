from jsonpath_ng.ext import parse
import urllib
import json
import objectpath

#https://gist.github.com/caspyin/2288960 how to read github


def ParseJson(url):
	
	f = urllib.urlopen(url)
	json_data = f.read()
	#jdata = json.load(json_api)
	tree_obj = objectpath.Tree(json_data)
	print tuple(tree_obj.execute('$..symbol'))

def ReadJson(url):
	abilityname = "RLC"
	propertyname = "manufacturer"
	f = urllib.urlopen(url)
	json_api = f.read()
	#jsonpath(impi_node, "$.sensor[?(@.sensor_type=='Temperature')]")
	result = parse("$.symbol=='RLC'").find(json_api)
	

	#parse('$[?(@.name=="' + abilityname + '")].properties[?(@.name=="' + propertyname + '")]').find(url)
	print result
	if len(result) == 1:
	    print result[0]
	    return str(result[0].value['value'])
	else:
	    return ""

#print (ParseJson("https://api.coinmarketcap.com/v1/ticker/?start=10&limit=500"))
print (ReadJson("https://api.coinmarketcap.com/v1/ticker/?start=10&limit=500"))
#print (ReadJson("https://api.github.com/users/dadi/repos"))
'''
import json
from pprint import pprint
json_data=open('bookmarks.json')
jdata = json.load(json_data)
pprint (jdata)
json_data.close()

{abilities": [
            {
          ...
                "name": "dadi",
                "properties": [
                    {
                        "name": "manufacturer",
                        "value": "xxxx",
                    },
                    {
                        "name": "product",
                        "value": "yyy",

                    }
                ],
                "type": "device_info"
            },
            {....}
            ]}
'''    