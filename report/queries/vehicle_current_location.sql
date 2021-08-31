SELECT
    vehicle.id AS vehicle_id,
    vehicle.year AS year,
    vehicle.model AS model,
    location.name AS current_location,
    max(rent.arrivedAt) AS since
FROM rent, vehicle
LEFT JOIN location ON location.id=rent.arrivedLocationId
WHERE vehicle.id=rent.vehicleId
    AND rent.isCompleted=1
GROUP BY vehicle_id, year, model;
