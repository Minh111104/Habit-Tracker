# Pixela Habit Tracking with Python 🏋️

This Python script integrates with the [Pixela API](https://pixe.la/) to help you track your daily habits or metrics, such as running distances. Using the Pixela API, this project allows you to create an account, set up a graph, and log your progress over time.

## Table of Contents

- [Overview](#overview)
- [Project Setup](#project-setup)
- [Features](#features)
- [Usage](#usage)
- [Requirements](#requirements)
- [Notes](#notes)

## Overview

Pixela is a tool for tracking various habits in the form of graphs. This script simplifies the process by automating:
1. Account creation
2. Graph creation
3. Daily tracking of activities (like running)
4. Updating or deleting entries for specific dates

## Project Setup

1. **Sign Up on Pixela**:
   - Pixela requires users to create a unique token and username. You can generate an account directly through the script.

2. **Configure Environment Variables**:
   - Replace `USERNAME` and `TOKEN` in the code with your Pixela username and token, or store them securely as environment variables.

3. **Define Graph**:
   - Customize `graph_config` to specify the graph’s properties (name, unit, type, and color).

## Features

- **Create a Pixela Account**: Sends an HTTP POST request to register a new user on Pixela.
- **Create a Graph**: Sets up a visual representation of your habit (e.g., “Running Graph” with units in kilometers).
- **Track Daily Metrics**: Records daily metrics by sending a POST request with a specified quantity.
- **Update Existing Entry**: Modifies a specific day’s entry.
- **Delete Entry**: Removes a specific day’s entry.

## Usage

1. **Initialize Pixela Account** (Uncomment line as needed):
    ```python
    response = requests.post(url=pixela_endpoint, json=user_params)
    ```

2. **Create Graph** (Uncomment as needed):
    ```python
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    ```

3. **Log Daily Data**:
    - Run the script and enter the number of kilometers run (or other metrics).
    - The script logs this value to your graph on Pixela.

4. **Update Data** (Optional):
    - Adjust `new_pixel_data` to change an entry for the current day.

5. **Delete Data** (Optional):
    - Deletes the specific day’s entry if needed.

## Requirements

- `requests` library
- Pixela account (username and token)

## Notes

- Pixela provides additional options for tracking different types of data, changing graph styles, and setting up multiple graphs. Refer to the [Pixela API documentation](https://docs.pixe.la/) for advanced usage.
- Make sure to keep your token secure, as it is used for authentication.
