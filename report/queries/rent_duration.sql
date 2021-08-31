SELECT
    vehicle.id AS vehicle_id,
    vehicle.year AS year,
    vehicle.model AS model,
    COUNT(rent.vehicleId) AS total_rents,
    AVG(strftime('%s', rent.arrivedAt)
        - strftime('%s', rent.departureAt)) AS avg_rent_duration_seconds
FROM vehicle, rent
WHERE vehicle.id=rent.vehicleId
    AND isCompleted=1
    AND rent.departureAt BETWEEN "{date_from}" AND "{date_to}"
GROUP BY
    vehicle_id,
    year,
    model
ORDER BY total_rents DESC;
