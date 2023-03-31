%define major 0
%define libname %mklibname xcb-xrm %{major}
%define develname %mklibname xcb-xrm -d

%global optflags %{optflags} -O3

Name:		xcb-util-xrm
Version:	1.3
Release:	3
Summary:	XCB utility functions for the X resource manager
Group:		System/Libraries

License:	MIT
URL:		https://github.com/Airblader/xcb-util-xrm
Source0:	https://github.com/Airblader/xcb-util-xrm/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(xcb-aux)
BuildRequires:	pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)

%description
%{summary}.

%package	-n %{libname}
Summary:	XCB utility functions for the X resource manager
Group:		System/Libraries

%description -n %{libname}
%{summary}.

%package	-n %{develname}
Summary:	Development files for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
%{summary}.

%prep
%autosetup -p1

%build
autoreconf -vfi
%configure --disable-silent-rules --disable-static --disable-dependency-tracking
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%check
%__make check

%files -n %{libname}
%license COPYING
%{_libdir}/*.so.%{major}{,.*}

%files -n %{develname}
%{_includedir}/xcb/%(n=xcb-xrm; echo ${n//-/_}).h
%{_libdir}/*.so
%{_libdir}/pkgconfig/xcb-xrm.pc
