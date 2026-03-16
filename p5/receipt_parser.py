import re
import json


def normalize_number(s):
    s = s.replace(" ", "").replace(",", ".")
    return float(s)


def extract_datetime(text):
    match = re.search(r"Time:\s*(\d{2}\.\d{2}\.\d{ss4})\s+(\d{2}:\d{2}:\d{2})", text)
    if match:
        return match.group(1), match.group(2)
    return None, None


def extract_payment_method(text):
    match = re.search(r"(Bank card|Cash|Card)", text, re.IGNORECASE)
    if match:
        return match.group(1)
    return None


def extract_total(text):
    match = re.search(r"TOTAL:\s*\n?\s*([\d ]+,\d{2})", text)
    if match:
        return normalize_number(match.group(1))
    return None


def extract_items(text):
    pattern = re.compile(
        r"\d+\.\s*\n"
        r"(.+?)\n"
        r"([\d,]+)\s*x\s*([\d ]+,\d{2})\n"
        r"([\d ]+,\d{2})",
        re.MULTILINE
    )

    items = []

    for match in pattern.finditer(text):
        name = match.group(1).strip()
        quantity = float(match.group(2).replace(",", "."))
        unit_price = normalize_number(match.group(3))
        line_total = normalize_number(match.group(4))

        items.append({
            "name": name,
            "quantity": quantity,
            "unit_price": unit_price,
            "line_total": line_total
        })

    return items


def extract_all_prices(items, total):
    prices = []

    for item in items:
        prices.append(item["unit_price"])
        prices.append(item["line_total"])

    if total is not None:
        prices.append(total)

    return prices


def main():
    with open("raw.txt", "r", encoding="utf-8") as file:
        text = file.read()

    date, time = extract_datetime(text)
    payment_method = extract_payment_method(text)
    total = extract_total(text)
    items = extract_items(text)
    prices = extract_all_prices(items, total)
    product_names = [item["name"] for item in items]

    result = {
        "date": date,
        "time": time,
        "payment_method": payment_method,
        "product_names": product_names,
        "prices": prices,
        "calculated_total": round(sum(item["line_total"] for item in items), 2),
        "receipt_total": total,
        "items": items
    }

    print("DATE:", result["date"])
    print("TIME:", result["time"])
    print("PAYMENT METHOD:", result["payment_method"])

    print("\nPRODUCT NAMES:")
    for name in result["product_names"]:
        print("-", name)

    print("\nPRICES:")
    for price in result["prices"]:
        print(price)

    print("\nCALCULATED TOTAL:", result["calculated_total"])
    print("RECEIPT TOTAL:", result["receipt_total"])

    print("\nJSON OUTPUT:")
    print(json.dumps(result, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    main()