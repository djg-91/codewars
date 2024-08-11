'''
https://www.codewars.com/kata/537e18b6147aa838f600001b

    Your task in this Kata is to emulate text justification in monospace font. 
    You will be given a single-lined text and the expected justification width. 
    The longest word will never be greater than this width.

    Here are the rules:

        Use spaces to fill in the gaps between words.
        Each line should contain as many words as possible.
        Use '\n' to separate lines.
        Last line should not terminate in '\n'
        '\n' is not included in the length of a line.
        Gaps between words can't differ by more than one space.
        Lines should end with a word not a space.
        Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
        Last line should not be justified, use only one space between words.
        Lines with one word do not need gaps ('somelongword\n').
        
    Example with width=30:

        Lorem  ipsum  dolor  sit amet,
        consectetur  adipiscing  elit.
        Vestibulum    sagittis   dolor
        mauris,  at  elementum  ligula
        tempor  eget.  In quis rhoncus
        nunc,  at  aliquet orci. Fusce
        at   dolor   sit   amet  felis
        suscipit   tristique.   Nam  a
        imperdiet   tellus.  Nulla  eu
        vestibulum    urna.    Vivamus
        tincidunt  suscipit  enim, nec
        ultrices   nisi  volutpat  ac.
        Maecenas   sit   amet  lacinia
        arcu,  non dictum justo. Donec
        sed  quam  vel  risus faucibus
        euismod.  Suspendisse  rhoncus
        rhoncus  felis  at  fermentum.
        Donec lorem magna, ultricies a
        nunc    sit    amet,   blandit
        fringilla  nunc. In vestibulum
        velit    ac    felis   rhoncus
        pellentesque. Mauris at tellus
        enim.  Aliquam eleifend tempus
        dapibus. Pellentesque commodo,
        nisi    sit   amet   hendrerit
        fringilla,   ante  odio  porta
        lacus,   ut   elementum  justo
        nulla et dolor.

    Also you can always take a look at how justification works in your text editor 
    or directly in HTML (css: text-align: justify).
'''


import numpy


def justify(text, width):
    text = text.split()
    lines = ''

    while len(text) > 0:
        words = []

        for word in text:
            words += [word]
            if not len(' '.join(words)) <= width:
                words.pop()
                break

        if len(words) == 1:
            lines += words[0] + '\n'
        elif len(words) == len(text):
            lines += ' '.join(words)
        else:
            spaces = width - len(''.join(words))
            arrays = []
            for x in numpy.array_split(numpy.array([' '] * spaces), len(words) - 1):
                arrays += [''.join(list(x))]

            for i in range(len(words)):
                lines += words[i]
                if i < len(arrays):
                    lines += arrays[i]
            lines += '\n'

        del text[:len(words)]
    return lines.strip()