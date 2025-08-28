# Python Quiz Games

### Project Overview

This repository contains two versions of a command-line quiz game built with Python. These projects are designed to demonstrate the progression from basic programming concepts to more advanced data structures and application logic.

-   **Basic Quiz Game (`quiz_game_basic.py`):** A simple quiz that presents a series of multiple-choice questions to the user and calculates their score.
-   **Category-Based Quiz Game (`quiz_game_advanced.py`):** An enhanced version that allows users to choose a quiz category. This project uses a more complex data structure (dictionary of lists) to manage questions, showcasing how to build a scalable and organized application.

### Features

#### **Basic Quiz Game (`quiz_game_basic.py`)**

-   **Interactive:** Asks questions and provides immediate feedback.
-   **Scoring System:** Tracks and displays the final score.
-   **Structured Data:** Stores questions in a simple list of dictionaries.

#### **Category-Based Quiz Game (`quiz_game_advanced.py`)**

-   **Category Selection:** Users can choose from multiple quiz categories (e.g., General Knowledge, Math, Science).
-   **Dynamic Content:** The quiz dynamically loads questions based on the user's selected category.
-   **Advanced Data Structure:** Uses a **dictionary of lists of dictionaries** to organize questions by category, a great example of real-world data management.
-   **Robust Error Handling:** The program includes `try-except` blocks to handle invalid category selections.

### How to Run

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd <project-directory-name>
    ```
3.  **To run the Basic Quiz:**
    ```bash
    python quiz_game_basic.py
    ```
4.  **To run the Category-Based Quiz:**
    ```bash
    python quiz_game_advanced.py
    ```

### Example Usage (Category-Based Quiz)

```bash
$ python quiz_game_advanced.py

----------------------------------------------------------
------------------ Welcome to the Quiz Game! -------------
----------------------------------------------------------

Available Categories:
1. General Knowledge
2. Math
3. English
4. Science
5. Technology
0. Exit
Choose a category (0 to exit): 2

--- You selected: Math ---

What is the value of 2 + 2 * 3?
A. 12
B. 8
C. 10
D. 6
Give Your Answer (A/B/C/D): B
✅ Correct Answer!

... (Quiz continues) ...

--------------------
Quiz End!
Your Total Score: 3/3
--------------------