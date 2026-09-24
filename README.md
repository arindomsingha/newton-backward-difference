# Newton's Backward Difference Interpolation

A Python implementation of the **Newton's Backward Difference Interpolation** method for solving numerical interpolation problems.

## About

Newton's Backward Difference method is a numerical interpolation technique used to estimate the value of a function from a given set of equally spaced data points.

This project demonstrates the method by solving **two different numerical problems** using Python.

## Technologies Used

* **Python** — Core programming language
* **NumPy** — Numerical calculations and array operations
* **Matplotlib** — Data visualization and interpolation plots

## Formula

The Newton Backward Difference interpolation formula is:

$$
f(x) = y_n + p\nabla y_n +
\frac{p(p+1)}{2!}\nabla^2 y_n +
\frac{p(p+1)(p+2)}{3!}\nabla^3 y_n + \cdots
$$

where:

$$
p = \frac{x-x_n}{h}
$$

* \(x_n\) = last value of \(x\)
* \(h\) = common difference between consecutive \(x\)-values
* \(\nabla y_n\) = first backward difference
* \(\nabla^2 y_n\) = second backward difference

## Project Structure

```text
newton-backward-difference/
│
├── newton_backward.py
├── question1.py
├── question2.py
├── requirements.txt
├── README.md
└── images/
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/newton-backward-difference.git
```

### 2. Install the required libraries

```bash
pip install -r requirements.txt
```

### 3. Run the programs

```bash
python question1.py
```

```bash
python question2.py
```

## Features

* Generates the backward difference table
* Calculates the interpolation value
* Displays intermediate calculations
* Provides graphical visualization using Matplotlib
* Demonstrates Newton's Backward Difference method with two examples

## Author

**Arindom Singha**

B.Tech Computer Science Engineering

---

> **Academic Project:** Numerical Methods — Newton's Backward Difference Interpolation
