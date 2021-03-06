# This file is part of MAMMULT: Metrics And Models for Multilayer Networks
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import networkx as nx
import sys


if __name__ == "__main__":

	
	if len(sys.argv) < 6:
	    print "Usage: %s <layer1> <layer2> <N bins> <min_value> <max_value>" % sys.argv[0]
	    sys.exit(1)


	filename_a = sys.argv[1]
	filename_b = sys.argv[2]
	
	intervals=int(sys.argv[3])
	minvalue=float(sys.argv[4])
	maxvalue=float(sys.argv[5])
	
	
	tot_a = []
	pos_a = []
	for t in range (intervals):
		tot_a.append(0)
		pos_a.append(0)

	

	
	fa=open(filename_a, 'r')
	Ga=nx.read_adjlist(fa)
	
	
	fb=open(filename_b, 'r')
	Gb=nx.read_weighted_edgelist(fb)
	
	

	
	for u,v in Gb.edges():
		Gbw=Gb[u][v]['weight']
		for i in range (intervals):
			a=minvalue+float(maxvalue-minvalue)*float(i)/intervals
			b=minvalue+float(maxvalue-minvalue)*float(i+1)/intervals
			if (Gbw>a and Gbw<b):
				tot_a[i]+=1
				break
		if (Ga.has_edge(u,v)==True):
			pos_a[i]+=1

	freq_a=[]
	for i in range (intervals):
		if (tot_a[i]>0):
			freq_a.append(float(pos_a[i])/tot_a[i])
		else:
			freq_a.append(0)
	print "#bin_minvalue bin_maxvalue frequence"
	for i in range (intervals):
		a=minvalue+float(maxvalue-minvalue)*float(i)/intervals
		b=minvalue+float(maxvalue-minvalue)*float(i+1)/intervals
		print a, b, freq_a[i]
