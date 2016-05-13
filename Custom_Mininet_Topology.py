from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.link import TCLink

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

		# Links between switches and hosts
		self.addLink(SwitchS2, SwitchS1, bw=20, delay='2ms', loss=10, cls=TCLink)
		self.addLink(HostH1, SwitchS1, bw=10, delay='2ms', cls=TCLink)
		self.addLink(HostH2, SwitchS1, bw=20, delay='10ms', cls=TCLink)
		self.addLink(HostH3, SwitchS2, bw=10, delay='2ms', cls=TCLink)
		self.addLink(HostH4, SwitchS2, bw=20, delay='10ms', cls=TCLink)


topos = { 'mytopo' : (lambda:CustomTopo())}