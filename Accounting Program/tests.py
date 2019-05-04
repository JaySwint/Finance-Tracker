"""
functions to test
-------------------

list_to_dictionary

dictionary_to_list

get_total_value_from_dict

-------------------

these are the only testable functions in the program "accounting_tools"; all other functions require user input/txtfiles

"""

import unittest
import accounting_tools


class Tester(unittest.TestCase):

    def test_list_to_dictionary(self):
        self.assertEqual(accounting_tools.list_to_dictionary(['cash,100'], ['loans,200'], ['equity,300']), ({'cash': 100}, {'loans': 200}, {'equity': 300}))
        self.assertEqual(accounting_tools.list_to_dictionary([], [], []), ({}, {}, {}))
        self.assertEqual(accounting_tools.list_to_dictionary(['CaSh,100'], ['LoAnS,200'], ['EqUiTy,300']), ({'CaSh': 100}, {'LoAnS': 200}, {'EqUiTy': 300}))
        self.assertEqual(accounting_tools.list_to_dictionary(['cash,0'], ['loans,0'], ['equity,0']), ({'cash': 0}, {'loans': 0}, {'equity': 0}))
        self.assertEqual(accounting_tools.list_to_dictionary(['cash,101'], ['loans,201'], ['equity,301']), ({'cash': 101}, {'loans': 201}, {'equity': 301}))
        self.assertEqual(accounting_tools.list_to_dictionary([' ,100'], [' ,200'], [' ,300']), ({' ': 100}, {' ': 200}, {' ': 300}))
        self.assertEqual(accounting_tools.list_to_dictionary(['cash,1000'], ['loans,20777'], ['equity,20193']), ({'cash': 1000}, {'loans': 20777}, {'equity': 20193}))

    def test_dictionary_to_list(self):
        self.assertEqual(accounting_tools.dictionary_to_list({'checks': 0}), (['checks'], [0], 0))
        self.assertEqual(accounting_tools.dictionary_to_list({'checks': 0, 'cash': 100}), (['checks', 'cash'], [0, 100], 100))
        self.assertEqual(accounting_tools.dictionary_to_list({'loans': 500, 'payable': 1023}), (['loans', 'payable'], [500, 1023], 1523))
        self.assertEqual(accounting_tools.dictionary_to_list({'loans': 0, 'payable': 100}), (['loans', 'payable'], [0, 100], 100))
        self.assertEqual(accounting_tools.dictionary_to_list({'': 0}), ([''], [0], 0))
        self.assertEqual(accounting_tools.dictionary_to_list({'A2 Da': 477, '2a A s': 10000}), (['A2 Da', '2a A s'], [477, 10000], 10477))
        self.assertEqual(accounting_tools.dictionary_to_list({'loans': 100, 'payable': 200, 'equity':500, 'test': 5060}),
                         (['loans', 'payable', 'equity', 'test'], [100, 200, 500, 5060], 5860))

    def test_get_total_value_from_dict(self):
        self.assertEqual(accounting_tools.get_total_value_from_dict({'cash': 100}), 100)
        self.assertEqual(accounting_tools.get_total_value_from_dict({'CaSh': 202}), 202)
        self.assertEqual(accounting_tools.get_total_value_from_dict({'check10': 0}), 0)
        self.assertEqual(accounting_tools.get_total_value_from_dict({'': 20309}), 20309)
        self.assertEqual(accounting_tools.get_total_value_from_dict({'': 0, 'cash': 100, 'loans': 500}), 600)
        self.assertEqual(accounting_tools.get_total_value_from_dict({'Ab N2': 12, 'cash': 37, 'mo': 60}), 109)
        self.assertEqual(accounting_tools.get_total_value_from_dict({'money': 7, 'cash': 706050, 'loans': 345}), 706402)


if __name__ == '__main__': unittest.main()
