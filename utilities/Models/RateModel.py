from utilities.db.db_manager import dbManager

class RateModel:
	def __init__(self):
		pass

	def AddRate(self, toID, fromID, onID, message, rate):
		query = "INSERT INTO Rating(ToID, FromID, OnID, Message, Rate) VALUES(%s, %s, %s, %s, %s)"
		return dbManager.commit(query, (toID, fromID, onID, message, rate,))

rateModel = RateModel()