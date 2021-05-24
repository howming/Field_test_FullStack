## Field_test_FullStack

### 1. Write a program to decode and process CSV file into a database table
  - 1 CSV file are located in /root/
    - filename: dns_sample.csv
  
  - You must write an import program (any language you choose, Ex: Perl / Python / PHP)
    - Directory: /root
    - Program name: Ex: import.pl / import.py / import.php
  
  - In the CSV file you could see the following fields:
    - frame.time_epoch : UNIX timestamp in nanoseconds
    - ip.src : source ip address
    - udp.srcport : source port
    - ip.dst : destination ip address
    - udp.dstport : destination port
    - dns.qry.name : DNS A record query (FQDN)
    
  - You must create a database table with the following fields:
    - Date
    - Time
    - usec
    - SourceIP
    - SourcePort
    - DestinationIP
    - DestinationPort
    - DNS A record query (FQDN) (eg: www.apple.com)
  
  5. The program (import) shall read the CSV files and import into the database table (1.4) filling the fields packet by packet.
  
### 2. Build a website to search the database by the following fields:
  - Source IP
  - Time range (from ~ to)
  - FQDN
  
### 3. Must have a login page for user password input

### 4. The Search function should list the following fields in a table:
  - Date, Time, usec, SourceIP, SourcePort, DestinationIP, DestinationPort, FQDN
  - The Search Result page should order by Date/Time/usec in Ascending order.
  - The Search function should have pagination functions and show only 50 records per page
