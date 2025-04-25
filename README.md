# Voting App
This is a simple voting application built using Docker and Docker Compose. The app allows users to vote for their favorite option (e.g., Cats or Dogs), stores the votes in a PostgreSQL database via a Redis queue, and displays the results in real-time.

## Project Structure
The application consists of five services:

- **voting-app**: A Flask-based web app where users can cast their votes (runs on port 5000).
- **redis**: An in-memory queue to temporarily store votes.
- **worker**: A Python script that processes votes from Redis and saves them to the database.
- **db**: A PostgreSQL database to store votes persistently.
- **result-app**: A Flask-based web app to display the voting results (runs on port 5001).

All services are orchestrated using Docker Compose.

## Prerequisites
To run this project, you need the following installed on your system:

- Docker
- Docker Compose (or the integrated docker compose plugin)

## Setup Instructions

1. Clone the Repository:
```bash
git clone https://github.com/RoyTonmoy/Voting-app.git
cd Voting-app
```

2. **Build and Run the Application**:Use Docker Compose to build and start all services:
```bash
docker compose up --build
```

- If you’re using the legacy `docker-compose` binary, use:
```bash
docker-compose up --build
```

- This command builds the images for `voting-app`, `worker`, and `result-app`, pulls the `redis` and `postgres` images, and starts the containers.


3. Access the Application:

- Voting App: Open `http://localhost:5000` in your browser to cast votes.
- Result App: Open `http://localhost:5001` to view the voting results.



## Usage

1. Voting:

- Visit `http://localhost:5000`.
- Select an option (e.g., Cats or Dogs) and click "Vote".
- Votes are queued in Redis and processed by the `worker`.


2. Viewing Results:

- Visit `http://localhost:5001`.
- The page displays the current vote counts, updated as the `worker` processes votes.



## Project Architecture
The application follows a microservices architecture:

- **voting-app**: Collects user votes and pushes them to a Redis queue.
- **redis**: Temporarily stores votes in a list.
- **worker**: Reads votes from Redis and saves them to the PostgreSQL database.
- **db**: Persists the votes in a PostgreSQL database.
- **result-app**: Queries the database and displays the vote counts.

All services communicate over a custom Docker network (`voting-network`).
## Directory Structure
```plain
Voting-app/
├── docker-compose.yml       # Defines all services, networks, and volumes
├── voting-app/              # Voting web app
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── worker/                  # Background worker to process votes
│   ├── Dockerfile
│   ├── worker.py
│   └── requirements.txt
├── result-app/              # Results web app
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── result.html
```

## Stopping the Application
To stop the running containers:
```bash
docker compose down
```
Or, if using the legacy `docker-compose`:
```bash
docker-compose down
```
To also remove the database volume (this deletes all votes):
```bash
docker volume rm voting-app_pgdata
```
## Troubleshooting

- **Container Exits Unexpectedly**:

  - Check the logs for the failing service:
    ```bash
    docker compose logs <service_name>
    ```
    Example: `docker compose logs db`


- Port Conflicts:

  - If ports 5000 or 5001 are in use, modify the `ports` in `docker-compose.yml` (e.g., change `"5000:5000"` to `"5002:5000"`).


- Database Connection Issues:

  - Ensure the credentials in worker/worker.py and result-app/app.py match those in docker-compose.yml (POSTGRES_USER, POSTGRES_PASSWORD, 
    POSTGRES_DB).

## License
This project is licensed under the MIT License. See the LICENSE file for details.
