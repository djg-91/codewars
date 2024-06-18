/*
https://www.codewars.com/kata/5817b124e7f4576fd00020a2

    Given film_actor and film tables from the DVD Rental sample 
    database find all movies both Sidney Crowe (actor_id = 105) 
    and Salma Nolte (actor_id = 122) cast in together and order the result set alphabetically.

    film schema
    
        Column     | Type                        | Modifiers
        ------------+-----------------------------+----------
        title       | character varying(255)      | not null
        film_id     | smallint                    | not null

    film_actor schema

        Column     | Type                        | Modifiers
        ------------+-----------------------------+----------
        actor_id    | smallint                    | not null
        film_id     | smallint                    | not null
        last_update | timestamp without time zone | not null 

    actor schema

        Column     | Type                        | Modifiers
        ------------+-----------------------------+----------
        actor_id    | integer                     | not null 
        first_name  | character varying(45)       | not null
        last_name   | character varying(45)       | not null
        last_update | timestamp without time zone | not null 

    The desired output:

        title
        -------------
        Film Title 1
        Film Title 2
        ...

    title - Film title
*/


WITH result AS (
SELECT f.title, COUNT(*) AS films
FROM 
  film f
    JOIN film_actor fa
      ON fa.film_id = f.film_id
      AND fa.actor_id IN (105, 122)
GROUP BY f.title
)
SELECT title FROM result
WHERE films > 1
ORDER BY 1;