from parse_es_import import parse_import

def test_parse_import():
    assert parse_import('') == '1'
