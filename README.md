# Recipe App 🍕
Cal State LA CS 3035 Programing Paradigms

## Overview
This Recipe App is a console-based application that allows users to search for and manage cooking recipes using the TheMealDB API. Built with Python, the app incorporates concepts from the Model-View-Controller (MVC) architecture to maintain a clean and organized codebase.

## Features

- List all meal categories
- View meals by category
- Search for meals by name
- Get a random meal suggestion
- List all culinary areas
- View meals by area
- Manage favorite recipes

## Architecture
The app follows the MVC architectural pattern:

### 1 Model
- `Category.py`: Represents a meal category
- `Meal.py`: Represents an individual meal
- `Recipe.py`: Represents detailed recipe information

### 2 View
- `consoleUI.py`: Handles the console-based user interface

### 3 Controller
- `Request.py`: Manages API communication and business logic

## Technology Stack
- Python 3
- requests library: For API communication
- colorama library: For console output styling

## API
This app utilizes the TheMealDB API to fetch recipe data.
