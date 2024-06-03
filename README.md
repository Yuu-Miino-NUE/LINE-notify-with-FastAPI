# LINE Notify with FastAPI
## Description
- LINE Notify via the request to the FastAPI server.
- Docker image is available from this repository.

## Usage
### Create image
```sh
docker build -t line-notify-by-fastapi .
```
### Get LINE Notify Token
Refer to [LINE Notify](https://notify-bot.line.me/en/).

### Put the token
The system uses the dotenv file in `conf` directory, i.e., `conf/.env`.
```sh
LINE_NOTIFY_TOKEN="YOUR_TOKEN"
```

### Run the container
For single service, run the container with the following command.
```sh
docker run -v ./conf:/code/conf -d -p 80:80 line-notify-by-fastapi
```

For docker-compose, please refer to the `docker-compose.yml` file and combine it with your services.
