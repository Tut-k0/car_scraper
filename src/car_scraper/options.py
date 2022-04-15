import argparse

from json import load
from typing import Union


def args() -> Union[dict, argparse.Namespace]:
    with open('../config.json') as config_file:
        config = load(config_file)

    # TODO: Find a 'better' way to choose configuration of parameters.
    if len(config) > 2:
        return config

    parser = argparse.ArgumentParser(
        description='Car scraper for auto tempest, specify parameters below.')
    parser.add_argument('-M', '--make', dest='make',
                        help="Make of the car, I.E Nissan")
    parser.add_argument('-m', '--model', dest='model',
                        help="Model of the car, I.E 370z")
    parser.add_argument('-z', '--zip', dest='zip', type=int, required=True,
                        help="ZIP code for the location to search from.")
    parser.add_argument('-r', '--radius', dest='radius', type=int,
                        required=True,
                        help='Radius around the given zip code to search.')
    parser.add_argument('-t', '--trim', dest='trim',
                        help='Specify the trim of the car here, I.E Sport Touring.')
    parser.add_argument('-k', '--keywords', dest='keywords',
                        help='Keywords to specify, separate with a "|", I.E apple carplay | aftermarket.')
    parser.add_argument('--minprice', dest='minprice', type=int,
                        help='Specify the search minimum price.')
    parser.add_argument('--maxprice', dest='maxprice', type=int,
                        help='Specify the search maximum price.')
    parser.add_argument('--minyear', dest='minyear', type=int,
                        help='Specify the search minimum year.')
    parser.add_argument('--maxyear', dest='maxyear', type=int,
                        help='Specify the search maximum year.')
    parser.add_argument('--minmiles', dest='minmiles', type=int,
                        help='Specify the search minimum mileage.')
    parser.add_argument('--maxmiles', dest='maxmiles', type=int,
                        help='Specify the search maximum mileage.')
    parser.add_argument('--transmission', dest='transmission',
                        help='Specify the search transmission type.')
    parser.add_argument('--title', dest='title',
                        help='Specify the state of the title.')
    parser.add_argument('--drive', dest='drive',
                        help='Specify the drive type, I.E rwd.')
    parser.add_argument('--fuel', dest='fuel',
                        help='Specify the fuel type, I.E gas.')
    parser.add_argument('-c', '--exterior_color', dest='exterior_color',
                        help='Specify the exterior color of the car.')
    parser.add_argument('--interior_color', dest='interior_color',
                        help='Specify the color of the interior.')
    parser.add_argument('-d', '--doors', dest='doors',
                        help='Specify the amount of doors the vehicle has.')
    parser.add_argument('--cylinders', dest='cylinders',
                        help='Specify the amount of cylinders the car has.')
    parser.add_argument('-b', '--bodystyle', dest='bodystyle',
                        help='Specify the body style of the vehicle.')

    options = parser.parse_args()

    return options
