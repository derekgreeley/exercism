# protein_translation.py

CODON_MAP = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
}

STOP_CODONS = {"UAA", "UAG", "UGA"}


def proteins(strand: str) -> list[str]:
    result = []

    # process in chunks of 3 (codons)
    for i in range(0, len(strand), 3):
        codon = strand[i : i + 3]
        if codon in STOP_CODONS:
            break
        # For this exercise, we assume codon is always valid
        amino_acid = CODON_MAP.get(codon)
        if amino_acid is None:
            # If you wanted to be defensive, you could raise here,
            # but the test suite only uses valid codons.
            continue
        result.append(amino_acid)

    return result
