# LINE Notify with FastAPI
## Description
- LINE Notify via the request to the FastAPI server.
- Authentication will be realized via your environment variable `.env`.
- Docker image is available from this repository.

## Usage
### Create image
```bash
docker build -t line-notify-by-fastapi .
```
### Get LINE Notify Token
Refer to [LINE Notify](https://notify-bot.line.me/en/).

### Put the token
The system uses the dotenv file in `conf` directory, i.e., `conf/.env`.
```bash
LINE_NOTIFY_TOKEN="YOUR_TOKEN"
```

### Run the container
For single service, run the container with the following command.
```bash
docker run -v ./conf:/code/conf -d -p 80:80 line-notify-by-fastapi
```

For docker-compose, please refer to the `docker-compose.yml` file and combine it with your services.

```yaml
services:
    fastapi:
        image: line-notify-by-fastapi
        volumes:
            - ./conf:/code/conf
        environment:
            TZ: "Asia/Tokyo"
        ports:
            - "8000:8000"
        restart: always
```

Note that your `conf` directory should contain the `.env` file.

### Send a message
For example, send a message with the cURL command.
```bash
curl -X POST "http://localhost:8000/messages/" -d "message=Hello, LINE Notify!"
```

Please refer to the automatically generated Swagger UI for more details.
```bash
http://localhost:8000/docs
```
