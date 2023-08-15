CREATE TABLE Users (
    users_id int NOT NULL,
    banned ENUM ('Yes', 'No'),
    role ENUM ('client', 'driver', 'partner'),
    PRIMARY KEY (users_id));

CREATE TABLE Trips (
    id int NOT NULL,
    client_id int NOT NULL,
    driver_id int NOT NULL,
    city_id int,
    status ENUM ('completed', 'cancelled_by_driver', 'cancelled_by_client'),
    request_at date,
    PRIMARY KEY (id),
    FOREIGN KEY (client_id) REFERENCES Users(users_id),
    FOREIGN KEY (driver_id) REFERENCES Users(users_id));

INSERT INTO Users(users_id,banned,role)
VALUES
(1,'No','client'),(2,'Yes','client'),(3,'No','client'),(4,'No','client'),(10,'No','driver'),(11,'No','driver'),(12,'No','driver'),(13,'No','driver');

INSERT INTO Trips(id,client_id,driver_id,city_id,status,request_at)
VALUES
(1,1,10,1,'completed','2013-10-01'),(2,2,11,1,'cancelled_by_driver','2013-10-01'),(3,3,12,6,'completed','2013-10-01'),(4,4,13,6,'cancelled_by_client','2013-10-01'),(5,1,10,1,'completed','2013-10-02'),(6,2,11,6,'completed','2013-10-02'),(7,3,12,6,'completed','2013-10-02'),(8,2,12,12,'completed','2013-10-03'),(9,3,10,12,'completed','2013-10-03'),(10,4,13,12,'cancelled_by_driver','2013-10-03');

SELECT t.request_at `Day`, ROUND(SUM(CASE WHEN t.status IN ('cancelled_by_driver','cancelled_by_client') AND u.banned <> 'Yes' THEN
1 ELSE 0 END)/SUM(CASE WHEN u.banned <> 'Yes' THEN 1 ELSE 0 END),2) `Cancellation Rate` FROM Users u INNER JOIN Trips t  ON u.users_id = t.
client_id  GROUP BY Day;
