#
# (C) 2007-2010 TaoBao Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# oceanbase.spec is for what ...
#
# Version: $id$
#
# Authors:
#   MaoQi maoqi@alipay.com
#

Name: %NAME
Version: %VERSION
Release: %{RELEASE}
Summary: TaoBao distributed database
Group: Applications/Databases
URL: http://oceanbase.alibaba-inc.com/
Packager: taobao
License: GPL
Vendor: TaoBao
Prefix:%{_prefix}
Source:%{NAME}-%{VERSION}.tar.gz
BuildRoot: %(pwd)/%{name}-root
BuildRequires: t-csrd-tbnet-devel >= 1.0.8 lzo >= 2.06 snappy >= 1.0.2 libaio-devel >= 0.3 t_libeasy-devel >= 1.0.13-186 openssl-devel >= 0.9.8 mysql-devel >= 5.0.77
Requires: lzo >= 2.06 snappy >= 1.0.2 libaio >= 0.3 openssl >= 0.9.8

%package -n oceanbase-utils
summary: OceanBase utility programs
group: Development/Tools
Version: %VERSION
Release: %{RELEASE}


%package -n oceanbase-devel
summary: OceanBase client library
group: Development/Libraries
Version: %VERSION
BuildRequires:curl >= 7.29.0 mysql-devel >= 5.0.77
Requires: curl >= 7.29.0 mysql-devel >= 5.0.77
Release: %{RELEASE}

%description
OceanBase is a distributed database

%description -n oceanbase-utils
OceanBase utility programs

%description -n oceanbase-devel
OceanBase client library

%define _unpackaged_files_terminate_build 0

%prep
%setup

%build
chmod u+x build.sh
./build.sh init
./configure RELEASEID=%{RELEASE} --prefix=%{_prefix} --with-test-case=no --with-release=yes --with-tblib-root=/opt/csr/common --with-easy-root=/usr --with-easy-lib-path=/usr/lib64
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755, admin, admin)
%dir %{_prefix}/etc
%dir %{_prefix}/bin
%dir %{_prefix}/lib
%config(noreplace) %{_prefix}/etc/schema.ini
%config(noreplace) %{_prefix}/etc/lsyncserver.conf.template
%config %{_prefix}/etc/sysctl.conf
%config %{_prefix}/etc/snmpd.conf
%{_prefix}/bin/rootserver
%{_prefix}/bin/updateserver
%{_prefix}/bin/mergeserver
%{_prefix}/bin/chunkserver
%{_prefix}/bin/rs_admin
%{_prefix}/bin/ups_admin
%{_prefix}/bin/cs_admin
%{_prefix}/bin/ob_ping
%{_prefix}/bin/str2checkpoint
%{_prefix}/bin/checkpoint2str
%{_prefix}/bin/lsyncserver
%{_prefix}/bin/dumpsst
%{_prefix}/bin/log_reader
%{_prefix}/lib/liblzo_1.0.a
%{_prefix}/lib/liblzo_1.0.la
%{_prefix}/lib/liblzo_1.0.so
%{_prefix}/lib/liblzo_1.0.so.0
%{_prefix}/lib/liblzo_1.0.so.0.0.0
%{_prefix}/lib/libmrsstable.a
%{_prefix}/lib/libmrsstable.la
%{_prefix}/lib/libmrsstable.so
%{_prefix}/lib/libmrsstable.so.0
%{_prefix}/lib/libmrsstable.so.0.0.0
%{_prefix}/lib/libnone.a
%{_prefix}/lib/libnone.la
%{_prefix}/lib/libnone.so
%{_prefix}/lib/libnone.so.0
%{_prefix}/lib/libnone.so.0.0.0
%{_prefix}/lib/libsnappy_1.0.a
%{_prefix}/lib/libsnappy_1.0.la
%{_prefix}/lib/libsnappy_1.0.so
%{_prefix}/lib/libsnappy_1.0.so.0
%{_prefix}/lib/libsnappy_1.0.so.0.0.0
%{_prefix}/bin/oceanbase.pl
%config %{_prefix}/etc/oceanbase.conf.template
%{_prefix}/tests/

%files -n oceanbase-utils
%defattr(0755, admin, admin)
%{_prefix}/bin/ob_import

%files -n oceanbase-devel
%defattr(0755, admin, admin)
%dir %{_prefix}/lib
%dir %{_prefix}/etc
%{_prefix}/lib/libobsql.so.0.0.0
%{_prefix}/lib/libobsql.a
%config(noreplace) %{_prefix}/etc/libobsql.conf
%config(noreplace) %{_prefix}/etc/libobsqlrc

%post
chown -R admin:admin $RPM_INSTALL_PREFIX
