# Field_test_FullStack
1. Write a program to decode and process CSV file into a database table
  1.1 1 CSV file are located in /root/
    1.1.1 CSV filename: dns_sample.csv
  1.2 You must write an import program (any language you choose, Ex: Perl / Python / PHP)
    1.2.1 Directory: /root
    1.2.2 Program name: Ex: import.pl / import.py / import.php
  1.3 In the CSV file you could see the following fields:
    1.3.1 frame.time_epoch : UNIX timestamp in nanoseconds
    1.3.2 ip.src : source ip address
    1.3.3 udp.srcport : source port
    1.3.4 ip.dst : destination ip address
    1.3.5 udp.dstport : destination port
    1.3.6 dns.qry.name : DNS A record query (FQDN)
  1.4 You must create a database table with the following fields:
    1.4.1 Date
    1.4.2 Time
    1.4.3 usec
    1.4.4 SourceIP
    1.4.5 SourcePort
    1.4.6 DestinationIP
    1.4.7 DestinationPort
    1.4.8 DNS A record query (FQDN) (eg: www.apple.com)
  1.5 The program (import) shall read the CSV files and import into the database table (1.4) filling the fields packet by packet.
  
2. Build a website to search the database by the following fields:
  2.1 Source IP
  2.2 Time range (from ~ to)
  2.3 FQDN
  
3. Must have a login page for user password input

4. The Search function should list the following fields in a table:
  4.1 Date, Time, usec, SourceIP, SourcePort, DestinationIP, DestinationPort, FQDN
  4.2 The Search Result page should order by Date/Time/usec in Ascending order.
  4.3 The Search function should have pagination functions and show only 50 records per page
