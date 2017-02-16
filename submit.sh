for a in $(ls *); do a2ps --rows 1 --columns 1 -R $a -o $a.ps; done
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -sOutputFile=$(echo $PWD)-daniher.pdf *ps
