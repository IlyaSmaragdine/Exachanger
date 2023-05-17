import pygsheets

#Auth
gc = pygsheets.authorize(service_file= 'exchanger-386923-131a3c7a7205.json')
# Open spredhseet by link
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1aaf1_vgLlBcENhU8edOpaQ7LDjU8tchjNV_kXvVJ66A/edit?usp=sharing')

# Open worksheet
wk1 = sh[0]

def main():
    currency_input = input('enter currency, available: USD, UAH, EUR, PLN. Enter exit to close a program\nenter your currency: ')

    if currency_input == 'USD':
        currency_output = input('enter currency to translate, available: UAH, EUR, PLN: ')

        if currency_output == "UAH":
            get_value = wk1.cell((1,3)).value
            amount = float(input('enter your amount, float type (for example: 12.0): '))
            print(amount, ' USD in UAH: ', amount*float(get_value))

        if currency_output == "EUR":
            get_value = wk1.cell((2, 3)).value
            amount = float(input('enter your amount, float type (for example: 12.0): '))
            print(amount, ' USD in EUR: ', amount * float(get_value))

        if currency_output == "PLN":
            get_value = wk1.cell((3, 3)).value
            amount = float(input('enter your amount, float type (for example: 12.0): '))
            print(amount, ' USD in PLN: ', amount * float(get_value))

    if currency_input == 'UAH':
        currency_output = input('enter currency to translate, available: USD, EUR, PLN: ')

        if currency_output == "USD":
            get_value = wk1.cell((4,3)).value
            amount = float(input('enter your amount, float type (for example: 12.0): '))
            print(amount, ' UAH in USD: ', amount*float(get_value))

        if currency_output == "EUR":
            get_value = wk1.cell((5, 3)).value
            amount = float(input('enter your amount, float type (for example: 12.0): '))
            print(amount, ' UAH in EUR: ', amount * float(get_value))

        if currency_output == "PLN":
            get_value = wk1.cell((6, 3)).value
            amount = float(input('enter your amount, float type (for example: 12.0): '))
            print(amount, ' UAH in PLN: ', amount * float(get_value))

    if currency_input == 'EUR':
        currency_output = input('enter currency to translate, available: USD, UAH, PLN: ')

        if currency_output == "USD":
            get_value = wk1.cell((7,3)).value
            amount = float(input('enter your amount, float type (for example: 12.0): '))
            print(amount, ' EUR in USD: ', amount*float(get_value))

        if currency_output == "UAH":
            get_value = wk1.cell((8, 3)).value
            amount = float(input('enter your amount, float type (for example: 12.0): '))
            print(amount, ' EUR in UAH: ', amount * float(get_value))

        if currency_output == "PLN":
            get_value = wk1.cell((9, 3)).value
            amount = float(input('enter your amount, float type (for example: 12.0): '))
            print(amount, ' EUR in PLN: ', amount * float(get_value))

    if currency_input == 'PLN':
        currency_output = input('enter currency to translate, available: USD, UAH, EUR: ')

        if currency_output == "USD":
            get_value = wk1.cell((10,3)).value
            amount = float(input('enter your amount, float type (for example: 12.0): '))
            print(amount, ' PLN in USD: ', amount*float(get_value))

        if currency_output == "UAH":
            get_value = wk1.cell((11, 3)).value
            amount = float(input('enter your amount, float type (for example: 12.0): '))
            print(amount, ' PLN in UAH: ', amount * float(get_value))

        if currency_output == "EUR":
            get_value = wk1.cell((12, 3)).value
            amount = float(input('enter your amount, float type (for example: 12.0): '))
            print(amount, ' PLN in EUR: ', amount * float(get_value))

    if currency_input == 'exit':
        print('thnx for using program')
        exit()

    main()

main()

print("success")



