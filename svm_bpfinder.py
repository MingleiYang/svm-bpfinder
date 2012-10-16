#!/usr/bin/python
import sys,os,commands,time

##########################################################################
base_dir = os.path.dirname(os.path.realpath(__file__))
#print base_dir

fname=sys.argv[1]
species=sys.argv[2]
maxslen=sys.argv[3]
model=base_dir+'/MODELS/'+species+'.svm.model'
infile="%d"%(time.time()*100)+'.in'
outfile="%d"%(time.time()*100)+'.out'
gfscript=base_dir+'/SCRIPTS/svm_getfeat.py'
svmlclass=base_dir+'/SCRIPTS/svm_classify'


##########################################################################

def print_merge(ffn,sfn):
	print '\t'.join(['seq_id','agez','ss_dist','bp_seq','bp_scr','y_cont','ppt_off','ppt_len','ppt_scr','svm_scr']) # header
	for l in commands.getoutput('paste '+ffn+' '+sfn).split('\n'):
		if l!='':
			la=l.split(' #') 
			feats=map(lambda x:x[2:],la[0].split(' ')[1:])
			extras=la[1].split('\t')
			pa=extras[:-2]+feats[:-1]+[extras[-2]]+[feats[-1]]+[extras[-1]]
			print '\t'.join(pa)		

##########################################################################

os.system(gfscript+' '+fname+' '+species+' '+maxslen+' > '+infile)
os.system(svmlclass+' '+infile+' '+model+' '+outfile+' > /dev/null') 
print_merge(infile,outfile)
os.remove(infile)
os.remove(outfile)



