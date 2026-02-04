from pprint import pprint


def reading_file():
    sneakers = []

    with open('Nike_shoes_2023-04-16.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines[1:]:  # fejléc kihagyása
            data = line.strip().split(',')

            shoe = {
                'title': data[1],
                'color': data[4],
                'full_price': float(data[5]),
                'current_price': float(data[6]),
                'publish_date': data[9]
            }

            sneakers.append(shoe)

    return sneakers


def print_shoes(sneakers):
    choice = input(
        'Válassz, hogy melyik szempont alapján rendezzem a cipőket!\n'
        '1 - title\n'
        '2 - color\n'
        '3 - full price\n'
        '4 - current price\n'
        '5 - publish date\n'
    )

    if choice == '1':
        key_name = 'title'
    elif choice == '2':
        key_name = 'color'
    elif choice == '3':
        key_name = 'full_price'
    elif choice == '4':
        key_name = 'current_price'
    elif choice == '5':
        key_name = 'publish_date'

    pprint(sorted(sneakers, key=lambda shoe: shoe[key_name]))


def main():
    sneakers = reading_file()
    print_shoes(sneakers)


main()
