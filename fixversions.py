#!/usr/bin/python

import yaml
from xml.etree import ElementTree as et

f = open('versions.yaml')
dataMap = yaml.load(f)
f.close

ns = "http://maven.apache.org/POM/4.0.0"

et.register_namespace('', "%s" % ns)

for project in dataMap.keys():

    filename = project + "/pom.xml"

    tree = et.ElementTree()
    tree.parse(filename)

    if tree.getroot().find("{%s}artifactId" % ns) is not None:
	if tree.getroot().find("{%s}artifactId" % ns).text in dataMap:
    	    tree.getroot().find("{%s}version" % ns).text = dataMap[tree.getroot().find("{%s}artifactId" % ns).text]

    deps = tree.getroot().findall(".//{%s}dependency" % ns)

    for dep in deps:
        if dep.find("{%s}artifactId" % ns) is not None:
	    if dep.find("{%s}artifactId" % ns).text in dataMap:
    	        dep.find("{%s}version" % ns).text = dataMap[dep.find("{%s}artifactId" % ns).text]

    tree.write(project + "/pom.xml")
