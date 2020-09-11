import pickle

from config import load_config_dict_from_json_file

config_dict = load_config_dict_from_json_file()
pickle_jar_fn = config_dict["pickle_jar_fn"]

def save_content_to_file(content):
	f = open(pickle_jar_fn, 'wb')
	jar = pickle.Pickler(f)
	jar.dump(content) # i.e., dump contents into jar
	f.close()

def load_content_from_file():
	f = open(pickle_jar_fn, 'rb')
	content = pickle.load(f)
	f.close()
	return content
