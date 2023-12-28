from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['Pokemon Name', 'Type']
table.add_row(['Pickachu', 'Electric'])
table.add_row(['Squirtle', 'Water'])
table.add_row(['Charmander', 'Fire'])
table.align = 'l'

print(table)