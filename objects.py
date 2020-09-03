class Entity(object):
	def __init__(self, id):
		self.id = id		# 5-digit string
		self.name = ''		# human-readable label: work title or author name

class Work(Entity):
	def __init__(self, id):
		Entity.__init__(self, id)
		self.type = 'work'
		self.author_ids = []	# list of 5-digit strings
		self.base_text_ids = [] # list of 5-digit strings
		self.commentary_ids = [] # list of 5-digit strings

class Author(Entity):
	def __init__(self, id):
		Entity.__init__(self, id)
		self.type = 'author'
		self.work_ids = []		# list of 5-digit strings
