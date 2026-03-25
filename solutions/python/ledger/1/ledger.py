# ledger.py
#
# Refactor log:
# 1. Replaced monolithic formatting logic with small focused helpers.
# 2. Centralized locale-specific labels and date formats in configuration.
# 3. Centralized currency symbol lookup.
# 4. Isolated description truncation and money formatting rules.
# 5. Made sorting explicit: date, description, change.
# 6. Kept output widths and spacing identical to the canonical tests.

from dataclasses import dataclass


@dataclass(frozen=True)
class Entry:
    date: str
    description: str
    change: int


def create_entry(date, description, change):
    return Entry(date, description, change)


LOCALE_CONFIG = {
    "en_US": {
        "header": ("Date", "Description", "Change"),
        "date_format": "mdy",
    },
    "nl_NL": {
        "header": ("Datum", "Omschrijving", "Verandering"),
        "date_format": "dmy",
    },
}

CURRENCY_SYMBOL = {
    "USD": "$",
    "EUR": "€",
}


def format_entries(currency, locale, entries):
    header_titles = LOCALE_CONFIG[locale]["header"]
    lines = [_format_header(*header_titles)]

    for entry in sorted(entries, key=lambda e: (e.date, e.description, e.change)):
        lines.append(_format_row(entry, currency, locale))

    return "\n".join(lines)


def _format_header(date_label, desc_label, change_label):
    return f"{date_label:<10} | {desc_label:<25} | {change_label:<13}"


def _format_row(entry, currency, locale):
    date_text = _format_date(entry.date, locale)
    desc_text = _format_description(entry.description)
    change_text = _format_money(entry.change, currency, locale)
    return f"{date_text:<10} | {desc_text:<25} | {change_text:>13}"


def _format_date(iso_date, locale):
    year, month, day = iso_date.split("-")
    if LOCALE_CONFIG[locale]["date_format"] == "mdy":
        return f"{month}/{day}/{year}"
    return f"{day}-{month}-{year}"


def _format_description(description):
    if len(description) <= 25:
        return description
    return description[:22] + "..."


def _format_money(amount_in_cents, currency, locale):
    symbol = CURRENCY_SYMBOL[currency]
    abs_amount = abs(amount_in_cents)

    whole = abs_amount // 100
    cents = abs_amount % 100

    if locale == "en_US":
        number = _group_en_us(whole) + f".{cents:02d}"
        if amount_in_cents < 0:
            return f"({symbol}{number})"
        return f"{symbol}{number} "

    number = _group_nl_nl(whole) + f",{cents:02d}"
    if amount_in_cents < 0:
        return f"{symbol} -{number} "
    return f"{symbol} {number} "


def _group_en_us(number):
    return f"{number:,}"


def _group_nl_nl(number):
    return f"{number:,}".replace(",", ".")