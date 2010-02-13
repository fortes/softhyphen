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

    >>> hyphenate_html('O paralelepipedo atrevessou a rua', 'pt-br')
    u'O &shy;pa&shy;ra&shy;le&shy;le&shy;pi&shy;pe&shy;do a&shy;tre&shy;ves&shy;sou a &shy;rua'

    Content inside <code>, <tt>, and <pre> blocks is not hyphenated
    >>> hyphenate_html('Document: <code>document + page_status</code>')
    u'Doc&shy;u&shy;ment: <code>document + page_status</code>'
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
    Hyphenate the text within an element, returning the hyphenated version
    """
    if isinstance(node, NavigableString):
        return NavigableString(hyphenator.inserted(node, SOFT_HYPHEN))
    elif node.contents and node.name not in ELEMENT_BLACKLIST:
        for i, c in enumerate(node.contents):
            node.contents[i] = hyphenate_element(c, hyphenator)

    return node

DICTIONARIES = {
    'cs-cz': 'hyph_cs_CZ',
    'da-dk': 'hyph_da_DK',
    'de-ch': 'hyph_de_CH',
    'de-de': 'hyph_de_DE',
    'el-gr': 'hyph_el_GR',
    'en-ca': 'hyph_en_CA',
    'en-gb': 'hyph_en_GB',
    'en-us': 'hyph_en_US',
    'es-es': 'hyph_es_ES',
    'fi-fi': 'hyph_fi_FI',
    'ga-ie': 'hyph_ga_IE',
    'hu-hu': 'hyph_hu_HU',
    'ia': 'hyph_ia',
    'id-id': 'hyph_id_ID',
    'is-is': 'hyph_is_IS',
    'it-it': 'hyph_it_IT',
    'lt-lt': 'hyph_lt_LT',
    'nl-nl': 'hyph_nl_NL',
    'pl-pl': 'hyph_pl_PL',
    'pt-br': 'hyph_pt_BR',
    'pt-pt': 'hyph_pt_PT',
    'ro-ro': 'hyph_ro_RO',
    'ru-ru': 'hyph_ru_RU',
    'sh': 'hyph_sh',
    'sk-sk': 'hyph_sk_SK',
    'sl-si': 'hyph_sl_SI',
    'sr': 'hyph_sr',
    'sv-se': 'hyph_sv_SE',
    'uk-ua': 'hyph_uk_UA'
}
def get_hyphenator_for_language(language):
    """
    Create a Hyphenator for the given language. Uses English if the
    language is not found.

    >>> get_hyphenator_for_language('ru-ru') #doctest: +ELLIPSIS
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
