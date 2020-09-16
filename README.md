# Kronecker Graph Generator

This repository contains a Kronecker Graph Generator.
The Kronecker model is a model for graph generation that obeys patterns observed in real-world networks (e.g., heavy-tail distribution, power-law).
This model is a simple implementation that uses a given Kronecker initiator matrix and iteratively (or recursively) computes the k-th Kronecker product.

## Prerequisite (Dependencies)

I used Scipy and Numpy for implementation.

```bash
pip install scipy==1.5.0
pip install numpy==1.18.1
```

## How to use
After cloning the code to your repository, generate Kronecker graph with the following command:
```bash
main.py [-h] [-f FILENAME] [-k K] [-o OUTPUTNAME]
```
