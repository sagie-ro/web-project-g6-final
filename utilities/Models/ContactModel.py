from utilities.db.db_manager import dbManager


class ContactModel:
    def __init__(self):
        pass

    def AddContact(self, name, userID, email, message):
        query = "INSERT INTO contact(Name, userID, Email, Message) VALUES(%s, %s, %s, %s)"
        return dbManager.commit(query, (name, userID, email, message,))

    def ViewMyMessages( userID):
        # query = "SELECT contact.ID AS ID,  contact.Message AS Message,  FROM  contact WHERE contact.ID  = %s"
        query = "SELECT * FROM contact WHERE contact.userID = %s"
        return dbManager.fetch(query, (userID,))

    def deleteMessage( ID):
        query = "DELETE FROM contact WHERE contact.ID = %s"
        return dbManager.commit(query, (ID,))


contactModel = ContactModel()

