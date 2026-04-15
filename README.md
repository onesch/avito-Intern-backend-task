### **Avito Tech Internship Backend Test Assignment**

The goal is to **develop a chat server** that provides an `HTTP API` for working with chats and user messages.

Source: https://solvit.space/test-tasks/1

### Development:
- Core entities:
    - [x] User.
    - [ ] Message.
    - [ ] Chat.
- - [x] Set up data storage.
- Main API methods:
    - [x] Add a new user.
        ```
        curl -X POST "http://127.0.0.1:9000/users/create-user" -H "Content-Type: application/json" -d '{"username": "test"}'
        ```
    - [ ] Create a new chat between users.
    - [ ] Send a message to a chat on behalf of a user.
    - [ ] Get the list of chats for a specific user.
    - [ ] Get the list of messages in a specific chat.
- - [ ] Provide instructions for running the application.

### Bonus:
- - [ ] Use containerization with the ability to run the project using `docker-compose up`.
