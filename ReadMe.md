#Mininet using Python

<strong>Installing  mininet on Linux</strong>
<ul>
<li>sudo apt-get update
<li>sudo apt-get install mininet
</ul>

<strong>Custom Mininet Topology (4hosts and 2 switches)</strong><br>
The file "Custom_Mininet_Topology.py" creates a 4 host (H1,H2,H3,H4) and links them with 2 switches (S1,S2).<br>
These are following parameters given to the topology and can be customized accrodingly by editing the **.py** file:<br>
a.	Topology<br>
b.	Host IP address<br>
c.	Host MAC address<br>
d.	Link latency<br>
e.	Link bandwidth<br>
f.	Link packet loss rate<br>

To test its fucnioanlity one can use the following command:<br>
sudo mn --custom ./Custom_Mininet_Topology.py --topo mytopo --test pingall

<strong>Automatic Host iperf after Topology is Established</strong><br>
The file "Auto_iperf_Host_Mininet.py" creates a mininet topology as the one above, but also automatically generates TCP flow using iperf on Hosts.<br>
Host H1 will generate a TCP flow to H3 with maximum rate from T=0sec (topology built) to T=20sec.<br>
Host H2 will generate a TCP flow to H4 from T=10sec to T=30sec (i.e, after a 10 sec delay from Host H1 parallelly on a different thread).<br>


#References:
1)	Introduction to Mininet https://github.com/mininet/mininet/wiki/Introduction-to-Mininet <br>
2)	Mininet Tutorial<br>
3)	Iperf: https://iperf.fr/<br>