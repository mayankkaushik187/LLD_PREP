from datetime import datetime
from typing import List
from vote import Vote
from votable import Votable
from commentable import Commentable
from tag import Tag

REP_FACTOR = 5


class Question(Votable, Commentable):
    def __init__(self, author, title, content, tags):
        self.title = title
        self.content = content
        self.author = author
        self.id = id(self)
        self.creation_date = datetime.now()
        self.answers = []
        self.tags = [Tag(name) for name in tags]
        self.votes = []
        self.comments = []

    def add_answer(self, answer):
        if answer not in self.answers:
            self.answers.append(answer)

    def vote(self, user, value):
        if value not in [-1, 1]:
            raise ValueError("Vote value must be either 1 or -1")
        self.votes = [v for v in self.votes if v.user != user]
        self.votes.append(Vote(user, value))
        self.author.update_reputation(value * REP_FACTOR)

    def get_vote_count(self):
        return sum(v.value for v in self.votes)

    def add_comments(self, comment):
        self.comments.append(comment)

    def get_comments(self):
        return self.comments.copy()
