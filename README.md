# QuartzAI

QuartzAI is a versatile AI bot and server implemented in Python. It leverages advanced AI techniques to provide chat completions, image generation, Text-to-Speech (TTS), and key/usage commands. The server exposes endpoints for chat, images, audio, and moderation, making it a comprehensive solution for various AI needs.

## Features

### bot.py

`bot.py` is a script that runs the QuartzAI bot. The bot provides the following features:

- **Chat completions**: Generate intelligent and contextually aware chat completions.
- **Image Generation**: Create images based on specific parameters or prompts.
- **Text-to-Speech (TTS)**: Convert text input into spoken words.
- **Key / Usage commands**: Execute specific commands based on user input.

To run the bot, use the following command:

```bash
python bot.py
```

### server.py

`server.py` is a script that runs the QuartzAI server. The server provides the following endpoints:

- **/v1/chat**: Endpoint for handling chat interactions.
- **/v1/images**: Endpoint for generating and serving images.
- **/v1/audio**: Endpoint for handling TTS requests and serving audio files.
- **/v1/moderation**: Endpoint for handling moderation tasks.

To start the server, use the following command:

```bash
python server.py
```

## Installation

To install the dependencies for this project, run the following command:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.

## Contributing

We welcome contributions to QuartzAI! If you have a bug fix, improvement, or new feature you'd like to add, please follow these steps:

1. Fork this repository.
2. Create a new branch in your forked repository.
3. Make your changes in the new branch.
4. Submit a pull request from the new branch in your forked repository to the main branch in the original repository.

Before submitting a pull request, please open an issue to discuss the changes you want to make.

## Contact

If you have any questions, issues, or just want to get in touch, feel free to reach out to us.
