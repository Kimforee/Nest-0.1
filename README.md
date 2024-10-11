# Nest 0.1
 New version of Nest Application

### Nest Admin :
![image](https://github.com/user-attachments/assets/e5c14c98-cbe7-4601-8c84-5998ba883315)

### Landing Page :
![image](https://github.com/user-attachments/assets/78172233-a87c-4791-a9d6-7d21b24492b6)

### Inside Nest :
![image](https://github.com/user-attachments/assets/e0e78210-556e-4ac0-8e7d-79137e81e4ab)

### Public Profile :
![image](https://github.com/user-attachments/assets/46ec37ec-64f1-485e-ac8e-5cccee0fc395)

# LearnNest - Django Web Application

LearnNest is a web-based platform built using Django that integrates real-time features using Django Channels and Redis. This project showcases the use of neomorphic design for the user interface and handles asynchronous events like WebSocket connections for real-time messaging.

## Features

- User profile management with edit functionality
- Real-time messaging powered by Django Channels
- Redis-based message broker for asynchronous events
- Neomorphic UI design
- User authentication and profile system
- Join request handling for various "nests" (groups)

## Tech Stack

- **Backend**: Django 4.x
- **Frontend**: HTML, CSS (Neomorphic design)
- **Database**: PostgreSQL (can be replaced with other databases)
- **Real-Time Communication**: Django Channels, WebSockets
- **Message Broker**: Redis
- **Environment Management**: Python Virtual Environment (`venv`)

## Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/Kimforee/Nest-0.1.git
cd Nest-0.1
```

### 2. Set up the virtual environment

Make sure Python is installed on your system. Then, set up a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies

After activating the virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set up Redis

Make sure Redis is installed and running on your system. For example, you can install Redis via:

- **macOS** (using Homebrew):
  ```bash
  brew install redis
  ```
- **Ubuntu**:
  ```bash
  sudo apt-get install redis-server
  ```
- **Windows**: 
  Use [Redis for Windows](https://github.com/MicrosoftArchive/redis/releases) or use Docker to run Redis.

Start the Redis server:

```bash
redis-server
```

### 5. Update Django Settings

In `settings.py`, make sure you have configured Redis for Channels:

```python
# settings.py
ASGI_APPLICATION = 'your_project_name.routing.application'

# Redis Channel Layer
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],  # Redis running locally
        },
    },
}
```

### 6. Migrate the database

Run the following command to apply migrations:

```bash
python manage.py migrate
```

### 7. Start the Django development server

You can now run the Django development server:

```bash
python manage.py runserver
```

### 8. Run the Channels worker

In a new terminal (with the virtual environment activated), start the Channels worker:

```bash
python manage.py runworker
```

### 9. Run Redis for WebSocket Support

Start the Redis server to handle WebSocket connections:

```bash
redis-server
```

## Usage

- Access the application at `http://127.0.0.1:8000`.
- Real-time functionality (such as messaging) will work through Django Channels and Redis.
  
## Testing

To run the unit tests (unit testing not yet initaited):

```bash
python manage.py test
```

## Neomorphic Design

This project incorporates neomorphic design for user profile interfaces. Neomorphism combines minimalism with soft shadows and highlights to create depth. You can find the neomorphic UI in the profile pages and buttons across the application.

## Channels and Redis

This project uses Django Channels and Redis for handling real-time WebSocket communication. Redis acts as the message broker, allowing Channels to handle asynchronous messages and real-time events.

- **Django Channels**: Extends Django’s built-in capabilities to handle WebSocket connections and other asynchronous protocols.
- **Redis**: Serves as the message broker for Django Channels, ensuring efficient communication between server and client.

## Contributing

Feel free to submit pull requests or raise issues. All contributions are welcome.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/feature-name`)
5. Open a pull request

## License

This project is licensed under the MIT License.
```

### Explanation:
- **Project setup**: Guides users on how to install and run the project locally using `venv`, Redis, and Django Channels.
- **Real-time features**: Highlights the integration of Redis and Django Channels for WebSocket handling.
- **File structure**: Provides an overview of the core directories and files.
- **Neomorphic design**: Describes the user interface design used in the project.

Feel free to adjust the content to match the specifics of your project.
