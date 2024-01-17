def ft_tqdm(lst: range) -> None:
    """def ft_tqdm(lst: range) -> None:"""
    total = 180;
    new_range=range(lst.start, lst.stop + 1, lst.step)
    for elem in new_range:
        tqdm = elem / (new_range.stop + 1)
        print(f"{int(tqdm * 100)}%|{'█' * (int(total * tqdm))}{' ' * int(total - (int(total * tqdm)))} | {elem}/{new_range.stop - 1}", end='\r')
        yield elem
    print()

