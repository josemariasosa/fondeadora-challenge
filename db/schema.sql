DROP TABLE IF EXISTS vehicle;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS reservation;
DROP TABLE IF EXISTS rent;

CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY UNIQUE,
    year INTEGER NOT NULL,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    motor TEXT NOT NULL
);

CREATE TABLE location (
    id INTEGER PRIMARY KEY UNIQUE,
    name TEXT NOT NULL
);

CREATE TABLE customer (
    id INTEGER PRIMARY KEY UNIQUE,
    email TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    dateOfBirth DATE NOT NULL
);

CREATE TABLE reservation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicleId INTEGER NOT NULL,
    customerId INTEGER NOT NULL,
    status TEXT NOT NULL,
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
    deparetureAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deparetureLocationId INTEGER NOT NULL,
    arrivedAt TIMESTAMP,
    arrivedLocationId INTEGER,
    FOREIGN KEY (reservationId) REFERENCES reservation (id),
    FOREIGN KEY (vehicleId) REFERENCES vehicle (id),
    FOREIGN KEY (customerId) REFERENCES customer (id),
    FOREIGN KEY (deparetureLocationId) REFERENCES location (id),
    FOREIGN KEY (arrivedLocationId) REFERENCES location (id)
);
