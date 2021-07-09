def translation(strand):
    match strand:  # new in 3.10: pattern-matching
        case "AUG":
            yield "Methionine"
        case "UUU" | "UUC":
            yield "Phenylalanine"
        case "UUA" | "UUG":
            yield "Leucine"
        case "UCU" | "UCC" | "UCA" | "UCG":
            yield "Serine"
        case "UAU" | "UAC":
            yield "Tyrosine"
        case "UGU" | "UGC":
            yield "Cysteine"
        case "UGG":
            yield "Tryptophan"
        case "UAA" | "UAG" | "UGA":
            yield "STOP"


def proteins(strand):
    proteins_list = []
    # idiom for clustering into 3-length groups
    for codon in zip(*[iter(strand)] * 3):
        for protein in translation("".join(codon)):
            if protein == "STOP":
                return proteins_list
            if protein not in proteins_list:
                proteins_list.append(protein)
    
    return proteins_list