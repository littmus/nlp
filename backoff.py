import os
from lxml import etree as ET
import kenlm

def main(argv):
    path = os.path.dirname(os.path.abspath(__file__))
    file_input = os.path.join(path, argv[0])
    file_output = os.path.join(path, argv[1])
    
    with open(file_input) as nyt, open(file_output, 'wb') as text:
        context = ET.iterparse(nyt, events=('end',), tag='TEXT')

        count = 0
        for event, elem in context:
            text.write(elem.text.encode('utf-8'))
            count += 1
    
    os.system("lmplz -o 4 --text %s --arpa %s.arpa" % (file_output, file_output))
    print 'language model generated'

    model = kenlm.LanguageModel('%s.arpa' % file_output)
    print '{0}-gram model'.format(model.order)


if __name__ == '__main__':
    main(sys.argv[1:])

