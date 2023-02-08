import matplotlib.pyplot as plt
group_names= ['Host', 'Pathogen']
group_size= [3,3]
subgroup_names=['TEs', 'RIP', 'AT-rich', 'HEs','InDels', 'CNVs','SNPs','Polysomy','CDCs','Orphan genes','Epigenetic','HGT','Hybridization', 'Polyploidization']
subgroup_size= [10,10,10,10,10,10,10,10,10,10,10,10,10,10]
subsubgroup_names=['Genomics', 'Transcriptomics', 'Proteomics', 'Metabolomics', 'Effectoromics', 'Genomics', 'Transcriptomics', 'Secretomics','Interactome']
subsubgroup_size=[4,4,4,4,4,5,5,5,5]
last_names=['Data analysis and bioinformatics']
last_size=[5]
# Create colors
a, b, c =[plt.cm.Greens, plt.cm.Reds, plt.cm.Blues]

font = {'weight': 'bold', 'size': 10}
plt.rc('font', **font)

fig, ax = plt.subplots()
ax.axis('equal')

mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, labeldistance=0.85, colors=[a(0.5), b(0.5)])
plt.setp( mypie, width=0.29, edgecolor='white')

mypie2, _ = ax.pie(subgroup_size, radius=1.3-0.3,labels=subgroup_names, labeldistance=0.8, colors=[c(0.3)])
plt.setp( mypie2, width=0.4, edgecolor='white')

mypie3, _ = ax.pie(subsubgroup_size, radius=0.59,labels=subsubgroup_names, labeldistance=0.6, colors=[a(0.5), a(0.5),a(0.5),a(0.5),a(0.5),b(0.5),b(0.5),b(0.5),b(0.5)])
plt.setp( mypie3, width=0.3, edgecolor='white')

mypie4, _ = ax.pie(last_size, radius=0.25,labels=last_names, labeldistance=0.6, colors=[c(0.5)])
plt.setp( mypie4, width=0.3, edgecolor='white')

ax.set_title("The integration of genomic variation, mutational events and omics studies in plant pathogen interaction.")
plt.show()
