# Mini-OS Simulator 🚀
<img width="720" height="913" alt="cpu_sch_fcfs" src="https://github.com/user-attachments/assets/bd93814c-c65f-4c52-9819-ff71583c1e9e" />

Mini-OS is a lightweight, modular operating system simulator developed in Python. It provides a terminal-based environment to visualize and analyze CPU scheduling algorithms and resource management.

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Overview

Mini-OS is designed as an educational tool to bridge the gap between theoretical operating system concepts and practical implementation. By providing a CLI-based "Kernel," it allows users to execute, visualize, and calculate performance metrics for various OS algorithms.

---

## Features

- **Kernel-like CLI:** Experience a shell-like environment with commands such as `ls`, `cd`, `run`, and `help`.
- **Modular Design:** Algorithms are separated by domain (CPU Scheduling, Memory Management, etc.).
- **Process Visualization:** Clear and intuitive Gantt chart generation for scheduling analysis.
- **Performance Metrics:** Automatic calculation of:
  - Average Waiting Time (AWT)
  - Average Turnaround Time (ATT)
  - CPU Utilization
- **No Dependencies:** Built with core Python modules, ensuring high portability.

---

## 📂 Project Structure

```text
Mini-OS/
├── main.py              # Main Kernel / Command Executor
├── cpu_sch/             # CPU Scheduling algorithms
│   ├── priority.py
│   ├── fcfs.py
│   └── utils.py         # CPU scheduling visualization helpers
├── disk_sch/            # Disk scheduling module
└── page_replacement/    # Memory management module
```

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Running the Simulator

#### Clone the Repository

```bash
git clone https://github.com/fatiimahoseini/mini-os.git
```

#### Execute the Kernel

```bash
python main.py
```

### Example Commands

```bash
ls
```

Explore available filesystem modules.

```bash
cd cpu_sch
```

Navigate into the CPU scheduling directory.

```bash
run priority.py
```

Execute the Priority Scheduling algorithm.

---

## 📝 Technical Highlights

### Dynamic Execution

Uses Python's `exec()` function to execute algorithm scripts within an isolated environment.

### Standardized Visualization

Every module includes a dedicated `utils.py` file to ensure consistent output formatting and visualization across different algorithms.

---

## 🤝 Contributing

Contributions are welcome!

If you have suggestions for new scheduling algorithms, additional operating system modules, or improvements to the shell environment, feel free to fork this repository and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

Developed for educational purposes.
