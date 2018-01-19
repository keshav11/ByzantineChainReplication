## Byzantine Chain Replication
An implementation of Byzantine Chain Replication based on- 

van Renesse R., Ho C., Schiper N. (2012) Byzantine Chain Replication. In: Baldoni R., Flocchini P., Binoy R. (eds) Principles of Distributed Systems. OPODIS 2012. Lecture Notes in Computer Science, vol 7702. Springer, Berlin, Heidelberg

The described system requires 2t+1 replicas to tolerate t Byzantine failures.

### Motivation
This was done as course project for the course [CSE 535 Asyschronous Systems](http://www3.cs.stonybrook.edu/~stoller/cse535/) at Stony Brook University taught by Professor Scott Stoller.

### Instructions
1. Unzip the release zip in your Windows 10 PC. Go to the root of the unzipped folder.
2. Put your config file in config folder.
3. Open two command line terminals
4. In the first terminal run the following command with <config_file_name.txt> as the argument
    python -m da --logfile -n MainNode --logfilename logs\log_verify_result_single_client_2_mainnode.txt -F info --message-buffer-size 100000  src\bcr.da <config_file_name.txt>
5. In the second terminal run the following command with <config_file_name.txt> as the argument
    python -m da --logfile -n ClientNode --logfilename logs\log_verify_result_single_client_2_clientnode.txt -F info --message-buffer-size 100000  src\bcr.da <config_file_name.txt>

For example to run test case 1:
1. open 2 command line terminals
2. on terminal 1 run the following command-
    python -m da --logfile -n MainNode --logfilename logs\log_verify_result_single_client_2_mainnode.txt -F info --message-buffer-size 100000  src\bcr.da config_result_verify_testcase_2.txt
3. on terminal 2 run the following command-
    python -m da --logfile -n ClientNode --logfilename logs\log_verify_result_single_client_2_clientnode.txt -F info --message-buffer-size 100000  src\bcr.da config_result_verify_testcase_2.txt

### Workload Generation
Algorithm:

```
pseudorandom(seed, n):
    initialize python's random number generator with the specified seed.
    for i in range(n):
        generate a random number from 1 to 4 and map it to (get put slice append)
        generated key and value using random to generate 4 random lowercase character
```

### Main Files
* src/bcr.da
* src/client.da
* src/object.py
* src/olympus.da
* src/replica.da


### Platform
```
OS: Windows 10
DistAlgo version: 1.0.9
Python implementation: CPython
Python version: 3.5
```
### Contributors
* Keshav Gupta
* Pratik Zambani
