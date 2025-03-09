## Requirements
1. User can post questions, answer questions, and comment on question and answers.
2. Users can vote on question and answers 
3. Questions should have tags associated with them.
4. Users can search for questions based on keywords, tags or even profile of the user.
5. The system should assign a score of rep, to users based on their activity on question and answers.
6. The system should handle concurrent access and ensure data consistency.


## Classes, Interfaces and Enumerations:
1. The User class can represent a user of the Stack Overflow system, User will have id, name, email, rep.
2. The Question class represents a question posted by a user, with properties such as id, title, content, author, answers, comments, tags, votes and creation date.
3. The Answer class should have id, content, author, associated question, comments, votes and creation date.
4. The Comment class will have id, content, author, creation date.
5. The Tag class will have id and name.
6. The Vote class will have a question/answer.
7. StackOverflow Class is the main class that manages teh Stack Overflow System. It provides with method for creating user, posting questions, answers and comments, voting on question and answers, searching for questions, and retrieving questions by tags and users.