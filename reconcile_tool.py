import csv
import io

# Simulate messy sales export data (e.g., from Shopify or a POS)
sales_csv = """order_id,customer_name,amount,status
ORD-001,Alice Smith,150.50,Completed
ORD-002,Bob Jones,99.00,Completed
ORD-003,Charlie Brown,250.00,Completed
ORD-004,Diana Prince,45.00,Refunded
ORD-005,Evan Wright,120.00,Completed
"""

# Simulate messy accounting export data (e.g., QuickBooks/Excel)
# Notice: ORD-003 has a typo in amount, ORD-005 is missing entirely, and INV-999 is an extra entry.
accounting_csv = """reference_id,client_name,recorded_amount,payment_status
ORD-001,Alice Smith,150.50,Paid
ORD-002,Bob Jones,99.00,Paid
ORD-003,Charlie Brown,240.00,Paid
ORD-004,Diana Prince,45.00,Refunded
INV-999,Unknown Entity,500.00,Paid
"""

def parse_csv(data_str):
    reader = csv.DictReader(io.StringIO(data_str.strip()))
    return list(reader)

def run_reconciliation():
    sales = {row['order_id']: row for row in parse_csv(sales_csv)}
    accounting = {row['reference_id']: row for row in parse_csv(accounting_csv)}

    discrepancies = []
    matched = 0

    sales_keys = set(sales.keys())
    accounting_keys = set(accounting.keys())

    # Check for missing in accounting or amount mismatches
    for oid, s_row in sales.items():
        if oid not in accounting:
            discrepancies.append({
                'id': oid,
                'issue': 'Missing in Accounting system',
                'sales_data': s_row,
                'accounting_data': None
            })
        else:
            acc_row = accounting[oid]
            s_amount = float(s_row['amount'])
            acc_amount = float(acc_row['recorded_amount'])
            if s_amount != acc_amount:
                discrepancies.append({
                    'id': oid,
                    'issue': f'Amount mismatch (Sales: {s_amount} vs Acc: {acc_amount})',
                    'sales_data': s_row,
                    'accounting_data': acc_row
                })
            else:
                matched += 1

    # Check for extra items in accounting
    for aid in accounting_keys - sales_keys:
        discrepancies.append({
            'id': aid,
            'issue': 'Extra record in Accounting (not found in Sales)',
            'sales_data': None,
            'accounting_data': accounting[aid]
        })

    print("=== RECONCILIATION AUDIT REPORT ===")
    print(f"Total Sales Records: {len(sales)}")
    print(f"Total Accounting Records: {len(accounting)}")
    print(f"Perfect Matches: {matched}")
    print(f"Discrepancies Flagged: {len(discrepancies)}\n")

    print("--- DETAILED DISCREPANCIES ---")
    for d in discrepancies:
        print(f"ID: {d['id']} | Issue: {d['issue']}")

if __name__ == '__main__':
    run_reconciliation()
