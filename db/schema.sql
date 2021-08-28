DROP TABLE IF EXISTS vehicle;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS service;
DROP TABLE IF EXISTS departure;
DROP TABLE IF EXISTS arrival;

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

CREATE TABLE user (
    id INTEGER PRIMARY KEY UNIQUE,
    email TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    dateOfBirth DATE NOT NULL,
    type TEXT NOT NULL
);

CREATE TABLE service (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicleId INTEGER NOT NULL,
    userId INTEGER NOT NULL,
    status TEXT NOT NULL,
    createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    type TEXT NOT NULL,
    bookedDays INTEGER,
    bookedForDate DATE,
    bookedForLocationId INTEGER, 
    FOREIGN KEY (vehicleId) REFERENCES vehicle (id),
    FOREIGN KEY (userId) REFERENCES user (id),
    FOREIGN KEY (bookedForLocationId) REFERENCES location (id)
);

CREATE TABLE departure (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    serviceId INTEGER NOT NULL,
    locationId INTEGER NOT NULL,
    createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    totalKm INTEGER NOT NULL,
    FOREIGN KEY (serviceId) REFERENCES service (id),
    FOREIGN KEY (locationId) REFERENCES location (id)
);

CREATE TABLE arrival (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    serviceId INTEGER NOT NULL,
    locationId INTEGER NOT NULL,
    createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    totalKm INTEGER NOT NULL,
    FOREIGN KEY (serviceId) REFERENCES service (id),
    FOREIGN KEY (locationId) REFERENCES location (id)
);

