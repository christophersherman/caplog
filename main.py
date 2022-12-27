from datetime import datetime, timedelta
import argparse
from JournalEntry import get_session, save_entry, display_entries
from JournalEntry import JournalEntry


# Define a custom type for the time argument
def time_type(string):
    try:
        date_format = '%Y-%m-%dT%H:%M:%S'
        date_tuple = datetime.strptime(string, date_format)
        return date_tuple
    except ValueError:
        if string == 'today':
            return datetime.now()
        elif string == 'yesterday':
            return datetime.now() - timedelta(days=1)
        else:
            raise argparse.ArgumentTypeError(f'Invalid time: {string}')


# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add arguments and options to the parser
parser.add_argument('time', nargs='?', type=time_type, help='The time of the journal entry (today or yesterday)')
parser.add_argument('entry', nargs='*', help='The journal entry (title and body)')
parser.add_argument('-l', '--list', action='store_true', help='List all journal entries')

# Parse the command-line arguments and options
args, unknown_args = parser.parse_known_args()

# Check if no arguments were provided
if not unknown_args and not any(vars(args).values()):
    parser.print_help()
else:
    time = args.time
    entry = ' '.join(args.entry)
    list_entries = args.list
    # Print the help message if the --help flag is provided
    
    # Split the entry into a title and body
    if entry:
        title, body = entry.split('.', 1)
        title = title+'.'
    else:
        title, body = '', ''

    # Use the parsed arguments and options in your script
    if list_entries:
        display_entries()
    else:
        #create_stuff
        entry = JournalEntry(title=title, body=body, created_at=time)
        print(entry)
