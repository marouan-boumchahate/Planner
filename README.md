# Task Manager Readme

## Introduction

Welcome to the Task Manager! This Python console-based application provides users with a simple and efficient way to manage their tasks. It includes features such as adding tasks, deleting tasks, and listing tasks based on various criteria like daily, weekly, or user-defined intervals.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Flowchart](#flowchart)

## Features

- Add, delete, and display tasks.
- Categorize tasks into daily, weekly, or user-defined intervals.
- Interactive console interface.
- Error handling for tasks with overlapping time intervals.
- Clear and visually appealing design.

## Requirements

- Python 3.5 and above

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Task-Manager.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Task-Manager
    ```

3. Run the application:

    ```bash
    python Project_Manager.py
    ```

## Usage

1. Run the application using the instructions provided in the installation section.
2. Navigate through the main menu to add, delete, or display tasks.
3. Choose specific options for displaying tasks, such as daily, weekly, or user-defined intervals.
4. Error handling ensures that tasks with overlapping time intervals are not allowed.
5. Enjoy an efficient and user-friendly way to manage your tasks.

## File Structure

- `Error_Exceptions.py`: Defines a custom exception class for handling time-related errors.
- `Project_Manager.py`: The main file containing the Project_Manager class, responsible for managing the user interface and task interactions.
- `__init__.py`: An empty file indicating that the directory should be treated as a Python package.
- `helper_functions.py`: Helper functions for user input, drawing screens, and checking time-related conditions.
- `task.py`: Defines the `clsTask` class representing a task object with methods for managing task attributes.
- `tasks_manager.py`: Implements the `Task_Manager` class responsible for managing tasks, including adding, deleting, and displaying tasks.

## Flowchart

Before delving into the code, take a look at the [Task Manager Flowchart](Planner_Project.png) to understand the logical flow of the game.
