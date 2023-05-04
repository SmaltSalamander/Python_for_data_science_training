def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    terminal_width = 80
    an_element = terminal_width / 100
    length = len(lst)
    for idx in range(length):
        percentage = int(((idx + 1) / length) * 100)
        progress = int(an_element * percentage)
        not_progress = int(terminal_width - progress)
        progress_bar = '|' + ('█' * progress) + (' ' * not_progress) + '|'
        spaces = ' ' * (3 - len(str(percentage)))
        perc_string = f"\r{spaces}{percentage}%"
        spaces_index = f"{' ' * (len(str(length)) - len(str(idx + 1)))}"
        items = str(f"{spaces_index}{idx + 1}/{length}")
        print(f"{perc_string}{progress_bar} {items}", end='')
        yield
