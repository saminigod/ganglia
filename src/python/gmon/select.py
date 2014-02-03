#!/opt/rocks/bin/python
#
# @Copyright@
#
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.6 (Emerald Boa)
# 		         version 6.1 (Emerald Boa)
#
# Copyright (c) 2000 - 2013 The Regents of the University of California.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided
# with the distribution.
#
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement:
#
# 	"This product includes software developed by the Rocks(r)
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
#
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of
# the associated name, interested parties should contact Technology
# Transfer & Intellectual Property Services, University of California,
# San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910,
# Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# @Copyright@
#
# $Log: select.py,v $
# Revision 1.16  2012/11/27 00:48:59  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.15  2012/05/06 05:49:07  phil
# Copyright Storm for Mamba
#
# Revision 1.14  2011/07/23 02:31:00  phil
# Viper Copyright
#
# Revision 1.13  2010/09/07 23:53:18  bruno
# star power for gb
#
# Revision 1.12  2009/05/01 19:07:17  mjk
# chimi con queso
#
# Revision 1.11  2008/10/18 00:56:08  mjk
# copyright 5.1
#
# Revision 1.10  2008/03/06 23:41:51  mjk
# copyright storm on
#
# Revision 1.9  2007/06/23 04:03:36  mjk
# mars hill copyright
#
# Revision 1.8  2006/09/11 22:48:16  mjk
# monkey face copyright
#
# Revision 1.7  2006/08/10 00:10:33  mjk
# 4.2 copyright
#
# Revision 1.6  2006/01/16 06:49:07  mjk
# fix python path for source built foundation python
#
# Revision 1.5  2005/10/12 18:09:19  mjk
# final copyright for 4.1
#
# Revision 1.4  2005/09/16 01:02:56  mjk
# updated copyright
#
# Revision 1.3  2005/08/08 21:24:58  mjk
# foundation
#
# Revision 1.2  2005/05/24 21:22:25  mjk
# update copyright, release is not any closer
#
# Revision 1.1  2005/03/12 00:58:37  fds
# The ganglia command line client. Moved from the monolithic source tree.
#
# Revision 1.7  2004/03/25 03:15:02  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.6  2003/08/27 23:10:55  mjk
# - copyright update
# - rocks-dist uses getArch() fix the i686 distro bug
# - ganglia-python spec file fixes (bad service start code)
# - found some 80col issues while reading code
# - WAN ks support starting
#
# Revision 1.5  2003/02/17 18:43:04  bruno
# updated copyright to 2003
#
# Revision 1.4  2003/02/08 02:22:29  fds
# Added introspective help method.
#
# Revision 1.3  2002/10/18 21:33:25  mjk
# Rocks 2.3 Copyright
#
# Revision 1.2  2002/04/09 05:52:57  mjk
# mds fixes
#
# Revision 1.1  2002/04/09 00:30:51  mjk
# mds changes
#

import gmon.ganglia
import string
import types
import sys

class Base:
	def __init__(self, ganglia, commands, args):
		self.ganglia  = ganglia
		self.commands = commands
		self.args     = args

	def hosts(self):
		return []

	def metrics(self):
		return []

	def help(self):
		pass

	def flavors(self):
		selects = []
		for Class in globals().values():
			if type(Class) == types.ClassType:
				if issubclass(Class, Base) and Class != Base:
					selects.append(Class.__name__)
		return selects

class Default(Base):
	def hosts(self):
		return self.ganglia.getCluster().getHosts()

	def metrics(self):
		return self.commands

	def help(self):
		print 'where "metric" is one of:'
		line = ''
		for metric in self.ganglia.getMetricNames():
			if len(line) + len(metric) > 70:
				print '\t%s' % line
				line = ''
			else:
				line = line + ' ' + metric
		print '\t%s' % line


class All(Base):
	def hosts(self):
		return self.ganglia.getCluster().getHosts()

	def metrics(self):
		return self.ganglia.getMetricNames()
