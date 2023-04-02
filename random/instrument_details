# Darius Corbin
# PA 13

class Instrument:
    def __init__(self, name, manufacturer, year_built, cost):
        self.name = name
        self.manufacturer = manufacturer
        self.year_built = year_built
        self.cost = cost

    def print_info(self):
        print('   Name:', self.name)
        print('   Manufacturer:', self.manufacturer)
        print('   Year built:', self.year_built)
        print('   Cost:', self.cost)
# TODO: Define the StringInstrument class that inherits from the Instrument class
    # TODO: Define constructor with attributes:
    #       name, manufacturer, year_built, cost, num_strings, num_frets
class StringInstrument(Instrument):
    def __init__(self, name, manufacturer, year_built, cost, num_strings, num_frets): #(Zybooks 12.1, 12.5)
        Instrument.__init__(self, name, manufacturer, year_built, cost)  # Call base class constructor
        self.name = name
        self.manufacturer = manufacturer
        self.year_built = year_built
        self.cost = cost
        self.num_strings = num_strings
        self.num_frets = num_frets

    # TODO: Define a print_info() method that overrides the print_info()
    #       in the Instrument class
    def print_info(self):
       print('   Name:', self.name)
       print('   Manufacturer:', self.manufacturer)
       print('   Year built:', self.year_built)
       print('   Cost:', self.cost)
       print('   Num_Strings:', self.num_strings)
       print('   Num_Frets:', self.num_frets)

if __name__ == "__main__":
    print('\nEnter the instrument Information:')
    instrument_name = input('Enter the name: ')
    manufacturer_name = input('Enter the manufacturer: ')
    year_built = int(input('Enter the year built: '))
    cost = int(input('Enter the cost: '))
    print('\nEnter the string instrument Information:')
    string_instrument_name = input('Enter the name: ')
    string_manufacturer = input('Enter the manufacturer: ')
    string_year_built = int(input('Enter the year built: '))
    string_cost = int(input('Enter the cost: '))
    num_strings = int(input('Enter the number of strings: '))
    num_frets = int(input('Enter the number of frets: '))
    # TODO: Create an Instrument instance, based on the user input
    x = Instrument(instrument_name, manufacturer_name, year_built, cost)
    print('\nInstrument Information:')
    # TODO:  Call the print_info method
    x.print_info()
    # TODO: Create a StringInstrument instance, based on the user input
    #Watch for change in variable names
    y = StringInstrument(string_instrument_name, string_manufacturer, string_year_built, string_cost, num_strings, num_frets)
    print('\nString Instrument Information:')
    # TODO: Call the print_info method
    y.print_info()
