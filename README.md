# stock-app
This is a repo that is a showcase for using docker, docker compose, and orchestrating all the pieces that fit in together when using Rasa as a chatbot building tool.
## Requirements
- docker compose version 2.14.1
## Instructions
1. First of all, you have to have environment variables in place for the docker compose to be able to pick up.
The easiest way to do so would be to supply a `.env` file. 
In order to speed up the startup process, there is a `.env.example` file that you can start with.
Feel free to change the values as needed and rename `.env.example` to `.env`. 

2. Run `docker compose build` in order to build all the services.
In order to spin up all the services that are interacting once they're built, run `docker compose up`.

3. After spinning up all the services, you'll be able to interact with your Rasa bot through a REST API available on `http://127.0.0.1:5005/webhooks/rest/webhook`.
Messages are sent to the bot in the form of a json like this:
```json
{
  "sender": "test_user",
  "message": "hi"
}
```
Now, you can even inspect what is going on in mongo what talking to the bot by inspecting what is available in it through `mongo-express` via `http://127.0.0.1:8081`.

### Note:
There is a possibility that the `bot` service won't be able to publish the messages to the queue. 
This is possible due to `bot` service channel being closed due to failure when there is no queue setup, 
no consumers being set or heartbeat missed.
In order to bypass this issue, if you get an error once you send a message to the bot, 
issue `docker compose restart bot` in order to restart the bot service.
After the restart everything should work just fine.

## Future work
Integrate ElasticSearch to be able to index and analyze data that is coming in to the bot, 
what stocks are being searched upon most often, which ones are interesting to based on user similarity, etc.