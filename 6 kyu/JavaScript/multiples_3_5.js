/*
https://www.codewars.com/kata/514b92a657cdc65150000006

    --- Multiples of 3 or 5 ---

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

    Additionally, if the number is negative, return 0.

    Note: If the number is a multiple of both 3 and 5, only count it once.
*/


function solution(number){
    let result = [];
    
    for (i = 2; i < number; i++) {
      if (i % 3 == 0 || i % 5 == 0) result.push(i);
    }
  
    return result.length > 0 ? result.reduce((acc, val) => acc + val, 0) : 0;
  }