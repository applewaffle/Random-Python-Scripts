from scapy.all import *
import argparse

parser = argparse.ArgumentParser(description="Visualize a .pcap file using scapy and afterglow.")
parser.add_argument("-c", "--conversations", help="Use this to view a conversations summary.",
	action="store_true")
parser.add_argument("-a", "--afterglow", help="Use this to view a complete viz, this is implied.",
	action="store_true")	
args = parser.parse_args()

if not len(sys.argv) > 1:
	print "Please use one of: -a, -c, or -h as an argument."

else:
	infile = raw_input('Please type an absolute path to the .pcap file: ')
	p=rdpcap(infile)
	print "Reading %s now." % infile

	if args.conversations:
		p.conversations()

	elif args.afterglow:
		p.afterglow()

print "Enjoy your visualization!"