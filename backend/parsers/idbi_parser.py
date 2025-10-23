import re

def parse(text: str):
    """IDBI Bank credit card statement parser with robust patterns"""
    t = text
    if 'idbi' not in t.lower():
        return None
    
    res = {'bank': 'IDBI Bank'}

    # Extract card last 4 digits
    patterns = [
        r'card\s*(?:number|no\.?)?\s*[:]*\s*(?:xxxx|x{4}|\*{4})[x\s\-*]*(?:xxxx|x{4}|\*{4})[x\s\-*]*(?:xxxx|x{4}|\*{4})[x\s\-*]*(\d{4})',
        r'(\d{4})\s*(?:\)|\])',
        r'(?:ending|ends)\s*(?:with|in)?\s*(\d{4})',
    ]
    for pattern in patterns:
        m = re.search(pattern, t, re.IGNORECASE)
        if m:
            res['card_last_4'] = m.group(1)
            break

    # Extract billing cycle
    patterns = [
        r'billing\s*cycle[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4}\s*(?:to|-|–)\s*[\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
        r'statement\s*period[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4}\s*(?:to|-|–)\s*[\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
        r'billing\s*period[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4}\s*(?:to|-|–)\s*[\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
    ]
    for pattern in patterns:
        m = re.search(pattern, t, re.IGNORECASE)
        if m:
            res['billing_cycle'] = m.group(1).strip()
            break

    # Extract due date
    patterns = [
        r'payment\s*due\s*date[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
        r'due\s*date[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
        r'pay\s*by[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
    ]
    for pattern in patterns:
        m = re.search(pattern, t, re.IGNORECASE)
        if m:
            res['payment_due_date'] = m.group(1).strip()
            break

    # Extract total outstanding/due
    patterns = [
        r'total\s*outstanding[:\s]*(?:rs\.?|₹)?\s*([\d,]+\.?\d*)',
        r'total\s*amount\s*due[:\s]*(?:rs\.?|₹)?\s*([\d,]+\.?\d*)',
        r'amount\s*due[:\s]*(?:rs\.?|₹)?\s*([\d,]+\.?\d*)',
        r'outstanding\s*balance[:\s]*(?:rs\.?|₹)?\s*([\d,]+\.?\d*)',
    ]
    for pattern in patterns:
        m = re.search(pattern, t, re.IGNORECASE)
        if m:
            res['total_due'] = m.group(1).strip()
            break

    return res
