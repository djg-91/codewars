: << 'END'
https://www.codewars.com/kata/515decfd9dcfc23bb6000006

    Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
    IPs should be considered valid if they consist of four octets, 
    with values between 0 and 255, inclusive.

    Valid inputs examples:
    Examples of valid inputs:
    1.2.3.4
    123.45.67.89
    Invalid input examples:
    1.2.3
    1.2.3.4.5
    123.456.78.90
    123.045.067.089
    Notes:
    Leading zeros (e.g. 01.02.03.04) are considered invalid
    Inputs are guaranteed to be a single string
END


adr="$1"

IFS=$'.'

let count=0
for oct in ${adr}; do
    if [[ $oct == 0 ]]; then
        let count+=1
        continue
    elif [[ $oct =~ ^0[0-9]{1,2}$ ]]; then
        echo False
        exit 1
    elif [[ "$oct" =~ ^[0-9]{1,3}$ ]] && [[ ! $((10#$oct)) -gt 255 ]]; then
        let count+=1
        continue
    else
        echo False
        exit 1
    fi
done

if [[ $count == 4 ]]; then
    echo True
else
    echo False
fi

exit