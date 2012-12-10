%define up_name check_lm_sensors
%define name    nagios-%{up_name}
%define version 3.1.0
%define release %mkrel 5

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    A Nagios plugin to monitor sensors values
License:    GPL
Group:      Networking/Other
Source:     http://www.id.ethz.ch/people/allid_list/corti/%{up_name}-%{version}.tar.gz
Requires:   hddtemp
Requires:   perl-Nagios-Plugin
BuildArch:  noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
check_lm_sensors is a Nagios plugin to monitor the values of on board sensors
and hard disk temperatures on Linux systems

%prep
%setup -q -n %{up_name}-%{version}

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
install -m 755 check_lm_sensors %{buildroot}%{_datadir}/nagios/plugins

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_lm_sensors.cfg <<'EOF'
define command{
	command_name	check_lm_sensors
	command_line	%{_datadir}/nagios/plugins/check_lm_sensors
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS Changes NEWS README INSTALL TODO COPYING VERSION
%{_datadir}/nagios/plugins/check_lm_sensors
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_lm_sensors.cfg



%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1.0-5mdv2011.0
+ Revision: 620459
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 3.1.0-4mdv2010.0
+ Revision: 440201
- rebuild

* Mon Dec 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.1.0-3mdv2009.1
+ Revision: 314635
- now a noarch package

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 3.1.0-2mdv2009.0
+ Revision: 268243
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.1.0-1mdv2009.0
+ Revision: 218048
- import nagios-check_lm_sensors


* Wed Jun 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.1.0-1mdv2009.0
- first mdv package
