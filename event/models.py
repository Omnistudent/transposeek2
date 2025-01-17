from django.db import models
from django.contrib.auth.models import User

import os
from django.conf import settings



#class UserXc(AbstractUser):
  #  x = models.IntegerField(null=True, blank=True)
  #  y = models.IntegerField(null=True, blank=True)

class ListItem(models.Model):
    name = models.CharField(max_length=100)
    is_checked = models.BooleanField(default=False)
    size=models.IntegerField("size",default=-1)
    # Add other fields as needed
	
class ListItem2(models.Model):
    name = models.CharField(max_length=100)
    is_checked = models.BooleanField(default=False)
    size=models.IntegerField("size",default=-1)
    # Add other fields as needed




	
class UserProfile(models.Model):

	last_active_time = models.DateTimeField(null=True, blank=True)
	name=models.CharField('User Name',max_length=120,default='0')
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user_type=models.CharField('user_type',max_length=120,default='regular')
	
	current_genome_dir=models.CharField('user_current_genome_dir',max_length=120,default='')
	blast_directory=models.CharField('blast_directory',max_length=120,default='')
	#blast_directory=models.CharField('blast_directory',max_length=120,default='c:/NCBI/blast-BLAST_VERSION+/bin/')
	first_e_cutoff=models.CharField('first_e_cutoff',max_length=120,default='1e-6')
	second_e_cutoff=models.CharField('second_e_cutoff',max_length=120,default='1e-6')
	transposase_protein_database=models.CharField('transposase_protein_database',max_length=120,default='C:/Users/Eris/Documents/scripts/autothink/is_aa_30_nov2016.fa')

	blast_files_dir=models.CharField('blast_files_dir',max_length=120,default="D:/blastresults/")
	blast_analysis_dir=models.CharField('blast_analysis_dir',max_length=120,default="D:/blastanalysis/")
	final_results_dir=models.CharField('analysed_gb_files',max_length=120,default="D:/final_results/")
	work_files_dir=models.CharField('work_files_dir',max_length=120,default="D:/workfiles/")
	is_list_csv_file_dir=models.CharField('is_list_csv_file_dir',max_length=120,default="D:/is_csvs/")
	is_frequency_pic_dir=models.CharField('is_frequency_pic_dir',max_length=120,default="c:/Users/Eris/Documents/visualAutothink/visapp_proj/static/event/images/")




	def __str__(self):
		return str(self.user)
      
class NCBISubentry(models.Model):
    name = models.CharField('name', max_length=120)
    link = models.CharField('link', max_length=120)
    
    def __str__(self):
        return self.name
    
class NCBIentry(models.Model):
    name = models.CharField('name', max_length=120)
    link = models.CharField('link', max_length=120,blank=True,default="-1")
    assembly_accession = models.CharField('assembly_accession', max_length=120,blank=True,default="-1")
    organism_name = models.CharField('organism_name', max_length=120,blank=True,default="-1")
    genome_rep = models.CharField('genome_rep', max_length=120,blank=True,default="-1")
    assembly_level = models.CharField('assembly_level', max_length=120,blank=True,default="-1")    
    asm_name = models.CharField('asm_name', max_length=120,blank=True,default="-1")
    gbrs_paired_asm = models.CharField('gbrs_paired_asm', max_length=120,blank=True,default="-1")
    ftp_path = models.CharField('ftp_path', max_length=120,blank=True,default="-1")
    assembly_type = models.CharField('assembly_type', max_length=120,blank=True,default="-1")    
    genome_size = models.CharField('genome_size', max_length=120,blank=True,default="-1")
    gc_percent = models.CharField('gc_percent', max_length=120,blank=True,default="-1")
    genome_size_ungapped = models.CharField('genome_size_ungapped', max_length=120,blank=True,default="-1")  
    replicon_count = models.CharField('replicon_count', max_length=120,blank=True,default="-1")
    scaffold_count = models.CharField('scaffold_count', max_length=120,blank=True,default="-1")
    contig_count = models.CharField('contig_count', max_length=120,blank=True,default="-1")
    has_representative = models.CharField('has_reprsentative', max_length=120,blank=True,default="-1")
    database = models.CharField('database',max_length=120, default="-1")
    seq_rel_date=models.CharField('seq_rel_date',max_length=120, default="-1")
    bioproject=models.CharField('bioproject',max_length=120, default="-1")
    biosample=models.CharField('biosample',max_length=120, default="-1")
    wgs_master=models.CharField('wgs_master',max_length=120, default="-1")
    taxid=models.CharField('taxid',max_length=120, default="-1")
    species_taxid=models.CharField('species_taxid',max_length=120, default="-1")
    refseq_category=models.CharField('refseq_category',max_length=120, default="-1")
    taxid=models.CharField('taxid',max_length=120, default="-1")
    infraspecific_name=models.CharField('infraspecific_name',max_length=120, default="-1")
    isolate=models.CharField('isolate',max_length=120, default="-1")
    version_status=models.CharField('version_status',max_length=120, default="-1")
    release_type=models.CharField('release_type',max_length=120, default="-1")
    asm_submitter=models.CharField('asm_submitter',max_length=120, default="-1")
    gbrs_paired_asm=models.CharField('gbrs_paired_asm',max_length=120, default="-1")
    paired_asm_comp=models.CharField('paired_asm_comp',max_length=120, default="-1")
    excluded_from_refseq=models.CharField('excluded_from_refseq',max_length=120, default="-1")
    relation_to_type_material=models.CharField('relation_to_type_material',max_length=120, default="-1")
    group=models.CharField('group',max_length=120, default="-1")
    asm_not_live_date=models.CharField('asm_not_live_date',max_length=120, default="-1")
    relation_to_type_material=models.CharField('relation_to_type_material',max_length=120, default="-1")
    genome_size_ungapped=models.CharField('genome_size_ungapped',max_length=120, default="-1")
    annotation_provider=models.CharField('annotation_provider',max_length=120, default="-1")
    annotation_name=models.CharField('annotation_name',max_length=120, default="-1")
    annotation_date=models.CharField('annotation_date',max_length=120, default="-1")
    total_gene_count=models.CharField('total_gene_count',max_length=120, default="-1")
    protein_coding_gene_count=models.CharField('protein_coding_gene_count',max_length=120, default="-1")
    non_coding_gene_count=models.CharField('non_coding_gene_count',max_length=120, default="-1")
    pubmed_id=models.CharField('pubmed_id',max_length=120, default="-1")


    
    
    
    subentries=models.ManyToManyField(NCBISubentry,blank=True)

    def __str__(self):
        return self.name
    





class Footprint(models.Model):
	start=models.IntegerField('start',default=-1)
	end=models.IntegerField('end',default=-1)
	sequence=models.CharField('sequence',max_length=5000,default="-1")
	def __str__(self):
		return "footprint"
		
class genomeEntry(models.Model):
    name=models.CharField('name',max_length=120)
    nick=models.CharField('nick',max_length=120,default="-")
    path=models.CharField('path',max_length=120,default="-1")
    extra=models.CharField('extra',max_length=120)
    is_dir=models.CharField('is_dir',max_length=120,default=-1)
    description=models.TextField(blank=True)
    contigs_num=models.IntegerField('contigs_num',default=-1)
    genome_size=models.IntegerField('genome_size',default=-1)
    footprint_size=models.IntegerField('footprint_size',default=-1)
    footprint_perc=models.FloatField('footprint_size',default=-1.0)
    button_analyse_isok=models.TextField('button_analyse_isok',default="red")
    button_prepare_isok=models.TextField('button_prepare_isok',default="red")
    button_blast_isok=models.TextField('button_blast_isok',default="red")
    button_blastanal_isok=models.TextField('button_blastanal_isok',default="red")
    button_footprints_isok=models.TextField('button_footprints_isok',default="red")
    button_analyse_results_isok=models.TextField('button_analyse_results_isok',default="red")


    files_num=models.IntegerField('files_num',default=-1)
    footprints=models.ManyToManyField(Footprint,blank=True)

    work_files_dir=models.CharField('work_files_dir',max_length=120,default="D:/workfiles/")
    concat_fasta_file=models.CharField('concat_fasta_file',max_length=120,default="")
    blast_results_file=models.CharField('blast_results_file',max_length=120,default="")
    blast_analysis_file=models.CharField('blast_analysis_file',max_length=120,default="")
    analysed_gb_files=models.CharField('analysed_gb_files',max_length=120,default="")
    is_list_csv_file=models.CharField('is_list_csv_file',max_length=120,default="")
    is_frequency_pic=models.CharField('is_frequency_pic',max_length=120,default="")

    def __str__(self):
	    return self.name


