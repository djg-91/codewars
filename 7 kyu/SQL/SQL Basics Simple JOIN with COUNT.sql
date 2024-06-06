/*
https://www.codewars.com/kata/580918e24a85b05ad000010c

    For this challenge you need to create a simple SELECT statement that will return 
    all columns from the people table, and join to the toys table so that 
    you can return the COUNT of the toys

    people table schema

        id
        name

    toys table schema

        id
        name
        people_id

    You should return all people fields as well as the toy count as "toy_count".
*/


SELECT 
  a.id, 
  a.name, 
  COUNT(*) AS toy_count
FROM 
  people a
    INNER JOIN toys b 
      ON a.id = b.people_id
GROUP BY a.id, a.name;