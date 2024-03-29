Summary:	A simple cross platform web browser
Name:		arora
Version:	0.11.0
Release:	2
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://arora.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	64334ce4198861471cad9316d841f0cb
URL:		http://code.google.com/p/arora/
BuildRequires:	QtSql-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake >= 4.5
Requires:	desktop-file-utils
Suggests:	xine-output-video-xcb
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

%post
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*.*
%{_iconsdir}/*/*/*/*.png
%{_iconsdir}/*/*/*/*.svg
%{_desktopdir}/arora.desktop
%dir %{_datadir}/arora
%dir %{_datadir}/arora/locale
%lang(ca) %{_datadir}/arora/locale/ca.qm
%lang(cs_CZ) %{_datadir}/arora/locale/cs_CZ.qm
%lang(da) %{_datadir}/arora/locale/da_DK.qm
%lang(de) %{_datadir}/arora/locale/de_DE.qm
#%lang(en_US) %{_datadir}/arora/locale/en_US.qm
%lang(el_GR) %{_datadir}/arora/locale/el_GR.qm
%lang(es) %{_datadir}/arora/locale/es.qm
%lang(es_CR) %{_datadir}/arora/locale/es_CR.qm
%lang(et) %{_datadir}/arora/locale/et_EE.qm
%lang(fi_FI) %{_datadir}/arora/locale/fi_FI.qm
%lang(fr_CA) %{_datadir}/arora/locale/fr_CA.qm
%lang(fr_FR) %{_datadir}/arora/locale/fr_FR.qm
%lang(gl) %{_datadir}/arora/locale/gl.qm
%lang(he_IL) %{_datadir}/arora/locale/he_IL.qm
%lang(hu) %{_datadir}/arora/locale/hu_HU.qm
%lang(it) %{_datadir}/arora/locale/it_IT.qm
%lang(ja) %{_datadir}/arora/locale/ja_JP.qm
%lang(ms) %{_datadir}/arora/locale/ms.qm
%lang(no) %{_datadir}/arora/locale/nb_NO.qm
%lang(nl) %{_datadir}/arora/locale/nl.qm
%lang(pl) %{_datadir}/arora/locale/pl_PL.qm
%lang(pt_BR) %{_datadir}/arora/locale/pt_BR.qm
%lang(pt_PT) %{_datadir}/arora/locale/pt_PT.qm
%lang(ru) %{_datadir}/arora/locale/ru_RU.qm
%lang(sk) %{_datadir}/arora/locale/sk_SK.qm
%lang(sr_RS) %{_datadir}/arora/locale/sr_RS.qm
%lang(tr) %{_datadir}/arora/locale/tr_TR.qm
%lang(uk) %{_datadir}/arora/locale/uk.qm
%lang(zh_CN) %{_datadir}/arora/locale/zh_CN.qm
%lang(zh_TW) %{_datadir}/arora/locale/zh_TW.qm
%{_mandir}/man1/*.1*
