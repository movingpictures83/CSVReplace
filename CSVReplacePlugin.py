import PyIO
import PyPluMA
class CSVReplacePlugin:
    def input(self, infile):
       self.parameters = PyIO.readParameters(infile)
    def run(self):
       self.csvfile = open(PyPluMA.prefix()+"/"+self.parameters["csvfile"], 'r')
       self.valuefile = open(PyPluMA.prefix()+"/"+self.parameters["values"], 'r')
       self.replace = dict()
       for line in self.valuefile:
           contents = line.strip().split('\t')
           self.replace[contents[0]] = contents[1]
       self.csvcontents = []
       for line in self.csvfile:
           contents = line.strip().split(',')
           for i in range(len(contents)):
               if (contents[i] in self.replace):
                   contents[i] = self.replace[contents[i]]
           self.csvcontents.append(contents)
    def output(self,outfile):
       outputfile = open(outfile, 'w')
       for j in range(len(self.csvcontents)):
          for k in range(len(self.csvcontents[j])):
              outputfile.write(self.csvcontents[j][k])
              if (k == len(self.csvcontents[j])-1):
                  outputfile.write("\n")
              else:
                  outputfile.write(',')
