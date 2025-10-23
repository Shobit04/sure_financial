import re

def parse(text: str):
    """Axis Bank credit card statement parser"""
    t = text
    res = {}
    
    # Check if this is an Axis statement
    if 'axis' not in t.lower():
        return None

    res['bank'] = 'Axis Bank'

    # Extract card last 4 digits - multiple patterns
    patterns = [
        r'card\s*(?:number|no\.?)?\s*[:]*\s*(?:xxxx|x{4}|\*{4})[x\s\-*]*(?:xxxx|x{4}|\*{4})[x\s\-*]*(?:xxxx|x{4}|\*{4})[x\s\-*]*(\d{4})',
        r'(\d{6})\*+(\d{4})',  # Format: 539494******6869
        r'(?:ending|ends)\s*(?:with|in)?\s*(\d{4})',
    ]
    for pattern in patterns:
        m = re.search(pattern, t, re.IGNORECASE)
        if m:
            # Handle the 6-digit prefix format
            if m.lastindex == 2:
                res['card_last_4'] = m.group(2)
            else:
                res['card_last_4'] = m.group(1)
            break

    # Prefer parsing from the PAYMENT SUMMARY block to avoid stray matches
    summary_block = re.search(r'payment\s+summary\s*\n([^\n]+)\n([^\n]+)', t, re.IGNORECASE)
    values_line = None
    if summary_block:
        headers_line, values_line = summary_block.group(1), summary_block.group(2)
        # Try to extract billing period (date range) from the values line
        m = re.search(r'(\d{1,2}/\d{2}/\d{4})\s*[-–]\s*(\d{1,2}/\d{2}/\d{4})', values_line)
        if m:
            res['billing_cycle'] = f"{m.group(1)} to {m.group(2)}"
    
    # Fallback patterns if not found via summary block
    if not res.get('billing_cycle'):
        patterns = [
            r'statement\s*period[^\n]*\n[^\n]*(\d{1,2}[\/\-]\d{2}[\/\-]\d{4})\s*[-–]\s*(\d{1,2}[\/\-]\d{2}[\/\-]\d{4})',
            r'billing\s*period[:\s]*(\d{1,2}[\/\-]\d{2}[\/\-]\d{4})\s*[-–]\s*(\d{1,2}[\/\-]\d{2}[\/\-]\d{4})',
            r'from\s*(\d{1,2}[\/\-]\d{2}[\/\-]\d{4})\s*(?:to|-|–)\s*(\d{1,2}[\/\-]\d{2}[\/\-]\d{4})',
        ]
        for pattern in patterns:
            m = re.search(pattern, t, re.IGNORECASE)
            if m:
                res['billing_cycle'] = f"{m.group(1)} to {m.group(2)}"
                break

    # Extract payment due date - prefer from summary values line (date after the range)
    if values_line and not res.get('payment_due_date'):
        m = re.search(r'\d{1,2}/\d{2}/\d{4}\s*[-–]\s*\d{1,2}/\d{2}/\d{4}\s+(\d{1,2}/\d{2}/\d{4})', values_line)
        if m:
            res['payment_due_date'] = m.group(1)
    if not res.get('payment_due_date'):
        patterns = [
            r'payment\s*due\s*date[^\n]*\n[^\n]*(\d{1,2}[\/\-]\d{2}[\/\-]\d{4})',
            r'due\s*date[:\s]*(\d{1,2}[\/\-]\d{2}[\/\-]\d{4})',
            r'pay\s*by[:\s]*(\d{1,2}[\/\-]\d{2}[\/\-]\d{4})',
        ]
        for pattern in patterns:
            m = re.search(pattern, t, re.IGNORECASE)
            if m:
                res['payment_due_date'] = m.group(1).strip()
                break

    # Extract total payment due - prefer first currency in summary values line
    if values_line and not res.get('total_due'):
        m = re.search(r'([₹C]?[\d,]+\.\d{2})', values_line)
        if m:
            res['total_due'] = m.group(1)
    if not res.get('total_due'):
        patterns = [
            r'total\s*payment\s*due[^\n]*\n\s*([₹C]?[\d,]+\.?\d*)\s*(?:dr|debit)?',
            r'total\s*amount\s*due[:\s]*([₹C]?[\d,]+\.?\d*)',
            r'total\s*due[:\s]*([₹C]?[\d,]+\.?\d*)',
            r'amount\s*payable[:\s]*([₹C]?[\d,]+\.?\d*)',
        ]
        for pattern in patterns:
            m = re.search(pattern, t, re.IGNORECASE)
            if m:
                res['total_due'] = m.group(1).strip()
                break

    return res
