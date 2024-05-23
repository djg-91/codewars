/*
https://www.codewars.com/kata/5541f58a944b85ce6d00006a

    Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

    F(n) * F(n+1) = prod

    Your function productFib takes an integer (prod) and returns an array:

    [F(n), F(n+1), true]

    If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return

    [F(n), F(n+1), false]

    F(n) being the smallest one such as F(n) * F(n+1) > prod
*/


function productFib(prod) {
    let fibo = [0, 1];
    let fibi = [];
    let result = false;
    
    while (true) {
      fibi = fibo.slice(-2);
      let fibi_result = fibi[0] * fibi[1];
      console.log(fibi);
      if (fibi_result == prod) {
        result = true;
        break;
      } else if (fibi_result > prod) {
        result = false;
        break;
      }
      fibo.push(fibi.reduce((acc, val) => acc + val, 0));
    }
    return [fibi[0], fibi[1], result];
  }