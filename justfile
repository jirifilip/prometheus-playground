set shell := ["powershell.exe"]


dev:
    docker compose down
    docker compose build
    docker compose up

clean:
    docker compose down
