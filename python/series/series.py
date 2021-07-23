def slices(series: str, length: int) -> list:
    if length > len(series) or length < 1:
        raise ValueError("Invalid length")
    slices_list = []
    for i in range(len(series) - length + 1):
        slices_list.append(series[i:i+length])
    return slices_list
