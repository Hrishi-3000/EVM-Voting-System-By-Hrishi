# EVM-Voting-System-By-Hrishi

A GUI-based Electronic Voting Machine (EVM) application built using Python and Tkinter. This project demonstrates a simple yet effective implementation of an electronic voting system that includes voter authentication, live result visualization, theme toggling, and data export capabilities.

## Features

### 1. Admin Panel
- Add candidate names for the voting process.
- Reset the entire voting system to start fresh.
- Password-protected access to voting results.

### 2. Voter Panel
- Voter authentication using phone numbers (each phone number can vote only once).
- Cast votes by selecting from a list of candidates.

### 3. Results Panel
- Admin-only access to live voting results.
- Graphical visualization of voting results using pie charts.
- Export results to CSV and JSON formats.

### 4. Theme Toggle
- Switch between light mode and dark mode for better visibility.

### 5. Data Management
- Automatically prevents double voting by maintaining a record of phone numbers that have already voted.

## Code Structure

### Classes

1. **`EVM` Class**
   - Manages core functionalities of the voting system:
     - Candidate registration (`add_candidates`).
     - Voter authentication (`add_voter`).
     - Casting votes (`cast_vote`).
     - Displaying and exporting results.

2. **`EVMApp` Class**
   - Handles the GUI of the application using Tkinter.
   - Manages interactions between the user and the `EVM` class:
     - Admin panel for adding candidates and viewing results.
     - Voter panel for casting votes.
     - Results panel for viewing and exporting data.
   - Implements the theme toggling feature.

### Core Methods

- **Admin Actions**
  - `add_candidates`: Adds candidates to the system.
  - `reset_system`: Resets the voting system.

- **Voting Process**
  - `cast_vote`: Allows a voter to cast their vote if their phone number is not already used.
  - `show_candidates`: Displays the list of registered candidates.

- **Results**
  - `show_results`: Retrieves the current vote count for each candidate.
  - `display_results_chart`: Creates a pie chart of the results using `matplotlib`.
  - `export_results_csv` and `export_results_json`: Save results to CSV and JSON formats.

### GUI Structure

- **Main Menu**:
  - Buttons to access the Admin Panel, Voter Panel, Results Panel, Instructions, and Theme Toggle.
- **Admin Panel**:
  - Input field to add candidate names.
  - Buttons to reset the system or return to the main menu.
- **Voter Panel**:
  - Input field to enter phone numbers.
  - Listbox to display candidates for selection.
  - Buttons to cast votes or return to the main menu.
- **Results Panel**:
  - Password-protected interface to view results.
  - Buttons to export results to CSV/JSON or return to the main menu.

## Prerequisites

- Python 3.6 or higher
- Required libraries:
  - `tkinter` (standard with Python)
  - `matplotlib`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/EVM-Voting-System.git
   cd EVM-Voting-System
