import matplotlib.pyplot as plt
labels = ['TEs', 'RIP', 'AT-rich', 'HEs','InDels', 'CNVs','SNPs','Polysomy','CDCs','Orphan genes','Epigenetic','HGT','Hybridization', 'Polyploidization']
sizes = [500, 500, 500, 500, 500, 500, 500, 500,500,500,500,500,500,500]

labels_gender = ['Genomics', 'Transcriptomics', 'Proteomics', 'Metabolomics', 'Effectoromics', 'Genomics', 'Transcriptomics', 'Secretomics','Interactome']
sizes_gender = [200, 200, 200, 200, 200, 200, 200, 200,200]



colors = ['#458B74', '#66CDAA', '#76EEC6', '#7FFFD4', '#98F5FF', '#8EE5EE', '#7AC5CD','#97FFFF','#8DEEEE','#79CDCD','#00CED1','#ADD8E6','#BFEFFF','#B2DFEE']
colors_gender = ['#D2B48C', '#FFA54F', '#EE9A49', '#CD853F', '#8B5A2B', '#FFE1FF', '#EED2EE', '#CDB5CD','#8B7B8B']


plt.pie(sizes, labels=labels, colors=colors, startangle=90, frame=True)
plt.pie(sizes_gender, labels=labels_gender,colors=colors_gender, radius=0.75, startangle=90)

centre_circle = plt.Circle((0, 0), 0.5, color='black', fc='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.tight_layout()
plt.show()
