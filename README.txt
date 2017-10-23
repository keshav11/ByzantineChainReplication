PLATFORM

INSTRUCTION

WORKLOAD GENERATION
Algorithm:
pseudorandom(seed, n):
    initialize python's random number generator with the specified seed.
    for i in range(n):
        generate a random number from 1 to 4 and map it to (get put slice append)
        generated key and value using random to generate 4 random lowercase character

BUGS AND LIMITATIONS


CONTRIBUTIONS
Keshav Gupta:
    olympus- create initial configuration: create keys, create, setup, and start processes
    generate pseudorandom workload with good diversity using specified seed
    all key generations and signature checks and validations
    timeout and send request to all replicas if timely response not received
    methods of dictionary object except slice and append
    handle retransmitted request as described in paper
    statement and signed result statement, send updated shuttle
    check validity of order proof (incl. signatures), add signed order
    check that dictionary contains expected content at end of test cases 1-6



MAIN FILES
src/bcr.da
src/client.da
src/object.py
src/olympus.da
src/replica.da

CODE SIZE
algorithm
other
total

LANGUAGE FEATURE USAGE.
list comprehensions
dictionary comprehensions
set comprehensions
aggregations
quantifications

OTHER COMMENTS

