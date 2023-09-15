#!/bin/sh
scriptdir=`dirname $0`

java -cp "$scriptdir/stanford-ner.jar:$scriptdir/lib/*" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier $scriptdir/ner-model.ser.gz -testFile $1 > -testFile $2

