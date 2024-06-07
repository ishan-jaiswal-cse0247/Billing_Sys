import json
import pdfkit
from jinja2 import Environment, FileSystemLoader
from num2words import num2words
import os
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_input(data: Dict[str, Any]) -> bool:
    required_fields = [
        'company_logo', 'seller_details', 'billing_details', 'shipping_details', 
        'place_of_supply', 'place_of_delivery', 'order_no', 'order_date', 
        'invoice_no', 'invoice_date', 'reverse_charge', 'items', 'seller_name', 'signature'
    ]
    for field in required_fields:
        if field not in data:
            logging.error(f"Missing required field: {field}")
            return False
    
    for item in data['items']:
        item_fields = ['description', 'unit_price', 'quantity', 'discount', 'tax_rate']
        for field in item_fields:
            if field not in item:
                logging.error(f"Missing required field in item: {field}")
                return False
    return True

def compute_values(data: Dict[str, Any]) -> Dict[str, Any]:
    for item in data['items']:
        item['net_amount'] = item['unit_price'] * item['quantity'] - item['discount']
        if data['place_of_supply'] == data['place_of_delivery']:
            item['cgst'] = item['net_amount'] * 0.09
            item['sgst'] = item['net_amount'] * 0.09
            item['igst'] = 0
        else:
            item['cgst'] = 0
            item['sgst'] = 0
            item['igst'] = item['net_amount'] * 0.18
        item['total_amount'] = item['net_amount'] + item['cgst'] + item['sgst'] + item['igst']

    data['total_amount'] = sum(item['total_amount'] for item in data['items'])
    data['amount_in_words'] = num2words(data['total_amount'], to='currency', lang='en_IN')
    return data

def generate_invoice(data: Dict[str, Any]) -> None:
    if not validate_input(data):
        logging.error("Invalid input data. Invoice generation aborted.")
        return
    
    data = compute_values(data)
    
    # Load template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('invoice_template.html')
    
    # Render HTML
    html_out = template.render(data)
    
    # Generate PDF
    output_pdf = f"invoices/{data['invoice_no']}.pdf"
    pdfkit.from_string(html_out, output_pdf)
    logging.info(f"Invoice generated successfully: {output_pdf}")

if __name__ == "__main__":
    # Example input data
    with open('example_input.json') as f:
        data = json.load(f)
    generate_invoice(data)
