from question import Question
from answer import Answer
from comment import Comment

REP_FACTOR = 5


class User:
    def __init__(self, user_id, username, email):
        self.id = user_id
        self.username = username
        self.email = email
        self.reputation = 0
        self.questions = []
        self.answers = []
        self.comments = []

    def post_question(self, title, content, tags):
        question = Question(self, title, content, tags)
        self.questions.append(question)
        self.update_reputation(REP_FACTOR)
        return question

    def answer_question(self, question, content):
        answer = Answer(self, question, content)
        self.answers.append(answer)
        question.add_answer(answer)
        self.update_reputation(2 * REP_FACTOR)
        return answer

    def comment_on(self, commentable, content):
        comment = Comment(self, content)
        self.comments.append(comment)
        commentable.add_comments(comment)
        self.update_reputation(2)
        return comment

    def update_reputation(self, value):
        self.reputation += value
        self.reputation = max(0, self.reputation)
