#!/usr/local/bin/python3


from cgitb import enable
enable()

from cgi import FieldStorage, escape

print('Content-type: text/html')
print()

form_data = FieldStorage()


STUDY = form_data.getfirst('study')
SUBSTUDY = form_data.getfirst('substudy')
CA_INPUTFILE = form_data.getfirst('inputfile')
SEQ_TYPE = form_data.getfirst('seq')
TRIMMED = form_data.getlist('trim')
ADAPTOR = form_data.getfirst('adaptor')
RRNA_INDEXES_LOCATION = form_data.getfirst('genind')
GENOME_INDEXES_LOCATION = form_data.getlist('genfa')
RNASE_SCRIPT = form_data.getfirst('rpscr')
RNASE_OFFSET= form_data.getlist('offset')
CHROM_SIZES = form_data.getlist('chromsize')


if len(form_data) != 0 :
   # if SEQ_TYPE != '' AND TRIMMED != '' AND ADAPTOR != ''AND RRNA_INDEXES_LOCATION != '' AND GENOME_INDEXES_LOCATION != '' AND RNASE_SCRIPT != '' AND RNASE_OFFSET!= '' AND CHROM_SIZES != '':
       myfile = open('CONFIG_FILE', 'w')
       myfile.write ('#the root directory for the study')
       myfile.write ("\n")
       if SEQ_TYPE =='Ribo':
            myfile.write ('BASE_DIR=/home/DATA/GWIPS_viz/Ribo_seq')
       elif SEQ_TYPE == 'mRNA_seq':
            myfile.write ('BASE_DIR=/home/DATA/GWIPS_viz/mRNA')
       myfile.write ("\n")
       myfile.write ("STUDY= %s", STUDY)
       myfile.write ("\n")
       myfile.write ("SUBSTUDY= %s", SUBSTUDY)
       myfile.write ("\n") 
       myfile.write ("#Type of seq Ribo-seq or mRNA-seq (no profile created)")
       myfile.write ("\n")
       myfile.write ("SEQ_TYPE=Ribo-seq")
       myfile.write ("\n") 
       myfile.write ("#Cutadapt parameters")
       myfile.write ("\n")
       myfile.write ("ADAPTOR=%s", ADAPTOR)
       myfile.write ("\n")
       myfile.write ("CA_INPUTFILE=%s", CA_INPUFILE)
       myfile.write ("\n")
       myfile.write ("#Input file already trimmed enter Y or N")
       myfile.write ("\n") 
       myfile.write ("TRIMMED=%s",TRIMMED)
       myfile.write ("\n")
       myfile.write ("#Bowtie remove ribosomal rRNA parameters")
       myfile.write ("\n")
       myfile.write ("RRNA_INDEXES_DIR=/home/DATA/rRNA_indexes")
       myfile.write ("\n")
       myfile.write ("RRNA_INDEXES_LOCATION=%s", RRNA_INDEXES_LOCATION)
       myfile.write ("\n") 
       myfile.write ("#Bowtie align to genome parameters",)
       myfile.write ("\n")
       myfile.write ("GENOME_INDEXES_DIR=/home/DATA/GWIPS_viz/Annotations_genomes_etc")
       myfile.write ("\n")
       myfile.write ("GENOME_INDEXES_LOCATION=%s", GENOME_INDEXES_LOCATION)
       myfile.write ("\n")
       myfile.write ("#Ribosome profile info")
       myfile.write ("\n")
       myfile.write ("RNASE_SCRIPT=", RNASE_SCRIPT)
       myfile.write ("\n") 
       myfile.write ("GENOME_FASTA_DIR=/home/DATA/GWIPS_viz/Annotations_genomes_etc")
       myfile.write ("\n")
       myfile.write ("GENOME_FASTA_LOCATION=%s", GENOME_FASTA_LOCATION)
       myfile.write ("\n")
       myfile.write ("RRNA_INDEXES_DIR=/home/DATA/rRNA_indexes")
       myfile.write ("\n")
       myfile.write ("RRNA_INDEXES_LOCATION=%s", RRNA_INDEXES_LOCATION)
       myfile.write ("\n") 
       myfile.write ("RNASE_OFFSET=%s", OFFSET)
       myfile.write ("\n")
       myfile.write ("#Ribosome Coverage parameters")
       myfile.write ("\n")
       myfile.write ("CHROM_SIZES_DIR=/home/DATA/GWIPS_viz/bigWig")
       myfile.write ("\n")
       myfile.write ("CHROM_SIZES = %s", CHROM_SIZES)
       myfile.write ("\n")
     #else:
     #outcome = "Error. Fill all the fields"
else:
    
    outcome = "Error. No Entry"

