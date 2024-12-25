# Process Scheduling Visualizer

## Description
This project visualizes CPU scheduling algorithms in an operating system. It supports three algorithms:
- **First-Come-First-Serve (FCFS)**
- **Shortest Job First (SJF)**
- **Round Robin (RR)**

Users can input processes with their arrival and burst times and see the resulting scheduling, including Gantt charts, waiting times, and turnaround times.

## Features
- **Visualize Process Scheduling Algorithms**: See how each algorithm schedules processes.
- **Real-Time Updates**: Update inputs and instantly view results.
- **Interactive Interface**: Simple web interface using Flask.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/process-scheduling-visualizer.git
    ```

2. Navigate to the project directory:
    ```bash
    cd process-scheduling-visualizer
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    python app.py
    ```

5. Open your browser and go to `http://127.0.0.1:5000/`.

## Requirements
- Python 3.x
- Flask

## Usage
- Select the number of processes and their burst times.
- Choose the scheduling algorithm and input parameters.
- Visualize the Gantt chart and performance metrics.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
