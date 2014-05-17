AutoFurigana
============

DESCRIPTION
-----------
AutoFurigana is a OpenOffice/LibreOffice macro to add furigana to Japanese
texts written in Python.


INSTALLATION
------------
1) Install python packages tinysegmenter and pykakasi.

    sudo pip3 install tinysegmenter
    sudo pip3 install pykakasi

2) Copy file AutoFurigana.py to folder 

    ~/.config/libreoffice/4/user/Scripts/python/AutoFurigana.py

3) Mark text segment to which furigana should be added.

4) Execute macro "add_furigana_to_selection" in OpenOffice/LibreOffice.


REQUIREMENTS
------------
AutoFurigana was only ever tested under Ubuntu Linux with Python 3. It
requirs the python packages tinysegmenter and pykakasi to split Japanese
text and generate readings for the words.


KNOWN PROBLEMS AND BUGS
-----------------------



LICENSE
-------
AutoFurigana is released under the GNU General Public License v2 or newer.


