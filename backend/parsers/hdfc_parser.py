import re

def parse(text: str):
    """HDFC Bank credit card statement parser with robust patterns"""
    t = text
    res = {}
    
    # Check if this is an HDFC statement
    if 'hdfc' not in t.lower():
        return None

    res['bank'] = 'HDFC Bank'

    # Extract card last 4 digits - multiple patterns
    patterns = [
        r'card\s*(?:number|no\.?)?\s*[:]*\s*(?:xxxx|x{4}|\*{4})[x\s\-*]*(?:xxxx|x{4}|\*{4})[x\s\-*]*(?:xxxx|x{4}|\*{4})[x\s\-*]*(\d{4})',
        r'(?:ending|ends)\s*(?:with|in)?\s*(\d{4})',
        r'(\d{4})\s*(?:\)|\])\s*card',
    ]
    for pattern in patterns:
        m = re.search(pattern, t, re.IGNORECASE)
        if m:
            res['card_last_4'] = m.group(1)
            break

    # Extract billing cycle/period
    patterns = [
        r'billing\s*period[:\s]*([\d]{1,2}\s*[\w]{3,9},?\s*[\d]{2,4}\s*(?:to|-|–)\s*[\d]{1,2}\s*[\w]{3,9},?\s*[\d]{2,4})',
        r'billing\s*period[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4}\s*(?:to|-|–)\s*[\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
        r'statement\s*period[:\s]*([\d]{1,2}\s*[\w]{3,9},?\s*[\d]{2,4}\s*(?:to|-|–)\s*[\d]{1,2}\s*[\w]{3,9},?\s*[\d]{2,4})',
        r'from\s*([\d]{1,2}\s*[\w]{3,9},?\s*[\d]{2,4})\s*(?:to|-|–)\s*([\d]{1,2}\s*[\w]{3,9},?\s*[\d]{2,4})',
        r'([\d]{1,2}\s+[\w]{3,9},?\s+[\d]{4})\s*-\s*([\d]{1,2}\s+[\w]{3,9},?\s+[\d]{4})',
    ]
    for pattern in patterns:
        m = re.search(pattern, t, re.IGNORECASE)
        if m:
            if m.lastindex == 2:
                res['billing_cycle'] = f"{m.group(1)} to {m.group(2)}"
            else:
                res['billing_cycle'] = m.group(1).strip()
            break

    # Extract payment due date
    patterns = [
        r'[₹C][\d,]+\.?\d*\s+(\d{1,2}\s+\w{3,9},?\s+\d{2,4})',  # Amount (₹ or C) followed by date (table format)
        r'due\s*date[:\s\n]*(\d{1,2}\s+\w{3,9},?\s+\d{2,4})',  # DUE DATE label
        r'pay(?:ment)?\s*by[:\s]*(\d{1,2}[-/\s]\w{3,9}[-/\s,]*\d{2,4})',
        r'payment\s*date[:\s]*(\d{1,2}[-/\s]\w{3,9}[-/\s,]*\d{2,4})',
        r'last\s*date\s*of\s*payment[:\s]*(\d{1,2}[-/\s]\w{3,9}[-/\s,]*\d{2,4})',
    ]
    for pattern in patterns:
        m = re.search(pattern, t, re.IGNORECASE)
        if m:
            res['payment_due_date'] = m.group(1).strip()
            break

    # Extract total amount due
    patterns = [
        # Table format: find TOTAL AMOUNT DUE header, then find ₹ or C amount after it (in next line/column)
        r'total\s*amount\s*due[^\n]*\n[^\n]*[₹C]([\d,]+\.?\d*)\s*$',  # Multi-line table format
        r'total\s*amount\s*due[^\n]*[₹C]([\d,]+\.?\d*)\s*(?:\n|$)',  # Amount on same or next line
        # Look for minimum due before due date
        r'minimum\s*due[:\s]*[₹C]?([\d,]+\.?\d*)\s+due\s*date',
        r'minimum\s*due\s*due\s*date[:\s\n]*[₹C]?([\d,]+\.?\d*)',
        r'minimum\s*due[:\s\n]*[₹C]?([\d,]+\.?\d*)\s+\d{1,2}\s+\w{3}',  # minimum due followed by date
        r'total\s*due[:\s\n]*[₹C]?([\d,]+\.?\d*)',
        r'amount\s*payable[:\s\n]*[₹C]?([\d,]+\.?\d*)',
    ]
    for pattern in patterns:
        m = re.search(pattern, t, re.IGNORECASE | re.MULTILINE)
        if m:
            res['total_due'] = m.group(1).strip()
            break

    return res
