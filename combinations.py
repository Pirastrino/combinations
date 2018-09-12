import argparse
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
        f"{self.flight_number},{self.price},{self.bags_allowed},{self.bag_price}"
        

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
    return flights

def main():
    flights = load_data()
    flights.sort(key=lambda flight: (flight.destination, flight.departure))
    for flight in flights:
        print(flight)

if __name__ == '__main__':
    main()
