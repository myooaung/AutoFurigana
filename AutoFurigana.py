# -*- coding: utf-8 -*-
"""
Adds furigana to selected text.

Sources:
 - http://tinysegmenter.tuxfamily.org/
 -  
 - 
 
Created on Sat May 17 13:05:51 2014

@author: Christian Wichmann
"""


def is_hiragana(char):
    """Checks if character is a hiragana symbol."""
    if '\u3040' <= char <= '\u309F':
        return True
    else:
        return False


def is_katakana(char):
    """Checks if character is a katagana symbol."""
    if '\u30A0' <= char <= '\u30FF':
        return True
    else:
        return False


def is_cjk_punctuation(char):
    """Checks if character is a punctuation symbol."""
    if '\u3000' <= char <= '\u303F':
        return True
    else:
        return False


def should_reading_be_added(word):
    all_hiragana = True
    all_katakana = True
    for char in word:
        all_hiragana &= is_hiragana(char)
        all_katakana &= is_katakana(char)
        if is_cjk_punctuation(char):
            return False
    return not (all_hiragana or all_katakana)


def add_furigana_to_selection():
    """Adds furigana to a selected Japanese text in the current document."""
    # get the doc from the scripting context
    model = XSCRIPTCONTEXT.getDocument()
    # get currently selected text
    cursor = model.getCurrentController().getViewCursor()
    current_selection = str(cursor.getString())
    # split selection into words
    words = split_text_into_words(current_selection)
    # get a new cursor
    start = cursor.getStart()
    #end = cursor.getEnd()
    text_document = model.getText()
    new_cursor = text_document.createTextCursorByRange(start)
    # loop through words and add readings when necessary
    for word in words:
        new_cursor.goRight(len(word), True)
        if should_reading_be_added(word):
            output = get_reading_kakasi(word)
            new_cursor.RubyText = output
        new_cursor.collapseToEnd()
    #text = model.Text
    #text.insertString(cursor, str(start), 0)


def add_furigana_to_word():
    """Adds furigana to a selected Japanese word in the current document."""
    # get the doc from the scripting context
    #context = uno.getComponentContext()
    #model = context.getDocument()
    model = XSCRIPTCONTEXT.getDocument()
    # get currently selected text
    cursor = model.getCurrentController().getViewCursor()
    current_selection = str(cursor.getString())
    # get reading for selection
    output = get_reading_kakasi(current_selection)
    # print text
    #text = model.Text
    #cursor = text.createTextCursor()
    #cursor.gotoEnd(False)
    # com.sun.star.style.CharacterProperties -> RubyText
    cursor.RubyText = output
    #text.insertString(cursor, '(' + output + ')', 0)


def split_text_into_words(text):
    import tinysegmenter
    segmenter = tinysegmenter.TinySegmenter()
    return segmenter.tokenize(text)


def get_reading_kakasi(word):
    """Gets reading for a given Japanese word by using kakasi. The reading in
       hiragana is returned by this function."""
    import pykakasi.kakasi as kakasi
    kakasi = kakasi()
    kakasi.setMode("J", "H")
    kakasi.setMode("C", True)  # default: Separator
    kakasi.setMode("c", False)  # default: no Capitalize
    conv = kakasi.getConverter()
    result = conv.do(word)
    return result


# set tuple of functions that should be exported
g_exportedScripts = (add_furigana_to_word, add_furigana_to_selection)
