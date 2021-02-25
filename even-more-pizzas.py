#!/usr/bin/env python3

import sys
import os
import subprocess
import optparse
import codecs
import solution1


SolutionList = [
    solution1.DeliverPizzas(),
]

if __name__ == '__main__':
    StubDirName = 'stubs'
    option_parser = optparse.OptionParser(
        usage='python %prog [options] <grep_executable>', version='1.0')
    option_parser.add_option('-i', '--input',
                             dest='input', type='string', default= 'Input/example.txt')
    option_parser.add_option('-o', '--output',
                             dest='output', type='string')
    options, args = option_parser.parse_args(sys.argv[1:])

    # Create a file to hold the generated encoded data.
    outputFilename = 'output'

    fileName = options.input
    with open(fileName, 'rt') as infile:
      inputData = infile.read()
    
    for solution in SolutionList:
      output = solution.DeliverPizzas(inputData)

    output_file = open(outputFilename+".txt", "w")
    output_file.write(output)
    output_file.close()