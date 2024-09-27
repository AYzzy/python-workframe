
import unittest

from DIARY.Diary import Diary


class TestDiary(unittest.TestCase):

    def test_that_diary_is_locked(self):
        diary = Diary(1, "ttt", "ttthb")
        diary.locked = True
        self.assertTrue(diary.Unlocked)

    def test_that_diary_is_unlocked(self):
        diary = Diary(1, "jhbkjn", "mhb")
        diary.unlockEntry("mhb")
        self.assertTrue(diary.unlockEntry)

    def test_to_create_diary(self):
        diary = Diary(1, "the", "the best")
        diary.unlockEntry("the best")
        diary.createEntry(1, "Test", "hello world")
        diary.locked = True
        self.assertEqual(1, diary.getEntriesSize())

    def test_to_delete_diary(self):
        diary = Diary(1, "the", "the best")
        diary.createEntry(1, "Test", "hello")
        diary.createEntry(2, "Test", "hello world")
        diary.deleteEntry(1)
        self.assertEqual(1, diary.getEntriesSize())

    def test_to_delete_diary_with_invalid_entry(self):
        diary = Diary(1, "the", "the best")
        diary.createEntry(1, "Test", "hello")
        diary.createEntry(2, "Test", "hello world")
        # diary.deleteEntry(-1)
        self.assertRaises(ValueError, lambda: diary.deleteEntry(4))

    def test_to_find_diary_(self):
        diary = Diary(1, "the", "the best")
        diary.createEntry(1, "Test", "hello")
        diary.createEntry(2, "Test", "hello world")
        diary.createEntry(3, "semicolon", "choose your hard")
        diary.findEntry(2)
        entry = diary.findEntry(2)
        self.assertEqual(entry, diary.findEntry(2))

    def test_to_update_diary_(self):
        diary = Diary(1, "the", "the best")
        diary.createEntry(1, "Test", "hello")
        diary.createEntry(2, "Test", "hello world")
        diary.createEntry(3, "semicolon", "choose your hard")
        # diary.updateEntry(2,"Semicolon Africa", "THE BEST OF THE BEST")
        entry = diary.updateEntry(2, "Semicolon Africa", "THE BEST OF THE BEST")
        self.assertEqual(entry, diary.updateEntry(2, "Semicolon Africa", "THE BEST OF THE BEST"))
