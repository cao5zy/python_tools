from parse_es_import import parse_import, parse_from

def test_parse_import():
    line = "import { StyleSheet, View, Animated, ScrollView, Easing } from 'react-native';"
    items =  parse_import(line)
    assert "StyleSheet" in items

def test_parse_import_with_invalid_line():
    line = "const x=3;"
    items =  parse_import(line)
    assert len(items) == 0
    
def test_parse_from():
    line = "import { StyleSheet, View, Animated, ScrollView, Easing } from 'react-native';"
    item = parse_from(line)
    assert item == 'react-native'

def test_parse_from_with_invalid_line():
    line = "const x=3;"
    item =  parse_from(line)
    assert item == ''
    
