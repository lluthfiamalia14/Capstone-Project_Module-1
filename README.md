# Capstone-Project_Module-1
# Employee Data System for HR in NGO

A simple employee management program built in Python to assist Human Resources (HR) teams in non-profit organizations (NGOs) or companies to manage and track employee data efficiently.

---

## Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Business Task](#business-task)
- [Key Stakeholders](#key-stakeholders)
- [How It Works](#how-it-works)
- [Data Source](#data-source)
- [Data Organization](#data-organization)
- [Key Features](#key-features)
- [Limitations](#limitations)

---

## Overview

This system is designed to help HR departments in NGOs or small businesses store, view, update, and manage employee records without relying on complex HR software. It's a beginner-friendly CRUD (Create, Read, Update, Delete) system implemented using only basic Python.

---

## Problem Statement

### Who has the problem?

- HR personnel in small NGOs or organizations without access to full-featured HR Information Systems (HRIS).

### What is the problem?

- Manually managing employee data in spreadsheets or documents can lead to:
  - Data entry errors.
  - Difficulty in tracking status like *leave*, *resignation*, or *promotion*.
  - Lack of integration and no search/update/delete automation.

---

## Business Task

Create a lightweight, text-based system that enables HR to:
- View all employees.
- Search employee by ID.
- Add new employee records.
- Update existing employee details.
- Delete employees no longer in the organization.

---

## Key Stakeholders

- **HR Department**: Main users who manage employee data.
- **Management/Leadership Team**: May request reports or updates from HR.
- **Employees**: Indirectly affected as their data must be accurately tracked.

---

## How It Works

Users interact via command-line interface:

1. HR logs in with username and password.
2. HR selects a menu option:
   - View all employee data.
   - Search by employee ID.
   - Add a new employee.
   - Update existing employee's information.
   - Delete an employee.
3. Data is stored in memory as Python lists.

---

## Data Source

### Where is your data located?

- All data is embedded in the code using Python lists.

### How is the data organized?

Each employee record is a combination of:
- First Name
- Last Name
- Position
- Department
- Salary
- Status (e.g., Active, Leave, Resign)
- Birthdate
- Auto-generated Employee ID (used as Primary Key)

### Primary Key

- `Employee ID` is uniquely generated using:
  - Department abbreviation
  - Initials
  - Birthdate (`YYYYMMDD`)

Example: `POL-MA-19980112`

### Required Columns

| Column        | Description                          |
|---------------|--------------------------------------|
| First Name    | Employee’s first name                |
| Last Name     | Employee’s last name                 |
| Position      | Job title or role                    |
| Department    | Division or team                     |
| Salary        | Monthly salary                       |
| Status        | Active / Leave / Resign              |
| Birthdate     | Format: YYYY-MM-DD                   |
| Employee ID   | Unique identifier (auto-generated)   |

---

## Key Features

- User login for security.
- View a formatted table of all employees.
- Search employee by ID.
- Add new employees with validation.
- Update employee data by field.
- Delete employee records with confirmation.
