SELECT * FROM flights;

-- SELECTING COL --

SELECT origin, destination FROM flights;

-- SPECIFYING DIFF. COL --

SELECT * FROM flights WHERE id = 3;

SELECT * FROM flights WHERE origin = 'New York';

SELECT * FROM flights WHERE duration > 500;

SELECT * FROM flights WHERE duration > 500 AND destination = 'Istambul'

-- AVG AND OTHER FUNC --

SELECT AVG(duration) FROM flights

SLECT COUNT(*) FROM flights