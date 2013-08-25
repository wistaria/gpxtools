#!/usr/bin/env python

# ref: http://docs.python.jp/3/library/xml.etree.elementtree.html

import sys
import xml.etree.ElementTree as ET

ns = 'http://www.topografix.com/GPX/1/1'
prefix = '{' + ns + '}'

root = ET.parse(sys.argv[1] if (len(sys.argv) == 2) else sys.stdin).getroot()

print '<?xml version="1.0" encoding="UTF-8" standalone="no" ?>'
print '<gpx xmlns="' + ns + '">'

for trk in root.findall(prefix + 'trk'):
    print '<trk>'
    print '<trkseg>'
    for seg in trk.findall(prefix + 'trkseg'):
        for pt in seg.findall(prefix + 'trkpt'):
            trkpt = ET.Element('trkpt')
            lat = pt.attrib['lat']
            lon = pt.attrib['lon']
            ele = pt.find(prefix+'ele').text
            time = pt.find(prefix+'time').text
            print '<trkpt lat="' + lat + '" lon="' + lon + '">' + '<ele>' + ele + '</ele><time>' + time + '</time></trkpt>'
    print '</trkseg>'
    print '</trk>'

print '</gpx>'
