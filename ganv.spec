Summary:	Interactive Gtk canvas widget for graph-based interfaces
Summary(pl.UTF-8):	Interaktywny widget płótna Gtk dla interfejsów opartych na grafach
Name:		ganv
Version:	1.8.0
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	37419b39a90622de9cf27e034fdb33c1
URL:		http://drobilla.net/software/ganv/
BuildRequires:	gettext-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	graphviz-devel >= 2.30
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	gtkmm-devel >= 2.10.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRequires:	python >= 2
BuildRequires:	yelp-tools
Requires:	gtkmm >= 2.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ganv is an interactive Gtk canvas widget for graph-based interfaces
(patchers, modular synthesizers, finite state automata, interactive
graphs, etc).

%description -l pl.UTF-8
Ganv to interaktywny widget płótna Gtk do interfejsów opartych na
grafach (panele połączeniowe, modularne syntezatory, automaty
skończone, wykresy interaktywne itp.).

%package devel
Summary:	Header files for Ganv library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ganv
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2.0
Requires:	gtkmm-devel >= 2.10.0

%description devel
Header files for Ganv library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ganv.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--gir \
	--strict

./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/gir-1.0
%{__mv} $RPM_BUILD_ROOT%{_libdir}/girepository-1.0/*.gir $RPM_BUILD_ROOT%{_datadir}/gir-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/ganv_bench
%attr(755,root,root) %{_libdir}/libganv-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libganv-1.so.1
%{_libdir}/girepository-1.0/Ganv-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libganv-1.so
%{_includedir}/ganv-1
%{_datadir}/gir-1.0/Ganv-1.0.gir
%{_pkgconfigdir}/ganv-1.pc
