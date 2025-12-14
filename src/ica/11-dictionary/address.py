betsy_info = {'Name': 'Betsy Foobar',
              'Phone': 'x8012',
              'Street': '1600 Grand Avenue',
              'City': 'Saint Paul',
              'State': 'MN',
              'Email': 'bfoobar@macalester.edu'}

tom_info = {'Name': 'Tom Riddle',
            'Phone': 'x8512',
            'Street': '1600 Grand Avenue',
            'City': 'Saint Paul',
            'State': 'MN',
            'Email': 'triddle@macalester.edu'}

address_book = [ betsy_info, tom_info,
                {'Name': 'Susan Fox',
                 'Phone': 'x6553',
                 'Street': '1600 Grand Avenue',
                 'City': 'Saint Paul',
                 'State': 'MN',
                 'Email': 'fox@macalester.edu'}]

print(address_book)

address_book.append ({'Name': 'Abigail Heuga',
                 'Phone': 'x2832',
                 'Street': '136 Clipper Street',
                 'City': 'San Francisco',
                 'State': 'CA',
                 'Email': 'aheuga@macalester.edu'})

address_book.append ({'Name': 'John Cochrane',
                    'Phone': 'x6501',
                    'Street': '507 Silver Avenue',
                    'City': 'San Francisco',
                    'State': 'CA',
                    'Email': 'jcochrane@gmail.com'})

def filter_by_city(city, address_book):
    result = []
    for address in address_book:
        if address['City'] == city:
            result.append(address)
    return result