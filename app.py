class Comment:
    def __init__(self):
        self.comment = []


def add_comment(self, message, author):
    comment = {}
    comment["message"] = message
    comment["author"] = author
    self.comment.append(comment)
    return{"message": "Comment added successfully"}

def edit_comment(self, message, author):
    if comment in self.comment:
        self.comment.update(comment)
        return{"message": "Comment updated successfully"}