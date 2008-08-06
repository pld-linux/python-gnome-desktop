%define		module			gnome-python-desktop
%define		pygtk_req		2:2.12.0
%define		gnome_python_req	2.22.0
#
# Conditional builds:
%bcond_without	totem		# disable totem support
#
Summary:	GNOME bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek GNOME
Name:		python-gnome-desktop
Version:	2.23.0
Release:	1
License:	GPL v2/LGPL v2.1 (see COPYING)
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-python-desktop/2.23/%{module}-%{version}.tar.bz2
# Source0-md5:	d8f8e61d99402e8b0a82d3c8d6e873be
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	bug-buddy >= 2.22.0
BuildRequires:	gnome-desktop-devel >= 2.10.0
BuildRequires:	gnome-keyring-devel >= 2.22.0
BuildRequires:	gnome-media-devel >= 2.22.0
BuildRequires:	gnome-panel-devel >= 2.22.0
BuildRequires:	gnome-vfs2-devel >= 2.22.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtksourceview-devel >= 1.8.4
BuildRequires:	libgnomeprintui-devel >= 2.18.1
BuildRequires:	libgtop-devel >= 2.22.0
BuildRequires:	librsvg-devel >= 1:2.22.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.22.0
BuildRequires:	nautilus-cd-burner-devel >= 2.22.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.3.2
BuildRequires:	python-gnome-devel >= %{gnome_python_req}
BuildRequires:	python-pycairo-devel
BuildRequires:	python-pygtk-devel >= %{pygtk_req}
BuildRequires:	rpmbuild(macros) >= 1.336
%{?with_totem:BuildRequires:	totem-pl-parser-devel >= 1.6.0}
BuildRequires:	waf >= 1.4.2
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
GNOME bindings for Python.

%description -l pl.UTF-8
Wiązania Pythona do bibliotek GNOME.

%package devel
Summary:	Development files for GNOME bindings for Python
Summary(pl.UTF-8):	Pliki programistyczne wiązań Pythona do GNOME
Group:		Libraries/Python
Requires:	%{name}-applet = %{version}-%{release}
Requires:	%{name}-libwnck = %{version}-%{release}
Requires:	%{name}-nautilus-cd-burner = %{version}-%{release}
Requires:	%{name}-print = %{version}-%{release}
Requires:	python-gnome-devel >= %{gnome_python_req}
Requires:	python-pygtk-devel >= %{pygtk_req}
Obsoletes:	python-gnome-extras-devel < 2.13.3

%description devel
Development files for GNOME bindings for Python.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Pythona do GNOME.

%package apidocs
Summary:	GNOME bindings for Python API documentation
Summary(pl.UTF-8):	Dokumentacja API wiązań Pythona do GNOME
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GNOME bindings for Python API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API wiązań Pythona do GNOME.

%package examples
Summary:	Example programs for python-gnome-desktop
Summary(pl.UTF-8):	Przykładowe programy do python-gnome-desktop
Group:		Libraries/Python
Requires:	%{name}-devel = %{version}-%{release}

%description examples
This package contains example programs for python-gnome-desktop.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy dla python-gnome-desktop.

%package applet
Summary:	GNOME Applet bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GNOME Applet
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-gnome-ui >= %{gnome_python_req}
Requires:	python-pygtk-glade >= %{pygtk_req}
Provides:	python-gnome-applet
Obsoletes:	python-gnome-applet
Obsoletes:	python-gnome-extras-applet

%description applet
GNOME Applet bindings for Python.

%description applet -l pl.UTF-8
Wiązania Pythona do biblioteki GNOME Applet.

%package evolution
Summary:	Evolution bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek Evolution
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-gnome-ui >= %{gnome_python_req}
Requires:	python-pygtk-glade >= %{pygtk_req}
Provides:	python-evolution
Obsoletes:	python-evolution

%description evolution
Evolution bindings for Python.

%description evolution -l pl.UTF-8
Wiązania Pythona do bibliotek Evolution.

%package gtksourceview
Summary:	Gtksourceview bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki gtksourceview
Group:		Libraries/Python
Requires:	%{name}-print = %{version}-%{release}
Obsoletes:	python-gnome-extras-gtksourceview

%description gtksourceview
Gtksourceview bindings for Python.

%description gtksourceview -l pl.UTF-8
Wiązania Pythona do biblioteki gtksourceview.

%package keyring
Summary:	GNOME keyring bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GNOME keyring
Group:		Libraries/Python
Requires:	python-pygobject >= 2.14.0

%description keyring
GNOME keyring bindings for Python.

%description keyring -l pl.UTF-8
Wiązania Pythona do biblioteki GNOME keyring.

%package libgtop
Summary:	Libgtop bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki libgtop
Group:		Libraries/Python
Requires:	python-pygobject >= 2.14.0
Obsoletes:	python-gnome-extras-libgtop

%description libgtop
Libgtop bindings for Python.

%description libgtop -l pl.UTF-8
Wiązania Pythona do biblioteki libgtop.

%package librsvg
Summary:	Librsvg bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki librsvg
Group:		Libraries/Python
Requires:	librsvg >= 1:2.22.0

%description librsvg
Librsvg bindings for Python.

%description librsvg -l pl.UTF-8
Wiązania Pythona do biblioteki librsvg.

%package libwnck
Summary:	Libwnck bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki libwnck
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}
Obsoletes:	python-gnome-extras-libwnck

%description libwnck
Libwnck bindings for Python.

%description libwnck -l pl.UTF-8
Wiązania Pythona do biblioteki libwnck.

%package mediaprofiles
Summary:	gnome-media-profiles bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do gnome-media-profiles
Group:		Libraries/Python
Requires:	python-gnome-ui >= %{gnome_python_req}
Requires:	python-pygtk-glade >= %{pygtk_req}
Obsoletes:	python-gnome-extras-mediaprofiles

%description mediaprofiles
gnome-media-profiles bindings for Python.

%description mediaprofiles -l pl.UTF-8
Wiązania Pythona do gnome-media-profiles.

%package nautilus-cd-burner
Summary:	Nautilus-cd-burner bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki nautilus-cd-burner
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}
Obsoletes:	python-gnome-extras-nautilus-cd-burner

%description nautilus-cd-burner
Nautilus-cd-burner bindings for Python.

%description nautilus-cd-burner -l pl.UTF-8
Wiązania Pythona do biblioteki nautilus-cd-burner.

%package print
Summary:	GNOME Print bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GNOME obsługi drukowania
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-gnome-canvas >= %{gnome_python_req}
Provides:	python-gnome-print
Provides:	python-gnome-print-ui
Obsoletes:	python-gnome-extras-print
Obsoletes:	python-gnome-print
Obsoletes:	python-gnome-print-ui

%description print
GNOME Print bindings for Python.

%description print -l pl.UTF-8
Wiązania Pythona do biblioteki GNOME obsługi drukowania.

%package totem
Summary:	Totem bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki totem
Group:		Libraries/Python
Requires:	python-gnome-vfs >= %{gnome_python_req}
Requires:	python-pygtk-gtk >= %{pygtk_req}
Obsoletes:	python-gnome-extras-totem

%description totem
Totem bindings for Python.

%description totem -l pl.UTF-8
Wiązania Pythona do biblioteki totem.

%prep
%setup -q -n %{module}-%{version}

%build
%waf configure \
	--prefix %{_prefix} \
	--libdir %{_libdir}
%{__waf} -v build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__waf} install \
	--destdir $RPM_BUILD_ROOT

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/{{*.la,*.py},*/{*.la,*.py}}

# wscript doesn't allow to pass proper gtk-doc dir
if [ ! -d $RPM_BUILD_ROOT%{_gtkdocdir} ]; then
	install -d $RPM_BUILD_ROOT%{_gtkdocdir}
	mv $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/* $RPM_BUILD_ROOT%{_gtkdocdir}
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS
%dir %{py_sitedir}/gtk-2.0/gnomedesktop
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomedesktop/_gnomedesktop.so
%{py_sitedir}/gtk-2.0/gnomedesktop/__init__.py[co]

%files devel
%defattr(644,root,root,755)
%{pydefsdir}/*.defs
%{_pkgconfigdir}/gnome-python-desktop-2.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/pygnomeprint
%{_gtkdocdir}/pygnomeprintui
%{_gtkdocdir}/pygtksourceview

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files applet
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomeapplet.so

%files evolution
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/evolution
%attr(755,root,root) %{py_sitedir}/gtk-2.0/evolution/ebook.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/evolution/ecal.so
%{py_sitedir}/gtk-2.0/evolution/__init__.py[co]

%files gtksourceview
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtksourceview.so

%files keyring
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gnomekeyring.so

%files libgtop
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtop.so

%files librsvg
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/rsvg.so

%files libwnck
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/wnck.so

%files mediaprofiles
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/mediaprofiles.so

%files nautilus-cd-burner
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/nautilusburn.so

%files print
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/gnomeprint
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomeprint/_print.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomeprint/ui.so
%{py_sitedir}/gtk-2.0/gnomeprint/__init__.py[co]

%if %{with totem}
%files totem
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/totem
%attr(755,root,root) %{py_sitedir}/gtk-2.0/totem/plparser.so
%{py_sitedir}/gtk-2.0/totem/__init__.py[co]
%endif
