%define	_snap	20070705
Summary:	Molecular visualisation system
Summary(pl.UTF-8):	System wizualizacji cząsteczek
Name:		pymol
Version:	1.0
Release:	0.%{_snap}.1
License:	Open Source PyMOL License
Group:		Applications
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	4d2c159249b262ca9fed7e378813f716
URL:		http://www.pymol.org/
BuildRequires:	python-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An open-source, user-sponsored, molecular visualization system.

%description -l pl.UTF-8
Otwarty, sponsorowany przez użytkowników system wizualizacji
cząsteczek.

%prep
%setup -q -n %{name}

%build
env CFLAGS="%{rpmcflags}" \
    LDFLAGS="%{rpmldflags}" \
    %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

%{__python} -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

env PYTHONPATH="$RPM_BUILD_ROOT%{py_sitedir}" \
    %{__python} -- setup2.py install
sed -i s,$RPM_BUILD_ROOT,, %{name}

install %{name} $RPM_BUILD_ROOT%{_bindir}
cp -R examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING LICENSE DEVELOPERS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/%{name}
%{py_sitedir}/chempy
%{py_sitedir}/pmg_wx
%{py_sitedir}/pmg_tk
%{_examplesdir}/%{name}-%{version}
