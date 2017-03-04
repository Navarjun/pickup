#!/usr/bin/env python3.6
import JSHelper as WebDriver

import xml.etree.ElementTree as XMLParser
root = XMLParser.parse("config.xml").getroot()

try:
  startUrl = root.attrib["url"]
except e:
  print(e)
  print("---------")
  print("Please add an attribute 'url' to the 'start' tag in your xml file")
