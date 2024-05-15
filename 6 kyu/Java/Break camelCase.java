/*
https://www.codewars.com/kata/5208f99aee097e6552000148

    Complete the solution so that the function will break up camel casing, 
    using a space between words.

    Example
    "camelCasing"  =>  "camel Casing"
    "identifier"   =>  "identifier"
    ""             =>  ""
*/


class Solution {
  public static String camelCase(String input) {
    String result = "";
    char[] chars = input.toCharArray();
    for (char c : chars) {
      result += (Character.isUpperCase(c)) ? " " + c : c;
    }
    return result;
  }
}