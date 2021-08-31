DROP TABLE IF EXISTS vehicle;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS reservation;
DROP TABLE IF EXISTS rent;

CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY UNIQUE,
    year INTEGER NOT NULL,
    make VARCHAR NOT NULL,
    model VARCHAR NOT NULL,
    motor VARCHAR NOT NULL
);

CREATE TABLE location (
    id INTEGER PRIMARY KEY UNIQUE,
    name VARCHAR NOT NULL
);

CREATE TABLE customer (
    id INTEGER PRIMARY KEY UNIQUE,
    email VARCHAR UNIQUE NOT NULL,
    name VARCHAR NOT NULL,
    dateOfBirth DATE NOT NULL
);

CREATE TABLE reservation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicleId INTEGER NOT NULL,
    customerId INTEGER NOT NULL,
    status VARCHAR NOT NULL,
    createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    bookedTotalDays INTEGER,
    bookedDepartureDatetime DATETIME,
    bookedDepartureLocationId INTEGER,
    bookedArrivedLocationId INTEGER,
    FOREIGN KEY (vehicleId) REFERENCES vehicle (id),
    FOREIGN KEY (customerId) REFERENCES customer (id),
    FOREIGN KEY (bookedDepartureLocationId) REFERENCES location (id),
    FOREIGN KEY (bookedArrivedLocationId) REFERENCES location (id)
);

CREATE TABLE rent (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reservationId INTEGER NOT NULL,
    vehicleId INTEGER NOT NULL,
    customerId INTEGER NOT NULL,
    isCompleted BOOL NOT NULL,
    departureAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    departureLocationId INTEGER NOT NULL,
    arrivedAt TIMESTAMP,
    arrivedLocationId INTEGER,
    FOREIGN KEY (reservationId) REFERENCES reservation (id),
    FOREIGN KEY (vehicleId) REFERENCES vehicle (id),
    FOREIGN KEY (customerId) REFERENCES customer (id),
    FOREIGN KEY (departureLocationId) REFERENCES location (id),
    FOREIGN KEY (arrivedLocationId) REFERENCES location (id)
);
