#!/usr/bin/env python

# ref: http://docs.python.jp/3/library/xml.etree.elementtree.html

import sys, time
import xml.etree.ElementTree as ET
from math import pi, cos, sin, sqrt, pow

ns = 'http://www.topografix.com/GPX/1/1'
prefix = '{' + ns + '}'

re = 6371 * 1000
q = 2*pi/180

root = ET.parse(sys.argv[1] if (len(sys.argv) == 3) else sys.stdin).getroot()
interval = float(sys.argv[len(sys.argv)-1])

print '<?xml version="1.0" encoding="UTF-8" standalone="no" ?>'
print '<gpx xmlns="' + ns + '">'

last = None
printed = False
for trk in root.findall(prefix + 'trk'):
    print '<trk>'
    print '<trkseg>'
    for seg in trk.findall(prefix + 'trkseg'):
        for pt in seg.findall(prefix + 'trkpt'):
            trkpt = ET.Element('trkpt')
            lat = pt.attrib['lat']
            lon = pt.attrib['lon']
            ele = pt.find(prefix+'ele').text
            t = pt.find(prefix+'time').text
            if (last == None):
                dis = 2 * interval
            else:
                dis = sqrt(pow(re*cos(q*float(lat))*sin(q*(float(lon)-float(last[1]))),2) + pow(re*sin(q*(float(lat)-float(last[0]))),2))
            if (dis > interval):
                print '<trkpt lat="' + lat + '" lon="' + lon + '">' + '<ele>' + ele + '</ele><time>' + t + '</time></trkpt>'
                printed = True
                last = (lat, lon, ele, t)
            else:
                printed = False
        if (not printed):
            print '<trkpt lat="' + lat + '" lon="' + lon + '">' + '<ele>' + ele + '</ele><time>' + t + '</time></trkpt>'
    print '</trkseg>'
    print '</trk>'
print '</gpx>'
