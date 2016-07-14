import xml.etree.ElementTree as ET



class MSCReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.tree = ET.parse(self.filepath)
        self.root = self.tree.getroot()
        self.ns = '{http://www.icpsr.umich.edu/DDI}'

    def __enter__(self):
        return self

    def readInstance(self):
       # print self.tree.find('.')[3]
        #print self.tree.find('.//' + self.ns + 'stdyDscr//' + self.ns + 'titl').text
        #print self.tree.find('.//' + self.ns + 'dataDscr/' + self.ns + 'varGrp/').text
        #print self.tree.find('.//' + self.ns + 'dataDscr/' + self.ns + 'varGrp').get('ID')

        #print self.tree.find('.//' + self.ns + 'dataDscr/'+ self.ns + 'var').get('ID')
        #print self.tree.find('.//' + self.ns + 'dataDscr/'+ self.ns + 'var').get('name')
        #print self.tree.find('.//' + self.ns + 'dataDscr//'+ self.ns + 'var/' + self.ns + 'labl').text

        #print self.tree.find('.//' + self.ns + 'dataDscr//'+ self.ns + 'var//' + self.ns + 'qstnLit').text

        #print self.root[0][0]
        #print self.root.attrib

        for v in self.root.findall('.//' + self.ns + 'dataDscr//'+ self.ns + 'var'):
            question_name = ''
            question_label = ''
            question_text = ''

            question_ID = v.get('ID')

            if v.get('name') != None:
                question_name = v.get('name')

            if v.find('./' + self.ns + 'labl') != None:
                question_label = v.find('./' + self.ns + 'labl').text

            if v.find('.//' + self.ns + 'qstnLit') != None:
                question_text = v.find('.//' + self.ns + 'qstnLit').text

            print question_ID
            print question_label
            print question_name
            print question_text

