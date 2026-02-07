#!/usr/bin/env python
import sys
import igc_lib
import json

def main():
    if len(sys.argv) < 2:
        print("Usage: %s file.igc [file.lkt]" % sys.argv[0])
        sys.exit(1)

    input_file = sys.argv[1]
    task_file = None
    if len(sys.argv) > 2:
        task_file = sys.argv[2]

    flight = igc_lib.Flight.create_from_file(input_file)
    if not flight.valid:
        print("Provided flight is invalid:")
        print(flight.notes)
        sys.exit(1)

    print(json.dumps(json.loads(flight.flight_summary()), indent=2) )
        
if __name__ == "__main__":
    main()