# C-array-to-.PCAP
A python utility that converts c-array of bytes into Wireshark readable .pcap file.

1. Save the c-array into a text file named ‘text1’. 

2. Note that text1 cannot have any comments or datatypes such as ‘char’ etc.  

3. Upon running the script, three files are generated. First and most important is your ‘pcap‘ file. Second is ‘binfile’ which is binary representation of text1. Lastly, the third file is ‘plaintext1.txt’ which is hexdump format file which is fed into text2pcap. 
