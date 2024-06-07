# Invoice Generator

## Overview

This project generates a PDF invoice based on the given input parameters. The invoice format matches a specified structure and includes placeholders for company logo, signature, and other details.

## Requirements

- Python 3.6+
- `jinja2` for HTML templating
- `pdfkit` for HTML to PDF conversion
- `num2words` for converting numbers to words

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd invoice_generator
   ```
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Install `wkhtmltopdf`:
   - On Ubuntu:
     ```bash
     sudo apt-get install wkhtmltopdf
     ```
   - On macOS:
     ```bash
     brew install wkhtmltopdf
     ```

## Usage

1. Prepare your input data in a JSON file (e.g., `example_input.json`).
2. Create a directory named `invoices` to store generated invoices:
   ```bash
   mkdir invoices
   ```
3. Run the invoice generator script:
   ```bash
   python invoice_generator.py
   ```
4. The generated PDF invoice will be saved in the `invoices` directory with the invoice number as the file name.

## Example Input

Refer to `example_input.json` in the project directory for an example of input data format.

## Notes

- Ensure paths to the company logo and signature images are correct in the input JSON.
- The script validates input data and handles errors gracefully.
- Designed for performance and scalability to handle a large volume of orders.

## License

This project is licensed under the MIT License.
