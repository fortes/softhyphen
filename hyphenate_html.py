"""
Hyphenates an HTML fragement using soft hyphens

Author: Filipe Fortes
"""

from lib.hyphenator import Hyphenator
from lib.BeautifulSoup import BeautifulSoup, NavigableString

def hyphenate_html(html, language='en-us', hyphenator=None):
    r"""
    Hyphenate a fragement of HTML

    >>> hyphenate_html('<p>It is <em>beautiful</em> outside today!</p>')
    u'<p>It is <em>beau&shy;ti&shy;ful</em> out&shy;side today!</p>'
    """
    # Load hyphenator if one is not provided
    if not hyphenator:
        hyphenator = get_hyphenator_for_language(language)

    # Create HTML tree
    soup = BeautifulSoup(html)

    # Recursively hyphenate each element
    hyphenate_element(soup, hyphenator)

    return unicode(soup)

SOFT_HYPHEN = r'&shy;'
ELEMENT_BLACKLIST = [
    'code', 'tt', 'pre'
]
def hyphenate_element(node, hyphenator):
    """
    Hyphenate the text within an element
    """
    #if node != None or (node.has_attr('name') and node.name in ELEMENT_BLACKLIST):
        ## Don't modify text within blacklisted elements
        #print 'backing out'
        #return

    if isinstance(node, NavigableString):
        return NavigableString(hyphenator.inserted(node, SOFT_HYPHEN))
    elif node.contents:
        for i, c in enumerate(node.contents):
            node.contents[i] = hyphenate_element(c, hyphenator)
        return node

DICTIONARIES = {
    'en-us': 'hyph_en_US'
}
def get_hyphenator_for_language(language):
    """
    Create a Hyphenator for the given language. Uses English if the
    language is not found.

    >>> get_hyphenator_for_language('en-US') #doctest: +ELLIPSIS
    <lib.hyphenator.Hyphenator object at ...
    """
    language = language.lower()

    # Fallback to English
    if not language in DICTIONARIES:
        language = 'en-us'

    return Hyphenator('dicts/%s.dic' % DICTIONARIES[language])

# Test when standalone
def _test():
    """Run doctests"""
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
