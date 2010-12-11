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

