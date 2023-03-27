Summary:	A client-side decorations library for Wayland client
Summary(pl.UTF-8):	Biblioteka dekoracji po stronie klienta dla klientów Wayland
Name:		libdecor
Version:	0.1.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://gitlab.freedesktop.org/libdecor/libdecor/-/releases
Source0:	https://gitlab.freedesktop.org/libdecor/libdecor/uploads/ee5ef0f2c3a4743e8501a855d61cb397/%{name}-%{version}.tar.xz
# Source0-md5:	7201e594958075d125e6f372d1cf56d7
URL:		https://gitlab.freedesktop.org/libdecor/libdecor
BuildRequires:	cairo-devel
BuildRequires:	dbus-devel >= 1.0
BuildRequires:	meson >= 0.47.0
BuildRequires:	ninja
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel >= 1.18
BuildRequires:	wayland-protocols >= 1.15
BuildRequires:	xz
Requires:	wayland >= 1.18
Suggests:	%{name}-plugin-cairo = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdecor is a library that can help Wayland clients draw window
decorations for them. It aims to provide multiple backends that
implements the decoration drawing.

%description -l pl.UTF-8
libdecor to biblioteka pomagająca klientom Wayland rysować dekoracje
okien. Celem jest dostarczenie wielu backendów implementujących
rysowanie dekoracji.

%package devel
Summary:	Development files for libdecor
Summary(pl.UTF-8):	Pliki programistyczne libdecor
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for developing applications
that use libdecor.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących libdecor.

%package plugin-cairo
Summary:	Cairo plugin for libdecor
Summary(pl.UTF-8):	Wtyczka Cairo do libdecor
Requires:	%{name} = %{version}-%{release}

%description plugin-cairo
Cairo plugin for libdecor.

%description plugin-cairo -l pl.UTF-8
Wtyczka Cairo do libdecor.

%prep
%setup -q

%build
%meson build \
	-Ddemo=false

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libdecor-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdecor-0.so.0
%dir %{_libdir}/libdecor
%dir %{_libdir}/libdecor/plugins-1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdecor-0.so
%dir %{_includedir}/libdecor-0
%{_includedir}/libdecor-0/libdecor.h
%{_pkgconfigdir}/libdecor-0.pc

%files plugin-cairo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdecor/plugins-1/libdecor-cairo.so
