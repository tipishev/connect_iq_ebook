Connect IQ eBook
----------------

To create xml and mc run::

    >>> self.file = open('dracula.txt', 'r')
    >>> device = Fenix5()
    >>> chunker = Chunker(self.file,
    >>>                   char_to_width=device.char_to_width,
    >>>                   line_widths=device.line_widths,
    >>>                   max_chunk_size=8000)
    >>> self.file_maker = FileMaker(chunker, device=device)
    >>> self.file_maker.write_files()
