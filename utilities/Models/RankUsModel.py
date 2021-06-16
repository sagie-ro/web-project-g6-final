from utilities.db.db_manager import dbManager

class RankUsModel:
	def __init__(self):
		pass

	def AddRank(self, ID, Rate, Message):
		query = "INSERT INTO rateus(UserID, Rate, Message) VALUES(%s, %s, %s)"
		return dbManager.commit(query, (ID, Rate, Message,))

rankUsModel = RankUsModel()