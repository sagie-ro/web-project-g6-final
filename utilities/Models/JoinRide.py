from utilities.db.db_manager import dbManager


class JoinRideModel:
    def __init__(self):
        pass

    def JoinRide(self, passengerID, RideID, pick, drop, msg):
        query = "INSERT INTO joinride(RideID, passengerID, pickup, dropoff, message) VALUES(%s, %s, %s, %s, %s)"
        return dbManager.commit(query, (RideID, passengerID, pick, drop, msg,))

    def ViewMyRides(self, passengerID):
        query = "SELECT rides.ID AS ID, rides.DepartureTime AS DepartureTime, joinride.pickup AS Origin, joinride.dropoff AS Destination, rides.Seats AS Seats, rides.Price AS Price, rides.Pets AS Pets, rides.Mask AS Mask, rides.Smoking AS Smoking, rides.Comment AS Comment, Driver.Name AS DriverName, Driver.ID AS DriverID FROM  rides, users As Driver, joinride WHERE Driver.ID=rides.DriverID AND rides.ID=joinride.RideID AND joinride.passengerID=%s"
        return dbManager.fetch(query, (passengerID,))

    def ViewMyPassengers(self, RideID):
        query = "SELECT joinride.ID AS ID, Passenger.Name AS Name, Passenger.ID AS PassengerID, joinride.pickup AS PickUP, joinride.dropoff AS DropOff FROM users AS Passenger, joinride WHERE Passenger.ID=joinride.passengerID AND joinride.RideID=%s"
        return dbManager.fetch(query, (RideID,))


joinRideModel = JoinRideModel()
