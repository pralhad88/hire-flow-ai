# hire-flow-ai
An AI-driven module designed to help hiring teams efficiently filter thousands of resumes based on job-specific criteria using semantic search and intelligent ranking.

# Project Setup

## Project Requirements

1. Python 3.x
2. pip (Python package installer)

If Python is not installed, install Python 3 and pip on your system first.

---

## Step 1: Create Virtual Environment

1. Run the following command in your project's root directory:
```bash
python -m venv venv
```

> **Note:** If you get an error regarding `venv`, first install the virtual environment module:
> ```bash
> pip install virtualenv
> ```

2. Activate the virtual environment:

### **Windows**
```bash
venv\Scripts\activate
```

### **Mac / Linux**
```bash
source venv/bin/activate
```

> **Tip:** You should see `(venv)` appear at the beginning of your command prompt, indicating the virtual environment is active.

---

## Step 2: Install Required Python Dependencies

While the virtual environment is active, install all required packages:
```bash
pip install -r requirements.txt
```

> **Note:** Make sure you're in the project root directory where `requirements.txt` is located.

---

## Step 3: Configure Environment Variables

Create a `.env` file with your API keys:

### **Mac / Linux**
```bash
cp .example-env .env
```

### **Windows**
```bash
copy .example-env .env
```

After creating the `.env` file, open it and replace the placeholder values with your actual API keys.

---

## Step 4: Run the Application

Everything is set up! Now you can run the main file:
```bash
python main.py
```

Provide the query you want to use to select the best candidate result.

---

## 🎉 You're Done!

Your environment is now configured:

* ✅ All pip installs are isolated inside the `venv`
* ✅ No repeated installation needed
* ✅ Project dependencies are managed separately

---

## Troubleshooting

### Deactivating the Virtual Environment

When you're done working, deactivate the virtual environment:
```bash
deactivate
```

### Reactivating Later

Next time you work on the project, just reactivate the virtual environment using the activation command from Step 1.

### Common Issues

- **"python: command not found"** → Try `python3` instead of `python`
- **Permission errors on Mac/Linux** → Use `python3 -m venv venv` instead
- **Module not found errors** → Ensure your virtual environment is activated before running the application