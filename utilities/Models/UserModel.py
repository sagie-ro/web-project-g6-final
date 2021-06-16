from utilities.db.db_manager import dbManager

class UserModel:
	def __init__(self):
		pass

	def Login(self, email, password):
		query = "SELECT ID FROM users WHERE email=%s AND password=MD5(%s)"
		return dbManager.fetch(query, (email, password,))

	def Register(self, name, email, dob, password, fb, license, num, comp, model, phone, profile):
		query = "INSERT INTO users(Name, Email, DOB, Password, FacebookLink, LicenseNumber, CarNumber, Company, CarModel, Phone, Profile) VALUES(%s, %s, %s, MD5(%s), %s, %s, %s, %s, %s, %s, %s)"
		return dbManager.commit(query, (name, email, dob, password, fb, license, num, comp, model, phone, profile,))

	def GetUser(self, ID):
		query = "SELECT ID, Name, Email, Phone, Profile, FacebookLink, LicenseNumber, CarNumber, CarModel, Company, (SELECT AVG(Rate) FROM Rating, rides WHERE rides.ID=Rating.OnID AND Rating.ToID=rides.DriverID AND rides.DriverID=%s) AS DriverRating, (SELECT AVG(Rate) FROM Rating, joinride WHERE Rating.OnID=joinride.RideID AND joinride.PassengerID=Rating.ToID AND joinride.passengerID=%s) AS PassengerRating, (SELECT COUNT(ID) FROM rides WHERE DriverID=%s) AS NumberOfRides, DOB FROM users WHERE ID=%s"
		return dbManager.fetch(query, (ID, ID, ID, ID,))

	def Update(self, ID, name, email, dob, password, fb, license, num, comp, model, phone, profile):
		query = "UPDATE users SET Name=%s, Email=%s, DOB=%s, password=MD5(%s), FacebookLink=%s, LicenseNumber=%s, CarNumber=%s, Company=%s, CarModel=%s, Phone=%s, Profile=%s WHERE ID=%s"
		return dbManager.commit(query, (name, email, dob, password, fb, license, num, comp, model, phone, profile, ID))

userModel = UserModel()