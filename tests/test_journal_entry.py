import unittest
import datetime
import os, sys
from sqlalchemy.orm import Session

# Add the directory containing `journalentry.py` to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../caplog")))

from journalentry import JournalEntry, get_session, save_entry, display_entries, remove_entry

class TestJournalEntry(unittest.TestCase):
    def setUp(self):
        os.environ['TESTING'] = "true"
        # Create a new JournalEntry object and save it to the database
        self.entry = JournalEntry('Test Title', 'Test Body', '@test', datetime.datetime.now())
        save_entry(self.entry)

    def test_get_session(self):
        # Call the get_session function
        session = get_session()

        # Assert that the returned object is a session
        self.assertIsInstance(session, Session)


    def test_save_entry(self):

        # Create a new session
        session = get_session()

        # Execute a SELECT statement to retrieve all the journal entries
        entries = session.query(JournalEntry).all()

        # Assert that the number of entries retrieved is 1
        self.assertEqual(len(entries), 1)
        # Assert that the title of the entry is correct
        self.assertEqual(entries[0].title, 'Test Title')
        # Assert that the body of the entry is correct
        self.assertEqual(entries[0].body, 'Test Body')
        # Assert that the tags of the entry are correct
        self.assertEqual(entries[0].tags, '@test')
        # Assert that the created_at field of the entry is within 1 second of the current time
        self.assertAlmostEqual(entries[0].created_at, datetime.datetime.now(), delta=datetime.timedelta(seconds=1))
    
    def test_display_entries(self):
        # Call the display_entries function
        display_entries()

        session = get_session()
        
        # Execute a SELECT statement to retrieve all the journal entries
        entries = session.query(JournalEntry).all()

        # Assert that the number of entries retrieved is 1
        self.assertEqual(len(entries), 1)
        # Assert that the title of the entry is correct
        self.assertEqual(entries[0].title, 'Test Title')
        # Assert that the body of the entry is correct
        self.assertEqual(entries[0].body, 'Test Body')
        # Assert that the tags of the entry are correct
        self.assertEqual(entries[0].tags, '@test')
        # Assert that the created_at field of the entry is within 1 second of the current time
        self.assertAlmostEqual(entries[0].created_at, datetime.datetime.now(), delta=datetime.timedelta(seconds=1))

    def tearDown(self):
        # Create a new session
        session = get_session()

        # Reattach the entry to the session using the merge method
        entry = session.merge(self.entry)

        # Store the ID of the entry
        entry_id = entry.id

        # Remove the entry from the database
        remove_entry(entry_id)







if __name__ == '__main__':
    unittest.main()