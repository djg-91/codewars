/*
https://www.codewars.com/kata/51b66044bce5799a7f000003

    Write two functions that convert a roman numeral to and from an integer value. 
    Multiple roman numeral values will be tested for each function.

    Modern Roman numerals are written by expressing each digit separately starting with 
    the left most digit and skipping any digit with a value of zero. In Roman numerals:

    1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
    2008 is written as 2000=MM, 8=VIII; or MMVIII
    1666 uses each Roman symbol in descending order: MDCLXVI.
    Input range : 1 <= n < 4000

    In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

    Examples
        to roman:
            2000 -> "MM"
            1666 -> "MDCLXVI"
            86 -> "LXXXVI"
            1 -> "I"

        from roman:
            "MM"      -> 2000
            "MDCLXVI" -> 1666
            "LXXXVI"  ->   86
            "I"       ->    1
*/


class RomanNumerals {
	static romans = {
		'I': 1,   'IV': 4,   'V': 5,   'IX': 9, 
		'X': 10,  'XL': 40,  'L': 50,  'XC': 90, 
		'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 
		'M': 1000
	};
  
	static romansInverted = {
		1:  {1: 'C', 4: 'CD', 5: 'D', 9: 'CM'},
		2:  {1: 'X', 4: 'XL', 5: 'L', 9: 'XC'},
		3:  {1: 'I', 4: 'IV', 5: 'V', 9: 'IX'}
	}

	static toRoman(num) {
		let result = '';
		num = num.toString().padStart(4, '0');
		
		for (let i = 0; i < num.length; i++) {
			
			let digit = parseInt(num[i]);
      
			if (digit == 0) { continue };
      			
			if (i == 0) {
				result += 'M'.repeat(digit);
			} else if (digit <= 3) {
				result += this.romansInverted[i][1].repeat(digit);
			} else if (digit == 4 || digit == 5) {
				result += this.romansInverted[i][digit];
			} else if (5 < digit && digit < 9) {
				result += this.romansInverted[i][5];
				result += this.romansInverted[i][1].repeat(digit - 5);
			} else if (digit == 9) {
				result += this.romansInverted[i][9];
			}
		}
		return result;
	}

	static fromRoman(str) {
		let result = 0;
		
		while (str.length > 0) {

			if (str.length == 1) {
				result += this.romans[str];
				return result;
			}
			
			if (str.slice(0, 2) in this.romans) {
				result += this.romans[str.slice(0, 2)];
				str = str.slice(2);
			} else {
				result += this.romans[str.slice(0, 1)];
				str = str.slice(1);
			}	
		}
		return result;  
	}
}