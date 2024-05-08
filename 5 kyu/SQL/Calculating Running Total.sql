/*
https://www.codewars.com/kata/589cf45835f99b2909000115

    Given a posts table that contains a created_at timestamp column 
    write a query that returns date (without time component), 
    a number of posts for a given date and a running (cumulative) 
    total number of posts up until a given date. The resulting set should 
    be ordered chronologically by date.

    Desired Output

    The resulting set should look similar to the following:

        date       | count | total
        -----------+-------+-------
        2017-01-26 |    20 |    20
        2017-01-27 |    17 |    37
        2017-01-28 |     7 |    44
        2017-01-29 |     8 |    52
        ...
    
    date - (DATE) date
    count - (INT) number of posts for a date
    total - (INT) a running (cumulative) number of posts up until a date
*/


WITH dates AS (
  SELECT 
    CAST(created_at AS DATE) AS date,
    COUNT(*) AS count
  FROM posts
  GROUP BY date
)
SELECT
  t1.date, t1.count, 
  CAST(
    (SELECT SUM(t2.count) 
    FROM dates t2
    WHERE t2.date <= t1.date) 
    AS INTEGER
  ) AS total
FROM dates t1
ORDER BY date;