%define		module			gnome-python-desktop
%define		pygtk_req		2:2.8.0
%define		gnome_python_req	2.12.1-3
#
# Conditional builds:
%bcond_without	totem		# disable totem support
#
Summary:	GNOME bindings for Python
Summary(pl):	Wi�zania Pythona do bibliotek GNOME
Name:		python-gnome-desktop
Version:	2.13.3
Release:	1
License:	GPL v2/LGPL v2.1 (see COPYING)
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-python-desktop/2.13/%{module}-%{version}.tar.bz2
# Source0-md5:	98118c8d5ad5480768fa52d4497cf3e3
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-media-devel >= 2.10.0
BuildRequires:	gnome-panel-devel >= 2.10.1
BuildRequires:	gnome-vfs2-devel >= 2.10.1
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	gtksourceview-devel >= 1.2.0
BuildRequires:	hal-devel
BuildRequires:	libgnomeprintui-devel >= 2.10.2
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libgtop-devel >= 2.13.0
BuildRequires:	librsvg-devel >= 1:2.9.5-2
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.10.0
BuildRequires:	metacity-devel
BuildRequires:	nautilus-cd-burner-devel >= 2.11.1
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 1:2.3.2
BuildRequires:	python-gnome-devel >= %{gnome_python_req}
BuildRequires:	python-pygtk-devel >= %{pygtk_req}
%{?with_totem:BuildRequires:	totem-devel >= 0.101}
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
GNOME bindings for Python.

%description -l pl
Wi�zania Pythona do bibliotek GNOME.

%package devel
Summary:	Development files for GNOME bindings for Python
Summary(pl):	Pliki programistyczne wi�za� Pythona do GNOME
Group:		Libraries/Python
Obsoletes:	python-gnome-extras-devel < 2.13.3
Requires:	%{name}-applet = %{version}-%{release}
Requires:	%{name}-nautilus-cd-burner = %{version}-%{release}
Requires:	%{name}-print = %{version}-%{release}
Requires:	%{name}-libwnck = %{version}-%{release}
Requires:	python-pygtk-devel >= %{pygtk_req}

%description devel
Development files for GNOME bindings for Python.

%description devel -l pl
Pliki programistyczne wi�za� Pythona do GNOME.

%package examples
Summary:	Example programs for python-gnome-desktop
Summary(pl):	Przyk�adowe programy do python-gnome-desktop
Group:		Libraries/Python
Requires:	%{name}-devel = %{version}-%{release}

%description examples
This package contains example programs for python-gnome-desktop.

%description examples -l pl
Ten pakiet zawiera przyk�adowe programy dla python-gnome-desktop.

%package applet
Summary:	GNOME Applet bindings for Python
Summary(pl):	Wi�zania Pythona do biblioteki GNOME Applet
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-gnome-ui >= %{gnome_python_req}
Requires:	python-pygtk-glade >= %{pygtk_req}
Obsoletes:	python-gnome-applet
Obsoletes:	python-gnome-extras-applet
Provides:	python-gnome-applet

%description applet
GNOME Applet bindings for Python.

%description applet -l pl
Wi�zania Pythona do biblioteki GNOME Applet.

%package gtksourceview
Summary:	Gtksourceview bindings for Python
Summary(pl):	Wi�zania Pythona do biblioteki gtksourceview
Group:		Libraries/Python
Obsoletes:	python-gnome-extras-gtksourceview
Requires:	%{name}-print = %{version}-%{release}

%description gtksourceview
Gtksourceview bindings for Python.

%description gtksourceview -l pl
Wi�zania Pythona do biblioteki gtksourceview.

%package libgtop
Summary:	Libgtop bindings for Python
Summary(pl):	Wi�zania Pythona do biblioteki libgtop
Group:		Libraries/Python
Obsoletes:	python-gnome-extras-libgtop
Requires:	python-pygtk-gobject >= %{pygtk_req}

%description libgtop
Libgtop bindings for Python.

%description libgtop -l pl
Wi�zania Pythona do biblioteki libgtop.

%package libwnck
Summary:	Libwnck bindings for Python
Summary(pl):	Wi�zania Pythona do biblioteki libwnck
Group:		Libraries/Python
Obsoletes:	python-gnome-extras-libwnck
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description libwnck
Libwnck bindings for Python.

%description libwnck -l pl
Wi�zania Pythona do biblioteki libwnck.

%package mediaprofiles
Summary:	gnome-media-profiles bindings for Python
Summary(pl):	Wi�zania Pythona do gnome-media-profiles
Group:		Libraries/Python
Obsoletes:	python-gnome-extras-mediaprofiles
Requires:	python-gnome-ui >= %{gnome_python_req}
Requires:	python-pygtk-glade >= %{pygtk_req}

%description mediaprofiles
gnome-media-profiles bindings for Python.

%description mediaprofiles -l pl
Wi�zania Pythona do gnome-media-profiles.

%package metacity
Summary:	Metacity bindings for Python
Summary(pl):	Wi�zania Pythona do Metacity
Group:		Libraries/Python
Requires:	python-gnome-ui >= %{gnome_python_req}
Requires:	python-pygtk-glade >= %{pygtk_req}

%description metacity
Metacity bindings for Python.

%description metacity -l pl
Wi�zania Pythona do Metacity.

%package nautilus-cd-burner
Summary:	Nautilus-cd-burner bindings for Python
Summary(pl):	Wi�zania Pythona do biblioteki nautilus-cd-burner
Group:		Libraries/Python
Obsoletes:	python-gnome-extras-nautilus-cd-burner
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description nautilus-cd-burner
Nautilus-cd-burner bindings for Python.

%description nautilus-cd-burner -l pl
Wi�zania Pythona do biblioteki nautilus-cd-burner.

%package print
Summary:	GNOME Print bindings for Python
Summary(pl):	Wi�zania Pythona do biblioteki GNOME obs�ugi drukowania
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-gnome-canvas >= %{gnome_python_req}
Obsoletes:	python-gnome-extras-print
Obsoletes:	python-gnome-print
Obsoletes:	python-gnome-print-ui
Provides:	python-gnome-print
Provides:	python-gnome-print-ui

%description print
GNOME Print bindings for Python.

%description print -l pl
Wi�zania Pythona do biblioteki GNOME obs�ugi drukowania.

%package totem
Summary:	Totem bindings for Python
Summary(pl):	Wi�zania Pythona do biblioteki totem
Group:		Libraries/Python
Obsoletes:	python-gnome-extras-totem
Requires:	python-gnome-vfs >= %{gnome_python_req}
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description totem
Totem bindings for Python.

%description totem -l pl
Wi�zania Pythona do biblioteki totem.

%prep
%setup -q -n %{module}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	HTML_DIR=%{_gtkdocdir}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/{*.la,*/{*.la,*.py}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS

%files devel
%defattr(644,root,root,755)
%{pydefsdir}/*
%{_pkgconfigdir}/*.pc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files applet
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomeapplet.so
%{py_sitedir}/gtk-2.0/gnome/applet.py?

%files gtksourceview
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtksourceview.so
%{_gtkdocdir}/pygtksourceview

%files libgtop
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtop.so

%files libwnck
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/wnck.so

%files mediaprofiles
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/mediaprofiles.so

%files metacity
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/metacity.so

%files nautilus-cd-burner
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/nautilusburn.so

%files print
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/gnomeprint
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomeprint/*.so
%{py_sitedir}/gtk-2.0/gnomeprint/*.py?
%{_gtkdocdir}/pygnomeprint
%{_gtkdocdir}/pygnomeprintui

%if %{with totem}
%files totem
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/totem
%attr(755,root,root) %{py_sitedir}/gtk-2.0/totem/*.so
%{py_sitedir}/gtk-2.0/totem/__init__.py?
%endif
