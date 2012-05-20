Overview
========
*infi.dtypes.hctl* provides a datatype for representing HCT and HCTL in such a way that is easy to extract each part and compare between objects.

Usage
=====
HCTL:
::
  >>> from infi.dtypes.hctl import HCTL
  >>> hctl = HCTL(1,0,0,1)
  >>> hctl.get_host()
  1
  >>> hctl.get_channel()
  0
  >>> hctl.get_target()
  0
  >>> hctl.get_lun()
  1

Checking out the code
=====================

This project uses buildout, and git to generate setup.py and __version__.py.
In order to generate these, run:
::
  python -S bootstrap.py -d -t
  bin/buildout -c buildout-version.cfg

If you don't have nose in your environment, you can have an isolated environment in this project by executing:
::
  bin/buildout install scripts
