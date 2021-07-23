def translation(strand: str) -> str:
    match strand:  # new in 3.10: pattern-matching
        case "AUG":
            return "Methionine"
        case "UUU" | "UUC":
            return "Phenylalanine"
        case "UUA" | "UUG":
            return "Leucine"
        case "UCU" | "UCC" | "UCA" | "UCG":
            return "Serine"
        case "UAU" | "UAC":
            return "Tyrosine"
        case "UGU" | "UGC":
            return "Cysteine"
        case "UGG":
            return "Tryptophan"
        case "UAA" | "UAG" | "UGA":
            return "STOP"


def proteins(strand: str) -> list[str]:
    proteins_list = []

    for i in range(0, len(strand), 3):
        protein = translation(strand[i:i+3])
        if protein == "STOP":
            break
        proteins_list.append(protein)

    return proteins_list
