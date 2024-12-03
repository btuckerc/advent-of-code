# Advent of Code Helper

A command-line tool to help manage Advent of Code solutions. Supports both Go (2024) and Python (previous years) solutions.

## Features

- 🎄 Automatic setup of daily problem structures
- 📥 Downloads problem descriptions and inputs
- 📝 Extracts example inputs from problem descriptions
- 🚀 Language-specific solution templates
- ✨ Answer submission handling
- 🔄 Session management

## Important Notes

- 🔒 Input files (`input.txt`) are unique per user and should not be shared
- ✅ Example inputs (`example.txt`) are from problem descriptions and can be shared
- 📝 Solution code can be shared after you've solved the problem
- 🔑 Keep your session cookie private

## Directory Structure

```
.
├── scripts/
│   └── aoc           # Main command-line tool
├── 2024/             # Solutions for 2024 (Go)
│   ├── go.mod
│   ├── README.md
│   └── day01/
│       ├── main.go
│       ├── README.md    # Problem description
│       ├── input.txt    # Your puzzle input
│       └── example.txt  # Example from problem
└── YYYY/             # Solutions for other years (Python)
    ├── requirements.txt
    ├── README.md
    └── dayNN/
        ├── solution.py
        ├── README.md
        ├── input.txt
        └── example.txt
```

## Setup

1. Clone the repository
2. Run initial setup:
   ```bash
   ./scripts/aoc init
   ```
3. Add your Advent of Code session cookie to `.env` or `.env.local`

## Usage

### Basic Commands

```bash
# Initialize the environment
./scripts/aoc init

# Set up a specific day
./scripts/aoc setup -d 1

# Set up all available days (during December 1-25)
./scripts/aoc setup

# Download input for a day
./scripts/aoc get -d 1

# Submit an answer
./scripts/aoc submit -d 1 "your_answer"
```

### Command Options

```
Commands:
  init                Initialize the environment
  setup [DAY]        Set up template for specific day or all days
  get DAY            Download input for specific day
  submit DAY ANSWER  Submit answer for specific day
  help              Show this help message

Options:
  -y, --year YEAR    Specify year (default: current year or previous if not December)
  -d, --day DAY      Specify day (default: current day)
  -p, --part PART    Specify part (1 or 2, default: 1)
  -h, --help         Show this help message
```

### Environment Variables

Create a `.env` or `.env.local` file with:
```bash
AOC_SESSION=your_session_cookie_here
```

To get your session cookie:
1. Go to https://adventofcode.com
2. Log in
3. Open Developer Tools (F12 or Command+Option+I)
4. Go to Application > Cookies
5. Copy the value of the 'session' cookie

## Features in Detail

### Setup Command
- Creates day directory with proper structure
- Downloads problem description as README.md
- Creates language-specific solution template
- Extracts example input if available
- Downloads puzzle input if session cookie is set
- During December 1-25, can set up all available days at once

### Solution Templates
- **Go (2024)**: Includes input reading, part1/part2 functions, and main
- **Python (Previous Years)**: Similar structure adapted for Python

### Input Handling
- Automatically downloads daily inputs with valid session
- Extracts example inputs from problem descriptions
- Supports fallback to example.txt when input.txt is missing

### Answer Submission
- Submits answers to Advent of Code
- Handles response parsing (correct/incorrect/timeout)
- Provides hints for wrong answers (too high/low)
- Automatically updates problem description with Part 2 when Part 1 is solved

## Development

The main script (`scripts/aoc`) is written in Bash and handles:
- Environment setup and configuration
- File and directory management
- HTTP requests to Advent of Code
- Template generation
- Answer submission

To modify templates or add features, edit the relevant sections in `scripts/aoc`.