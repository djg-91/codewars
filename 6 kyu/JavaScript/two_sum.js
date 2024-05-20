/*
https://www.codewars.com/kata/52c31f8e6605bcc646000082

    --- Two Sum ---

    Write a function that takes an array of numbers (integers for the tests) and a target number. 
    It should find two different items in the array that, when added together, give the target value. 
    The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

    For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

    The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; 
    target will always be the sum of two different items from that array).

    twoSum([1, 2, 3], 4) // returns [0, 2] or [2, 0]
    twoSum([3, 2, 4], 6) // returns [1, 2] or [2, 1]
*/


function twoSum(numbers, target) {
    for (let i1 = 0; i1 < numbers.length; i1++) {
        for (let i2 = 0; i2 < numbers.length && i1 != i2; i2++) {
            if (numbers[i1] + numbers[i2] == target) return [i1, i2];
        }
    }
}