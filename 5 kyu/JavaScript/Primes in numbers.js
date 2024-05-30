/*
https://www.codewars.com/kata/54d512e62a5e54c96200019e

    Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

    "(p1**n1)(p2**n2)...(pk**nk)"
    with the p(i) in increasing order and n(i) empty if n(i) is 1.

    Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
*/


function primeFactors(n) {
    let result = {};
    let result_str = "";
    let i = 2;
    while (i <= n) {
        if (n % i == 0) {
            result[i] = i in result ? result[i] + 1 : 1;
            n = n / i;
        } else {
          i++;
        }
    }
    for (let k in result) {
        result_str += result[k] > 1 ? `(${k}**${result[k]})` : `(${k})`;
    }
    return result_str;
}