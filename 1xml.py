# import xml.etree.ElementTree as ET
# from okb2.models import *
# from datetime import datetime
# tree = ET.parse("V036.xml")
# root = tree.getroot()
#
# for child in root:
#     if child.findtext("S_CODE") != None:
#         v = V036()
#         v.s_code = child.findtext("S_CODE")
#         v.parameter = int(child.findtext("Parameter"))
#         # v.datebeg = datetime.strptime(child.findtext("DATEBEG"),'%Y-%m-%d') if len(child.findtext("DATEBEG")) != 0 else None
#         # v.dateend = datetime.strptime.strptime(child.findtext("DATEEND"),'%Y-%m-%d') if len(child.findtext("DATEEND")) != 0 else None
#         v.save()
#         # print(parse(child.findtext("DATEBEG")))

# import docx
# from docx.enum.section import WD_ORIENTATION
#
#
# doc = docx.Document()
#
# section = doc.sections
# section.orientation = WD_ORIENTATION.LANDSCAPE
#
# doc.add_paragraph('tes3t1')
# doc.save('1211.docx')


class StringList:
    def __init__(self,val):
        self.val = val
    def __hash__(self):
        return hash(str(self.val))
    def __repr__(self):
        return str(self.val)
    def __eq__(self, other):
        return str(self.val) == str(other.val)
    def __getitem__(self, item):
        s = str(self.val)
        s = s.replace('[', '')
        s = s.replace(']','')
        return s.split(',')[item]

pats= []
pats.append(
StringList(['СЕМЕНОВА',
            'ТАТЬЯНА',
            'АНАТОЛЬЕВНА'])
)
for p in pats:
    print(f'{p[0]}{p[1]}')