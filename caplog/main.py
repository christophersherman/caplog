from datetime import datetime, timedelta
import re
import argparse
from journalentry import save_entry, display_entries, JournalEntry


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

def scrape_tags(string):
    # Use a regular expression to find all words that start with @
    tags = re.findall(r'\B@\w+', string)
    # Return the list of tags as a comma-separated string, or an empty string if no tags were found
    return ','.join(tags) if tags else ''


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()

    # Add arguments and options to the parser
    parser.add_argument('time', nargs='?', type=time_type,  help='The time of the journal entry (today or yesterday)')
    parser.add_argument('entry', nargs='*',  help='The journal entry (title and body)')
    parser.add_argument('-l', '--list', action='store_true', help='List all journal entries')

    # Parse the command-line arguments and options
    args = parser.parse_args()

    # If no arguments are passed, display the help information
    if not any(vars(args).values()):
        parser.print_help()
        return

    # Continue with the rest of the code
    time = args.time
    entry = ' '.join(args.entry)
    list_entries = args.list
    
    # Split the entry into a title and body
    if entry:
        title, body = entry.split('.', 1)
        title = title+'.'
        tags = scrape_tags(body)
    else:
        title, body = '', ''

    # Use the parsed arguments and options in your script
    if list_entries:
        display_entries()
    else:
        #create_stuff
        entry = JournalEntry(title=title, body=body, tags=tags, created_at=time)
        save_entry(entry)


if __name__ == '__main__':
    main()
