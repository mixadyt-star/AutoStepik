# Automatic course solving on Stepik
*Read this in other languages: [English](README.md), [Русский](README.ru.md)*

This project is a simple automated system for solving tasks on the Stepik website. It includes a solver based on the OpenRouter API, a service that provides free models for use.
## Installation
1.  Clone the repository:
    ```bash
    git clone https://github.com/mixadyt-star/AutoStepik.git
    cd AutoStepik
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
## Usage
### Configuration
To use the script, you need to configure the solver and enter your account credentials in the main.py file.
#### Solver configuration
In the AiSolver class constructor, enter your OpenRouter API token and the model you wish to use in the token and model fields respectively. Here is an example of a configured solver:

    solver = AiSolver(
        ai_client=OpenRouterClient(
            token="sk-or-v1-fcbc04b76faa0...", # Get one at https://openrouter.io/keys
            model="xiaomi/mimo-v2-flash:free" # List of models can be found here: https://openrouter.ai/models
        ),
    )
#### Client configuration
Pass your Stepik account email and password to the AutoStepik class constructor in the email and password fields respectively.
You can also set the number of parallel processes with the max_workers argument (it is not recommended to use more than 20 processes). Here is an example of a configured client:

    AutoStepik(
        email="example@gmail.com",
        password="ExamplePassword123!!",
        solver=solver,
        max_workers=10,
    ).solve()
    
### Running the script
To start the automatic task solving process, run the following command:

    python main.py

During operation, the program will ask you to select the course you want to solve. You make your choice by entering the number corresponding to the desired course. Here is an example of the selection menu:

    Choose course:
      1. "Python Generation": a course for beginners
    AutoStepik > 1

## License
This project is distributed under the MIT License.
