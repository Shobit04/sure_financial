import re

def parse(text: str):
    """ICICI Bank credit card statement parser with robust patterns"""
    t = text
    if 'icici' not in t.lower():
        return None
    
    res = {'bank': 'ICICI Bank'}

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

    # Extract billing period
    patterns = [
        r'billing\s*period[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4}\s*(?:to|-|–)\s*[\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
        r'statement\s*period[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4}\s*(?:to|-|–)\s*[\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
        r'from\s*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})\s*(?:to|-|–)\s*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
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
        r'payment\s*due\s*date[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
        r'due\s*date[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
        r'pay\s*by[:\s]*([\d]{1,2}[\/\-\s][\w]{3,9}[\/\-\s][\d]{2,4})',
    ]
    for pattern in patterns:
        m = re.search(pattern, t, re.IGNORECASE)
        if m:
            res['payment_due_date'] = m.group(1).strip()
            break

    # Extract amount due
    patterns = [
        r'(?:total\s*)?amount\s*due[:\s]*(?:rs\.?|₹)?\s*([\d,]+\.?\d*)',
        r'total\s*due[:\s]*(?:rs\.?|₹)?\s*([\d,]+\.?\d*)',
        r'payment\s*amount[:\s]*(?:rs\.?|₹)?\s*([\d,]+\.?\d*)',
    ]
    for pattern in patterns:
        m = re.search(pattern, t, re.IGNORECASE)
        if m:
            res['total_due'] = m.group(1).strip()
            break

    return res
