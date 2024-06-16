# Automatic LinkedIn Connections Acceptor

This repository contains a Python script that uses Selenium to automate the process of accepting LinkedIn connection requests. The script is designed to run in a Docker container, making it easy to deploy and manage.

## Features

- Automates the process of accepting LinkedIn connection requests.
- Runs headless using Firefox.
- Can be easily deployed using Docker.

## Requirements

- Docker
- A LinkedIn account

## Getting Started

### Prerequisites

Make sure you have Docker installed on your machine. You can download and install Docker from [here](https://www.docker.com/products/docker-desktop).

### Clone the Repository

```sh
git clone https://github.com/ChirayuGupta2003/Linkedin-Connections
cd Linkedin-Connections
```

### Environment Variables

Create a `.env` file in the root of the project directory and add your LinkedIn email and password:

```
EMAIL=your_linkedin_email
PASSWORD=your_linkedin_password
```

### Building the Docker Image

Use the following command to build the Docker image:

```sh
sudo docker build -t automatic_linkedin_connections .
```

### Running the Docker Container

Run the container with the following command:

```sh
sudo docker run --env-file .env automatic_linkedin_connections:latest
```

## File Structure

```
.
├── Dockerfile
├── README.md
├── main.py
├── requirements.txt
└── .env
```

- `Dockerfile`: Docker configuration for creating the Docker image.
- `main.py`: Python script for automating LinkedIn connection requests.
- `requirements.txt`: Python dependencies for the project.
- `.env`: Environment file containing LinkedIn credentials.

## Dependencies

The project dependencies are listed in the `requirements.txt` file. These dependencies are automatically installed when building the Docker image.

## Important Notes

- Ensure that your LinkedIn credentials are kept secure. Do not share or expose the `.env` file.
- Use this script responsibly and adhere to LinkedIn's terms of service.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Selenium](https://www.selenium.dev/) for providing a robust framework for web automation.
- [Docker](https://www.docker.com/) for containerization technology.

---

If you encounter any issues or have questions, feel free to open an issue or submit a pull request. Happy automating!
