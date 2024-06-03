/*
https://www.codewars.com/kata/594901ba44645fd7bd00005f

    Given a demographics table in the following format:

    demographics table schema
        id
        name
        birthday
        race

    return a single column named calculation where the value is the bit length of name, 
    added to the number of characters in race.
*/


SELECT BIT_LENGTH(name) + LENGTH(race) AS calculation
FROM demographics;