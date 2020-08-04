#!/usr/bin/env python

import argparse

def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is getting sail.")

def list_ships():
    ships = ['Chevrolet', 'Toyota', 'Ford']
    print(f"Ships: {','.join(ships)}")

def greet(greeting, name):
    message = f"{greeting} {name}"
    print(message)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description= "Car models")
    parser.add_argument('--twice', '-t', help='Do it twice', action='store_true')
    subparsers =parser.add_subparsers(dest='func')
    ship_parser = subparsers.add_parser('ships', help='Car related commands')
    ship_parser.add_argument('command', choices=['list', 'sail'])

    sailor_parser = subparsers.add_parser('sailors', help='Talk to the saior')
    sailor_parser.add_argument('name', help='Sailors name')
    sailor_parser.add_argument('--greeting', '-g', help='Greeting', default='Ahoy there')
    args = parser.parse_args()

    if args.func == 'sailors':
        greet(args.greeting, args.name)
    elif args.command == 'list':
        list_ships()
    else:
        sail()