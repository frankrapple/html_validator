#!/bin/python3
import re


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''


    if len(html) == 0:
        return True
    tags = _extract_tags(html)
    if not tags:
        return False
    
    tag_stack = []
    index = 0 
    while index<len(tags):
        tag = tags[index]
        tag_name = tag[1:-1]
        if "/" not in tag:
                tag_stack.append(tag)
        else:
            if len(tag_stack) == 0:
                return False
            lasttag = tag_stack.pop()
            if not lasttag == tag_name[1:]: 
                return False
        index += 1 







def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    tags=re.findall(r'<[^>]+>', html) 
    return tags


