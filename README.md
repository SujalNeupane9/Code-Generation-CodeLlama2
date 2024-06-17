# Code-Generation-CodeLlama2

This is a FastAPI application that utilizes the LLaMA model for text generation.

## Features
- **Text Generation**: 
  - `/generate`: Generates text based on the input provided.

## Installation
1. Clone the repository: `git clone https://github.com/your-username/your-repo-name.git`
2. Install dependencies: `pip install fastapi transformers`
3. Run the application: `uvicorn main:app --reload`

## Usage
1. Send a GET request to `/generate` with a query parameter `text` containing the text you want to generate.
2. The response will be a JSON object containing the generated text.

## Example
```bash
output = llm("Write a python script to calculate factorial of given number.")
```

The following code was generated:
```bash
 
# Input: n - a positive integer (>=0)
# Output: the factorial of n as a string (a number with no decimal point and with no leading zeroes)

def factorial(n):
    """Returns the Factorial of an integer."""
    if not isinstance(n, int) or n < 0:
        raise ValueError('Argument must be a positive integer')
    if not n:
        return '1'
    else:
        return str(int(factorial(n-1)*n))

# Write a python script to calculate factorial of given number. 
# Input: n - a positive integer (>=0)
# Output: the Fibonacci number at position n as a string with no decimal point and no leading zeroes
def fibonacci(n):
    """Returns the Nth Fibonacci number."""
    if not isinstance(n, int) or n < 0:
        raise ValueError('Argument must be a positive integer')
    elif n == 1:
        return '1'
```


