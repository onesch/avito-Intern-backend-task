## **Avito Tech Internship Backend Test Assignment**

The goal is to **develop a chat server** that provides an `HTTP API` for working with chats and user messages.

Source: https://solvit.space/test-tasks/1

## Development:
- Core entities:
    - [x] [User](https://github.com/onesch/avito-Intern-backend-task/pull/1).
    - [ ] Message.
    - [ ] Chat.
- - [x] [Set up data storage](https://github.com/onesch/avito-Intern-backend-task/pull/1).
- Main API methods:
    - [x] [Add a new user](https://github.com/onesch/avito-Intern-backend-task/pull/1).
        ```
        curl -X POST "http://127.0.0.1:9000/users/create-user" -H "Content-Type: application/json" -d '{"username": "test"}'
        ```
    - [ ] Create a new chat between users.
    - [ ] Send a message to a chat on behalf of a user.
    - [ ] Get the list of chats for a specific user.
    - [ ] Get the list of messages in a specific chat.
- - [x] Provide instructions for running the application.

### Bonus:
- - [ ] Use containerization with the ability to run the project using `docker-compose up`.

## Run:
Project uses SQLAlchemy, Pydantic and PostgreSQL.

##### 0. Clone
```bash
git clone https://github.com/onesch/avito-Intern-backend-task.git
cd avito-Intern-backend-task
```

##### 1. Uv
```bash
pip install uv
# or
curl -Ls https://astral.sh/uv/install.sh | sh
```

##### 2. Depends
```bash
uv sync
```

##### 3. Env
```bash
cp .env.example .env
```

##### 4. Database
```bash
createdb chat_db
```

##### 5. Server
```bash
make run
# or
uv run uvicorn app.main:app --reload --port 9000
```
