import pandas as pd
from locale import atof, setlocale, LC_NUMERIC
setlocale(LC_NUMERIC, 'nl_NL')


class Spendit:
    def __init__(self, month):
        self.monthly_expenses_names = ['ZIGGO SERVICES BV', 'VITENS NV', 'CZ Groep Zorgverzekeraar', 'KION Kinderopvang BV',
                                       'Vattenfall Klantenservice N.V.', 'Radicalsports', 'SWAPFIETS BY BUCKAROO', 'T. Leijser']
        self.month = month
        self.monthly_expenses = 0

    def calculate_m_expenses(self, file):
        parsed_data = pd.read_csv(file, ';')
        target_indexes = []

        for name in self.monthly_expenses_names:
            target = parsed_data[parsed_data['Tegenrekeninghouder'] == name]
            target_index = target.index.values
            target_indexes.extend(target_index)

        for t_index in target_indexes:
            target_money = parsed_data['Bedrag'][t_index]
            target_money = atof(target_money)
            self.monthly_expenses = self.monthly_expenses + target_money

        print('Recurring monthly expensens:',
              self.month, self.monthly_expenses)


juni = Spendit('juni')
juni.calculate_m_expenses('data/Knab-juni.csv')
