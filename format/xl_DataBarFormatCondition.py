# Copyright(c) 2016, David Mans, Konrad Sobon
# @arch_laboratory, http://archi-lab.net, http://neoarchaic.net

import clr
import sys

pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)

import os
appDataPath = os.getenv('APPDATA')
dynPath = appDataPath + r"\Dynamo\0.9"
if dynPath not in sys.path:
	sys.path.Add(dynPath)
	
bbPath = appDataPath + r"\Dynamo\0.9\packages\Bumblebee\extra"
if bbPath not in sys.path:
	try:
		sys.path.Add(bbPath)
		import bumblebee as bb
	except:
		import xml.etree.ElementTree as et
		root = et.parse(dynPath + "\DynamoSettings.xml").getroot()
		for child in root:
			if child.tag == "CustomPackageFolders":
				for path in child:
					if path not in sys.path:
						sys.path.Add(path)
		import bumblebee as bb

#The inputs to this node will be stored as a list in the IN variable.
dataEnteringNode = IN

minType = IN[0]
minValue = IN[1]
maxType = IN[2]
maxValue = IN[3]
directionType = IN[4]
gradientFill = IN[5]
fillColor = IN[6]
borderColor = IN[7]

formatCondition = bb.BBDataBarFormatCondition()

if minType != None:
	formatCondition.minType = minType
if minValue != None:
	formatCondition.minValue = minValue
if maxType != None:
	formatCondition.maxType = maxType
if maxValue != None:
	formatCondition.maxValue = maxValue
if directionType != None:
	formatCondition.directionType = directionType
if gradientFill != None:
	formatCondition.gradientFill = gradientFill
if fillColor != None:
	formatCondition.fillColor = fillColor
if borderColor != None:
	formatCondition.borderColor = borderColor

#Assign your output to the OUT variable
OUT = formatCondition
