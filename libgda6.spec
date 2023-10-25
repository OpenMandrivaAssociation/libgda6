%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define _disable_rebuild_configure 1

%define build_mysql 1
%{?_with_mysql: %global build_mysql 1}

%define api 6.0
%define major 6
%define pkgname libgda%{api}
%define oname gda6

%define libname %mklibname %{oname}
%define libnamereport %mklibname %{oname}-report
%define libnameui %mklibname %{oname}-ui
%define libnamexslt %mklibname %{oname}-xslt
%define girname %mklibname %{oname}-gir
%define girnameui %mklibname %{oname}ui-gir
%define devname %mklibname -d %{oname}

Summary:	GNU Data Access
Name:		libgda6
Version:	6.0.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Databases
Url:		https://www.gnome-db.org/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/libgda/%{url_ver}/libgda-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	bison
BuildRequires:	yelp-tools
BuildRequires:	flex
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	db-devel
BuildRequires:	gdbm-devel
BuildRequires:	pkgconfig(ldap)
BuildRequires:	postgresql-devel
BuildRequires:	readline-devel
BuildRequires:	unixODBC-devel
BuildRequires:	xbase-devel
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(goocanvas)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:	pkgconfig(libgvc)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(sqlite3) >= 3.7.15.2
BuildRequires:  pkgconfig(vapigen)
%if %{build_mysql}
BuildRequires:	mysql-devel
%endif

Requires:	iso-codes

%description
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

%package -n	%{pkgname}
Summary:	GNU Data Access Development
Group: 		Databases

%description -n	%{pkgname}
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

%package -n	%{libname}
Summary:	GNU Data Access Development
Group: 		System/Libraries
Provides:	libgda = %{EVRD}

%description -n	%{libname}
This package contains the shared library for %{name}.

%package -n %{girname}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n	%{devname}
Summary:	GNU Data Access Development
Group: 		Development/Databases
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package contains the development files for %{name}.

%prep
%autosetup -n libgda-%{version} -p1

%build
export CPPFLAGS+=' -I/usr/include/graphviz'
%meson
%meson_build

%install
%meson_install
%find_lang libgda-%{api} --with-gnome --all-name

%files -n %{pkgname} -f libgda-%{api}.lang
%doc AUTHORS COPYING README
%{_datadir}/libgda-%{api}
%dir %{_libdir}/libgda-%{api}
%dir %{_libdir}/libgda-%{api}/providers

%files -n %{libname}
%{_libdir}/libgda-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Gda-%{api}.typelib

%files -n %{devname}
%{_libdir}/libgda-%{api}.so
%{_libdir}/libgda-%{api}/providers/libgda-postgres-%{api}.so
%{_libdir}/libgda-%{api}/providers/libgda-sqlite-%{api}.so
%{_libdir}/pkgconfig/libgda-%{api}.pc
%{_libdir}/pkgconfig/libgda-postgres-%{api}.pc
%{_libdir}/pkgconfig/libgda-sqlite-%{api}.pc
%{_includedir}/libgda-%{api}/libgda/
%{_datadir}/vala/vapi/libgda-%{api}.deps
%{_datadir}/vala/vapi/libgda-%{api}.vapi
%{_datadir}/gir-1.0/Gda-6.0.gir
