class Sql_Statement(object):
	def __init__(self, table, registry=[]):
		self.table = table 
		self.registry = registry

# Create Select Statement Method
	def select(self, values=[], parameters=[]):
		if len(self.registry) == 0:
			sql_query = "SELECT * FROM " + self.table
		else:
			sql_query = "SELECT " + self.registry + " FROM " + self.table
			
		count = len(parameters)
		if count == 0:
			condition = ""
		else:
			condition = " WHERE "
	
		while count > 0:
			if count == 1 :
				condition = condition +  parameters[count-1] + " = '" + values[count-1] + "' "
			else:
				condition = condition + parameters[count-1] + " = '" + values[count-1] + "' and "
			count -= 1		
	
		sql_query = sql_query + condition + ';'
		return sql_query

# Create Insert Statement Method
	def insert(self, parameters, values):
		sql_query = "INSERT INTO " + self.table + " ("
		count = 0
		while count < len(parameters):
			sql_query += parameters[count] 
			if count != len(parameters)-1:
				sql_query += ","
			count += 1
		
		sql_query = sql_query + ") VALUES ("
		count = 0
		while count < len(values):
			sql_query += "'" + values[count] + "'"
			if count != len(values)-1:
				sql_query += ","
			count += 1
		
		sql_query = sql_query + ")"
		return sql_query
		 
		 
# Create Update Statement Method
	def update(self, parameters, values, user_parm, user_value):
		sql_query = "UPDATE " + self.table + " SET "
		count = 0
		while count < len(parameters):
			sql_query += parameters[count] + "='" + values[count] + "'"
			if count != len(parameters)-1:
				sql_query += ","
			count += 1
		
		sql_query += " WHERE " + user_parm + "='" + user_value + "';"
		return sql_query
		