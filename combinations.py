import argparse
import json
import sys
from datetime import datetime, timedelta


class Flight(object):
    
    def __init__(self, source, destination, departure, arrival, flight_number,
                 price, bags_allowed, bag_price):
        try:
            self.source = str(source)
            self.destination = str(destination)
            self.departure = datetime.strptime(departure, "%Y-%m-%dT%H:%M:%S")
            self.arrival = datetime.strptime(arrival, "%Y-%m-%dT%H:%M:%S")
            self.flight_number = str(flight_number)
            self.price = int(price)
            self.bags_allowed = int(bags_allowed)
            self.bag_price = int(bag_price)
        except Exception as e:
            print(e)

    def __repr__(self):
        departure = datetime.strftime(self.departure, "%Y-%m-%dT%H:%M:%S")
        arrival = datetime.strftime(self.arrival, "%Y-%m-%dT%H:%M:%S")
        return f"{self.source},{self.destination},{departure},{arrival},"\
               f"{self.flight_number},{self.price},{self.bags_allowed},"\
               f"{self.bag_price}"

    def to_json(self):
        flight = self.__dict__
        departure = datetime.strftime(self.departure, "%Y-%m-%dT%H:%M:%S")
        arrival = datetime.strftime(self.arrival, "%Y-%m-%dT%H:%M:%S")
        flight['departure'] = departure
        flight['arrival'] = arrival
        return f"{flight}"

class Combination(Flight):
    
    def __init__(self):
        try:
            self.min_connection_time = None
            self.max_connection_time = None
        except Exception as e:
            print(e)

    def __repr__(self):
        return f"{self.source},{self.destination} from {self.legs}"

    def set_connection_time(self, min_connection_time, max_connection_time):
        try:
            self.min_connection_time = int(min_connection_time)
            self.max_connection_time = int(max_connection_time)
        except Exception as e:
            print(e)

def load_data():  
    flights = []
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    args = parser.parse_args()
    infile = args.infile.read().splitlines()
    for line in infile:
        argv = line.split(",")
        flight = Flight(*argv)
        flights.append(flight)
    flights.sort(key=lambda flight: (flight.source, flight.departure))
    return flights

def map_sources(flights):
    index_map = {}
    for flight in flights:
        if flight.source not in index_map:
            index_map.setdefault(flight.source, []).append(
            flights.index(flight))
    return index_map

def main():
    flights = load_data()
    mapping = map_sources(flights)
    print(flights[0].to_json())
    print(mapping)
    comb = Combination()
    comb.set_connection_time(1, 4)
    print(comb.min_connection_time)
    print(comb.max_connection_time)

if __name__ == '__main__':
    main()
