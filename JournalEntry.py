from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime

# Create a Base object for the ORM
Base = declarative_base()

# Define the journal_entries table as a class


class JournalEntry(Base):
    __tablename__ = 'journal_entries'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))  # Specify a length of 50 characters for the title column
    body = Column(String(2000))
    created_at = Column(DateTime)

    def __init__(self, title, body, created_at):
        self.title = title
        self.body = body
        self.created_at = created_at

    def __repr__(self):
        return f'<JournalEntry(title={self.title}, {self.body}, {self.created_at}'


def get_session():
    # Connect to the database
    engine = create_engine('mysql://user:@127.0.0.1:3306/test')

    # Create the journal_entries table in the database if it does not exist
    Base.metadata.create_all(engine)

    # Create a session to manage the persistence of objects
    Session = sessionmaker(bind=engine)
    session = Session()

    return session


def save_entry(entry):
    session = get_session()
    session.add(entry)
    session.commit()

def display_entries():
    # Get a session to the database
    session = get_session()

    # Execute a SELECT statement to retrieve all the journal entries
    entries = session.query(JournalEntry).all()

    # Iterate over the entries and print them to the screen
    for entry in entries:
        print(f'Title: {entry.title}')
        print(f'Body: {entry.body}')
        print(f'Created At: {entry.created_at}')
        print()  # Add a blank line for readability

