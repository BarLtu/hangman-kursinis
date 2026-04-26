from word_source import ListWordSource, FileWordSource

class WordSourceFactory:
    @staticmethod
    def get_word_source(source_type, detail=None):
        if source_type == 'file':
            return FileWordSource(detail if detail else "words.txt")
        elif source_type == 'list':
            return ListWordSource()
        else:
            raise ValueError(f"Unknown source type: {source_type}")
