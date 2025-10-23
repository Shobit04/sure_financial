import re
from typing import Dict
from parsers import hdfc_parser, icici_parser, idbi_parser, sbi_parser, kotak_parser, axis_parser
from utils.data_formatter import clean_amount, parse_date


class UniversalParser:
    def __init__(self):
        # Keep a canonical list but we'll dynamically prioritize based on detected bank
        self.parsers = [hdfc_parser, icici_parser, idbi_parser, sbi_parser, kotak_parser, axis_parser]

    def detect_bank(self, text: str) -> str:
        """Detect bank from text - works with any bank statement"""
        mapping = {
            'HDFC Bank': ['hdfc bank', 'hdfc'],
            'ICICI Bank': ['icici bank', 'icici'],
            'IDBI Bank': ['idbi bank', 'idbi', 'industrial development bank'],
            'Axis Bank': ['axis bank', 'axis'],  # Check Axis before SBI
            'SBI Card': ['sbi card', 'state bank of india card'],  # More specific
            'Kotak Mahindra Bank': ['kotak mahindra', 'kotak'],
            'Yes Bank': ['yes bank'],
            'IndusInd Bank': ['indusind bank', 'indusind'],
            'Standard Chartered': ['standard chartered'],
            'Citi Bank': ['citibank', 'citi'],
            'HSBC': ['hsbc'],
            'American Express': ['american express', 'amex'],
        }
        t = text.lower()
        for name, kws in mapping.items():
            for k in kws:
                if k in t:
                    return name
        return 'Unknown Bank'

    def generic_extract(self, text: str) -> Dict:
        """Generic extraction for any bank statement - fallback method"""
        result = {}
        
        # Extract card number (last 4 digits)
        patterns = [
            r'(?:card\s*(?:number|no\.?|#)?[:\s]*.*?)(\d{4})(?:\s|$|\))',
            r'xxxx[x\s-]*xxxx[x\s-]*xxxx[x\s-]*(\d{4})',
            r'\*\*\*\*[*\s-]*\*\*\*\*[*\s-]*\*\*\*\*[*\s-]*(\d{4})',
            r'(?:ending|ends)\s*(?:with|in)?\s*(\d{4})',
        ]
        for pattern in patterns:
            m = re.search(pattern, text, re.IGNORECASE)
            if m:
                result['card_last_4'] = m.group(1)
                break
        
        # Extract billing cycle / statement period
        patterns = [
            r'(?:billing|statement)\s*(?:period|cycle|date)[:\s]*([\d]{1,2}\s*[\w]{3,9},?\s*[\d]{2,4}\s*(?:to|-|–)\s*[\d]{1,2}\s*[\w]{3,9},?\s*[\d]{2,4})',
            r'(?:billing|statement)\s*(?:period|cycle|date)[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4}\s*(?:to|-|–)\s*[\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
            r'(?:from|period)[:\s]*([\d]{1,2}\s*[\w]{3,9},?\s*[\d]{2,4}\s*(?:to|-|–)\s*[\d]{1,2}\s*[\w]{3,9},?\s*[\d]{2,4})',
            r'(?:from|period)[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4}\s*(?:to|-|–)\s*[\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
            r'([\d]{1,2}\s+[\w]{3,9},?\s+[\d]{4})\s*-\s*([\d]{1,2}\s+[\w]{3,9},?\s+[\d]{4})',
        ]
        for pattern in patterns:
            m = re.search(pattern, text, re.IGNORECASE)
            if m:
                if m.lastindex == 2:
                    result['billing_cycle'] = f"{m.group(1)} to {m.group(2)}"
                else:
                    result['billing_cycle'] = m.group(1).strip()
                break
        
        # Extract payment due date
        patterns = [
            r'(?:payment\s*)?due\s*(?:date|by|on)[:\s]*([\d]{1,2}\s*[\w]{3,9},?\s*[\d]{2,4})',
            r'(?:payment\s*)?due\s*(?:date|by|on)[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
            r'(?:pay\s*by|payment\s*by)[:\s]*([\d]{1,2}\s*[\w]{3,9},?\s*[\d]{2,4})',
            r'(?:pay\s*by|payment\s*by)[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
            r'(?:must\s*be\s*paid\s*by)[:\s]*([\d]{1,2}\s*[\w]{3,9},?\s*[\d]{2,4})',
            r'(?:must\s*be\s*paid\s*by)[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
        ]
        for pattern in patterns:
            m = re.search(pattern, text, re.IGNORECASE)
            if m:
                result['payment_due_date'] = m.group(1).strip()
                break
        
        # Extract total amount due
        patterns = [
            r'(?:total\s*)?(?:amount\s*)?due[:\s]*[₹rs\.]*\s*([\d,]+\.?\d*)',
            r'(?:total\s*)?outstanding[:\s]*[₹rs\.]*\s*([\d,]+\.?\d*)',
            r'(?:minimum\s*)?(?:amount\s*)?(?:to\s*)?pay[:\s]*[₹rs\.]*\s*([\d,]+\.?\d*)',
            r'(?:total\s*)?balance[:\s]*[₹rs\.]*\s*([\d,]+\.?\d*)',
            r'(?:amount\s*)?payable[:\s]*[₹rs\.]*\s*([\d,]+\.?\d*)',
        ]
        for pattern in patterns:
            m = re.search(pattern, text, re.IGNORECASE)
            if m:
                result['total_due'] = m.group(1).strip()
                break
        
        return result

    def parse_text(self, text: str) -> Dict:
        """Parse any credit card statement - universal parser"""
        bank = self.detect_bank(text)
        result = {
            'bank': bank,
            'card_last_4': None,
            'billing_cycle': None,
            'payment_due_date': None,
            'total_due': None,
            'confidence': 0.0,
            'notes': []
        }

        # Build a prioritized parser list: detected bank parser first (if known), then the rest
        parser_map = {
            'HDFC Bank': hdfc_parser,
            'ICICI Bank': icici_parser,
            'IDBI Bank': idbi_parser,
            'SBI Card': sbi_parser,
            'Kotak Mahindra Bank': kotak_parser,
            'Axis Bank': axis_parser,
        }
        prioritized_parsers = []
        if bank in parser_map:
            prioritized_parsers.append(parser_map[bank])
        # Append remaining parsers, avoiding duplicates
        for p in self.parsers:
            if p not in prioritized_parsers:
                prioritized_parsers.append(p)

        # Try bank-specific parser(s) in priority order first
        parser_found = False
        for p in prioritized_parsers:
            try:
                r = p.parse(text)
                if r and any(r.values()):  # Check if parser returned any data
                    result.update(r)
                    parser_found = True
                    # If parser provided bank override (e.g., in case detect_bank was wrong), set it
                    if r.get('bank'):
                        result['bank'] = r['bank']
                    # Note which specific parser we used
                    used_name = result.get('bank', 'specific')
                    result['notes'].append(f'Used {used_name} parser')
                    break
            except Exception as e:
                result['notes'].append(f'Parser error: {str(e)[:50]}')
                continue

        # If no bank-specific parser worked, use generic extraction
        if not parser_found or result['confidence'] == 0:
            generic_data = self.generic_extract(text)
            # Only update fields that are still None
            for key, value in generic_data.items():
                if not result.get(key) and value:
                    result[key] = value
            result['notes'].append('Used generic universal parser')

        # Clean and format data
        if result.get('total_due'):
            result['total_due'] = clean_amount(result['total_due'])
        if result.get('payment_due_date'):
            result['payment_due_date'] = parse_date(result['payment_due_date'])

        # Calculate confidence score
        fields = ['bank', 'card_last_4', 'billing_cycle', 'payment_due_date', 'total_due']
        filled = sum(1 for k in fields if result.get(k) and result[k] != 'Unknown Bank')
        result['confidence'] = round(filled / len(fields), 2)

        # Add contextual notes
        if result['confidence'] < 0.5:
            result['notes'].append('Low confidence - manual verification strongly recommended')
        elif result['confidence'] < 1.0:
            result['notes'].append('Some fields missing - please verify extracted data')
        else:
            result['notes'].append('All fields extracted successfully')

        # Generate summary
        try:
            result['summary'] = self.summarize(result)
        except Exception as e:
            result['summary'] = f'Unable to generate summary: {str(e)}'

        return result

    def summarize(self, data: Dict) -> str:
        """Generate human-readable summary"""
        bank = data.get('bank', 'Unknown bank')
        total = data.get('total_due', 'unknown amount')
        due = data.get('payment_due_date', 'unknown date')
        card = data.get('card_last_4', 'XXXX')
        
        if total != 'unknown amount' and due != 'unknown date':
            summary = f"Your {bank} credit card (ending {card}) has a total amount due of {total}, payable by {due}."
        elif total != 'unknown amount':
            summary = f"Your {bank} credit card (ending {card}) has a total amount due of {total}."
        elif due != 'unknown date':
            summary = f"Your {bank} credit card (ending {card}) payment is due by {due}."
        else:
            summary = f"Credit card statement for {bank} (ending {card}) - some details could not be extracted."
        
        return summary
