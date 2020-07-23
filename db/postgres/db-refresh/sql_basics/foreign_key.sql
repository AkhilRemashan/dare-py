CREATE TABLE passengers(
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
);

INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob', 2);

SELECT * FROM passengers WHERE name = 'Alice';

SELECT * FROM flights WHERE id = 1;

-- 
-- 

SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id;