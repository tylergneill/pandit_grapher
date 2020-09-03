import pickle

from config import load_config_dict_from_json_file

config_dict = load_config_dict_from_json_file()
jar_fn = config_dict["jar_fn"]

def save_content_to_file(content):
	f = open(jar_fn, 'wb')
	jar = pickle.Pickler(f)
	jar.dump(content) # i.e., dump contents into jar
	f.close()

def load_content_from_file():
	f = open(jar_fn, 'rb')
	content = pickle.load(f)
	f.close()
	return content
