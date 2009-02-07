buildout.dumppickedversions
===========================

Q: What is a buildout extension ?

A: http://pypi.python.org/pypi/zc.buildout#extensions

The problem
-----------

When using a zc.buildout based deployment system I want to be able to reproduce
the same setup with the same set of egg versions one month later. Without 
pinning all eggs the task is impossible.


Solution
--------

``buildout.dumppickedversions`` is a buildout extension that does just that. It
can print or generate a versions.cfg file with all not pinned eggs.


buildout.dumppickedversions options
-----------------------------------

dump-picked-versions-file
    A file name you want ``buildout.dumppickedversions`` to write to.
    If not given ``buildout.dumppickedversions`` will dump the results to the 
    screen.


