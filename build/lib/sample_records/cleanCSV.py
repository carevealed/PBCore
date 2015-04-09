__author__ = 'lpsdesk'
import string
import unicodedata
f = open("/Users/lpsdesk/PycharmProjects/PBcore/sample_records/cbpf_export_feb2015.csv")
pre = unicode(f.read(), 'utf-8')
converted = unicodedata.normalize('NFKD', pre).encode('ascii','ignore')
of = open('/Users/lpsdesk/PycharmProjects/PBcore/sample_records/cbpf_export_feb2015con.csv', 'w')
of.write(converted)
of.close()
print converted
