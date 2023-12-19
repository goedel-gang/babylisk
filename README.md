Inspired by
[this](https://github.com/savbell/advent-of-code-one-liners/tree/master)
absolute legend.

Some one-line solutions for Advent of Code problems. I am not allowing myself to
use the walrus operator because that's unnatural `:D`

The files `q14b.py` and `q16b.py` are my actual solutions for Days 14 and 16.
These files read their puzzle input from `q??_input.txt`.
I have then adapted these in a number of stages:

The files `q14_oneline.py` `q16_oneline.py` are the first step on the road to
madness. In these I've replaced every `def` by a `lambda` already. They're not
technically one-liners yet but they're very close and they are a bit easier to
read.

The files `q14_oneline_real.py` and `q16_oneline_real.py` are (syntactically)
honest one-liners. Basically I've taken the previous files and rearranged them a
bit to make it a proper one-liner. There is still some whitespace, including
some newlines, but that is purely decorative and can be removed without issue.

The files `q14_oneline_mangled.py` and `q16_oneline_mangled.py` are just there
in case you want something really illegible to look at. I have replaced all the
variables with one-letter names and given them a cursory golf. Doubtless there
are more bytes to be shaved either by some clever tricks or a big rewrite. These
files read their input from stdin in the interest of saving a few bytes of
source code.

All my code works and gives the correct output when I run it with

`PyPy 7.3.13` or `CPython Python 3.11.6`. The latter does give some syntax
warnings about `q14_oneline_mangled.py`, but it still executes.

`PyPy` takes about `0.4` seconds to run `q14_oneline_mangled.py` and
`1.8` seconds to run `q16_oneline_mangled.py`. That's not so bad, given the
circumstances!
