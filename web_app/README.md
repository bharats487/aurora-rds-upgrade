# AWS RDS Demo Web Application

This is a Flask web application that connects to an AWS Aurora MySQL database.

## Prerequisites

- Python 3.8+
- AWS CLI configured with appropriate credentials
- Terraform applied to create the RDS cluster

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Initialize the database:
```bash
python init_db.py
```

3. Run the application:
```bash
python -m flask run
```

4. Open your browser and navigate to `http://localhost:5000`

## Features

- Automatic AWS RDS endpoint discovery
- Database connection testing
- Basic CRUD operations (modify models as needed)
- Bootstrap-based responsive UI

## Security Note

- The database password is currently hardcoded. In production, use AWS Secrets Manager or environment variables.
- Ensure proper AWS IAM permissions are configured for RDS access.
