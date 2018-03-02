import unittest

from app import Comment


class Test1(unittest.TestCase):
    def test_add_comment(self):
        response = comment.add_comment("Pleasure working with you", "Jane Doe")
        self.assertEqual(response["message"], "Comment added successfully")

    def test_edit_comment(self):
        response = comment.update_contact(comment)
        self.assertEqual(response["message"], "Comment contact successfully")