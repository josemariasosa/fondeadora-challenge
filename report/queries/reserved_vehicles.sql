SELECT 
    vehicle.id AS vehicle_id,
    vehicle.year AS year,
    vehicle.model AS model,
    COUNT(reservation.id) AS total_reservations
FROM vehicle, reservation
WHERE vehicle.id=reservation.vehicleId
    AND reservation.status!="canceled"
    AND reservation.createdAt BETWEEN "{date_from}" AND "{date_to}"
GROUP BY
    vehicle_id,
    year,
    model
ORDER BY total_reservations DESC;
