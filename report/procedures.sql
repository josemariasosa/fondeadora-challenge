-- SELECT 
--     vehicle.id AS vehicle_id,
--     vehicle.year AS year,
--     vehicle.model AS model,
--     COUNT(reservation.id) AS total_reservations
-- FROM vehicle, reservation
-- WHERE vehicle.id=reservation.vehicleId AND reservation.status="confirmed"
-- GROUP BY
--     vehicle_id,
--     year,
--     model
-- ORDER BY total_reservations DESC;

-- SELECT 
--     vehicleId AS vehicle_id,
--     COUNT(vehicleId) AS total_rents,
--     AVG(strftime('%s',arrivedAt) - strftime('%s',departureAt)) AS avg_rent_duration
-- FROM rent
-- WHERE isCompleted=1
-- GROUP BY
--     vehicleId;

SELECT
    vehicleId,
    arrivedLocationId,
    max(departureAt)
from rent
WHERE isCompleted=1
group by vehicleId;