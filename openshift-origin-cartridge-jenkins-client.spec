%if 0%{?fedora}%{?rhel} <= 6
    %global scl ruby193
    %global scl_prefix ruby193-
%endif

%global cartridgedir %{_libexecdir}/openshift/cartridges/jenkins-client-single-master

Summary:       Embedded jenkins client single master support for OpenShift v2
Name:          openshift-origin-cartridge-jenkins-client-single-master
Version: 1.0
Release:       1%{?dist}
Group:         Network/Daemons
License:       ASL 2.0
URL:           https://github.com/remidiniz/openshift-origin-cartridge-jenkins-client-single-master
Source0:       https://github.com/remidiniz/openshift-origin-cartridge-jenkins-client-single-master/archive/master.tar.gz
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
%if 0%{?fedora}%{?rhel} <= 6
Requires:      java-1.6.0-openjdk
%else
Requires:      java-1.7.0-openjdk
%endif
Requires:      %{?scl:%scl_prefix}rubygems
Requires:      %{?scl:%scl_prefix}rubygem-json
Provides:      openshift-origin-cartridge-jenkins-client-single-master-1.0 = 2.0.0
Obsoletes:     openshift-origin-cartridge-jenkins-client-single-master-1.0 <= 1.99.9
BuildArch:     noarch

%description
Provides plugin jenkins client single master support.

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}/configuration
%{cartridgedir}/metadata
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog