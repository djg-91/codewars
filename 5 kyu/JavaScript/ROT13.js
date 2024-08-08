/*
https://www.codewars.com/kata/52223df9e8f98c7aa7000062

    How can you tell an extrovert from an introvert at NSA?
    Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

    I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
    According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

    For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

    Test examples:

        "EBG13 rknzcyr." -> "ROT13 example."

        "This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"<
*/


function rot13(str) {
    const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
    let msg = '';
    for (const char of str) {
        if (char.match(/[a-z]/i)) {
            let pos = char === char.toUpperCase() ? alphabet.indexOf(char.toLowerCase()) : alphabet.indexOf(char);
            pos = (pos + 13) % 26;
            msg += char === char.toUpperCase() ? alphabet[pos].toUpperCase() : alphabet[pos];
        } else {
            msg += char;
        }
    }
    return msg;
  }