%define		snap	20080528
Summary:	A simple cross platform web browser
Name:		arora
Version:	0.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://arora.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	702d29d021f7ac2c4e3ace3252876071
URL:		http://code.google.com/p/arora/
BuildRequires:	QtWebKit-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
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
%setup -q

%build
qmake-qt4 PREFIX=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/arora
%{_pixmapsdir}/*.*
%{_iconsdir}/*/*/*/*.png
%{_iconsdir}/*/*/*/*.svg
%{_desktopdir}/arora.desktop
%dir %{_datadir}/arora
%dir %{_datadir}/arora/locale
%lang(cs_CZ) %{_datadir}/arora/locale/cs_CZ.qm
%lang(da) %{_datadir}/arora/locale/da.qm
%lang(de) %{_datadir}/arora/locale/de.qm
%lang(en) %{_datadir}/arora/locale/en.qm
%lang(es) %{_datadir}/arora/locale/es.qm
%lang(et) %{_datadir}/arora/locale/et.qm
%lang(fr_CA) %{_datadir}/arora/locale/fr_CA.qm
%lang(fr_FR) %{_datadir}/arora/locale/fr_FR.qm
%lang(hu) %{_datadir}/arora/locale/hu.qm
%lang(it) %{_datadir}/arora/locale/it.qm
%lang(nl) %{_datadir}/arora/locale/nl.qm
%lang(pl) %{_datadir}/arora/locale/pl.qm
%lang(pt_BR) %{_datadir}/arora/locale/pt_BR.qm
%lang(tr) %{_datadir}/arora/locale/tr.qm
%lang(ru) %{_datadir}/arora/locale/ru.qm
#%lang(zh_CN) %{_datadir}/arora/locale/zh_CN.qm
%{_mandir}/man1/*.1*
