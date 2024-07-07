
def read_text(filename):
        # open the file
        file = open(filename, mode='rt', encoding='utf-8')
        
        # read all text
        text = file.read()
        file.close()
        return text

def to_lines(text):
    sents = text.strip().split('\n')
    return sents