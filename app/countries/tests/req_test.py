import unittest

from app.countries.req import capital, Capital, get_capitals


class TestCapital(unittest.TestCase):

    def test_capital(self):
        capitals = get_capitals()
        for c in capitals:
            if c.name == 'Moscow':
                moscow = c
                break
        else:
            raise AssertionError
        t = capital('Moscow')
        self.assertEqual(t.name, moscow.name)
        self.assertEqual(t.country, moscow.country)
        self.assertEqual(t.info, moscow.info)
