from utilities.db.db_manager import dbManager

class RideModel:
	def __init__(self):
		pass

	def AddRide(self,driver,  date, origin, destination, price, seats, animals, masks, smoke, msg):
		query = "INSERT INTO rides(DriverID, DepartureTime, Origin, Destination, Price, Seats, Mask, Pets, Smoking, Comment, Status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'RUNNING')"
		return dbManager.commit(query, (driver, date, origin, destination, price, seats, masks, animals, smoke, msg,))


	def ViewRides(self, origin, destination, date, animals, masks, smoke):
		query = "SELECT rides.ID AS ID, rides.DepartureTime AS DepartureTime, rides.Origin AS Origin, rides.Destination AS Destination, rides.Seats AS Seats, rides.Price AS Price, rides.Pets AS Pets, rides.Mask AS Mask, rides.Smoking AS Smoking, rides.Comment AS Comment, Driver.Name AS DriverName, rides.DriverID AS DriverID FROM rides, users As Driver WHERE Driver.ID=rides.DriverID AND %s IN (NULL, '', rides.Origin) AND %s IN (NULL, '', rides.Destination) AND %s IN (NULL, '', rides.DepartureTime) AND %s in (null, '', rides.Smoking) AND %s in (null, '', rides.mask) AND %s in (null, '', rides.Pets) AND rides.Status='RUNNING'"
		return dbManager.fetch(query, (origin, destination, date, smoke, masks, animals,))

	def ViewAll(self):
		query = "SELECT rides.ID AS ID, rides.DepartureTime AS DepartureTime, rides.Origin AS Origin, rides.Destination AS Destination, rides.Seats AS Seats, rides.Price AS Price, rides.Pets AS Pets, rides.Mask AS Mask, rides.Smoking AS Smoking, rides.Comment AS Comment, Driver.Name AS DriverName, rides.DriverID AS DriverID FROM rides, users As Driver WHERE Driver.ID=rides.DriverID AND rides.Status='RUNNING'"
		return dbManager.fetch(query)

	def ViewMyRides(self, driverID):
		query = "SELECT rides.ID AS ID, rides.DepartureTime AS DepartureTime, rides.Origin AS Origin, rides.Destination AS Destination, rides.Seats AS Seats, rides.Price AS Price, rides.Pets AS Pets, rides.Mask AS Mask, rides.Smoking AS Smoking, rides.Comment AS Comment, Driver.Name AS DriverName, rides.Status AS Status, rides.DriverID AS DriverID FROM rides, users As Driver WHERE Driver.ID=rides.DriverID AND rides.DriverID=%s"
		return dbManager.fetch(query, (driverID,))

	def MarkAsEnd(self, rideID):
		query = "UPDATE rides SET Status='END' WHERE ID=%s"
		return dbManager.commit(query, (rideID,))

rideModel = RideModel()