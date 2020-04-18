from parse_es_import import parse_import

def test_parse_import():
    line = "import { StyleSheet, View, Animated, ScrollView, Easing } from 'react-native';"
    items =  parse_import(line)
    assert "StyleSheet" in items
