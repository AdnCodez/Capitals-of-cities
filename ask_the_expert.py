# This program uses two new Tkinter widgets, simpledialog() creates a popup box that asks the user and,
# messagebox()
# displays the capital city.
from tkinter import Tk, simpledialog, messagebox


def read_from_file():
    with open('capital_data.txt') as file:
        for line in file:
            if line != "\n":
                line = line.rstrip('\n')
                country, city = line.split('/')
                the_world[country] = city


def write_to_file(country_name, city_name):
    with open('capital_data.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)


print('ask the Expert - Capital Cities of the World')
# Create a tkinter window
root = Tk()
# Hide the tkinter window
root.withdraw()

the_world = {}
read_from_file()
while True:
    try:
        query_country = simpledialog.askstring('Country Capital Expert', 'Type the name of a country:')
        try:
            query_country = query_country.capitalize()
        except AttributeError:
            pass
        if query_country in the_world:
            result = the_world[query_country]
            messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!')
        else:
            new_city = simpledialog.askstring('Teach me', 'I don\'t know! ' + 'What is the capital city of ' + query_country + ' ?')
            new_city = new_city.capitalize()
            the_world[query_country] = new_city
            write_to_file(query_country, new_city)

    except TypeError:
        break

