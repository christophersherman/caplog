import datetime
import argparse
from JournalEntry import get_session, save_entry, display_entries
from JournalEntry import JournalEntry






# Create an ArgumentParser object
parser = argparse.ArgumentParser()
#parser.add_argument('-f', '--file', help='The input file')
#parser.add_argument('-o', '--output', help='The output file')
parser.add_argument('--show-help', action='store_true', help='Show this help message and exit')
args = parser.parse_args()

# Print the help message if the --help flag is provided
if args.show_help:
    parser.print_help()

#save_entry(JournalEntry("Second Journal Entry", "This is the second test entry", datetime.datetime.now()))

#display_entries()



