%define		snap	20080528
Summary:	A simple cross platform web browser
Name:		arora
Version:	0.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	%{name}-20080528.tar.bz2
# Source0-md5:	a5f1c6df366748bf8e6f556e12f220d1
URL:		http://code.google.com/p/arora/
BuildRequires:	QtWebKit-devel
BuildRequires:	qt4-qmake >= 4.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Arora was originally created as a demo for Qt to help test the
QtWebKit component and find API issues and bugs before the release. An
older version can still be found in Qt's source code in the
demo/browser directory. Currently Arora is a very basic browser whose
feature list includes things like "History" and "Bookmarks". It does
not have support for netscape plugins, so no flash support until Qt
4.5. But it is small, less then 10,000 lines of code, very fast, lean,
mean and loads of fun to hack on.

%prep
%setup -q -n %{name}

%build
qmake-qt4 PREFIX=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/arora
%{_desktopdir}/arora.desktop
%dir %{_datadir}/arora
%lang(cs_CZ) %{_datadir}/arora/locale/cs_CZ.qm
%lang(de) %{_datadir}/arora/locale/de.qm
%lang(en) %{_datadir}/arora/locale/en.qm
%lang(es) %{_datadir}/arora/locale/es.qm
%lang(fr) %{_datadir}/arora/locale/fr.qm
%lang(pl) %{_datadir}/arora/locale/pl.qm
%lang(ru) %{_datadir}/arora/locale/ru.qm
