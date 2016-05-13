from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost
from mininet.node import OVSController
import time
import threading

class CustomTopo(Topo):
		
	def __init__(self):
	# Creating a custom topology

		# Initializing the topology
		Topo.__init__(self)

		# Host addition
		HostH1 = self.addHost('H1', ip='10.0.0.1', mac='00:00:00:00:ff:01')
		HostH2 = self.addHost('H2', ip='10.0.0.2', mac='00:00:00:00:ff:02')
		HostH3 = self.addHost('H3', ip='10.0.0.3', mac='00:00:00:00:ff:03')
		HostH4 = self.addHost('H4', ip='10.0.0.4', mac='00:00:00:00:ff:04')

		# Switch addition
		SwitchS1 = self.addSwitch('S1')
		SwitchS2 = self.addSwitch('S2')

		# Links between switches and hosts1
		self.addLink(SwitchS2, SwitchS1, bw=20, delay='2ms', loss=10, cls=TCLink)
		self.addLink(HostH1, SwitchS1, bw=10, delay='2ms', cls=TCLink)
		self.addLink(HostH2, SwitchS1, bw=20, delay='10ms', cls=TCLink)
		self.addLink(HostH3, SwitchS2, bw=10, delay='2ms', cls=TCLink)
		self.addLink(HostH4, SwitchS2, bw=20, delay='10ms', cls=TCLink)

def iperfTopo():
	topo = CustomTopo()
	net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink, controller=OVSController)
	net.start()
	
	H1 = net.get('H1')
	H2 = net.get('H2')
	H3 = net.get('H3')
	H4 = net.get('H4')
	
	# Generation of TCP flow from clients (H1,H2) to servers (H3,H4) respectively
	def iperfH3H1():
		h3 = H3.cmd('iperf -s &')
		print h3
		h1 = H1.cmd('iperf -c 10.0.0.3 -t 20 -i 0.5')
		print h1
	
	time.sleep(10)

	def iperfH4H2():
		h4 = H4.cmd('iperf -s &')
		print h4
		h2 = H2.cmd('iperf -c 10.0.0.4 -t 20 -i 0.5 ')
		print h2
	
	t1 = threading.Thread(target=iperfH3H1, args=())
	t2 = threading.Thread(target=iperfH4H2, args=())

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	net.stop()


if __name__ == '__main__':
	setLogLevel('info')
	iperfTopo()
