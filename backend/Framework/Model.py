import inspect
from json import JSONEncoder

class ModelParaJson(JSONEncoder):
    def default(self, o):
    	obj = {}
    	for name, method in inspect.getmembers(o, predicate=inspect.ismethod):
    		if(name[:3] == "get"):
    			obj[self.convert(name[3:])] = method()
        return obj

    def convert(self,name):
	    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
	    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

	def naoEstaNaListaNegra(self,o):
		pass
