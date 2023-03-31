def file_gen(fnames):
    for fname in fnames:
        if fname.endswith('.txt'):
            yield fname