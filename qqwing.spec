%define major 2
%define libname %mklibname %name %major
%define devname %mklibname -d %name

Name:           qqwing
Version:        1.3.4
Release:        4
Summary:        Command-line Sudoku solver and generator
Group:		Games/Puzzles
License:        GPLv2+
URL:            https://ostermiller.org/qqwing/
Source0:        http://ostermiller.org/qqwing/qqwing-%{version}.tar.gz

%description
QQwing is a command-line Sudoku solver and generator.

%package        -n %{libname}
Summary:        Library for Sudoku solving and generation
Group:		System/Libraries

%description    -n %{libname}
libqqwing is a C++ library for solving and generating Sudoku puzzles.

%package        -n %{devname}
Summary:        Development files for libqqwing
Group:		Development/C++
Requires:       %{libname} = %{version}-%{release}

%description    -n %{devname}
Libraries and header files for developing applications that use libqqwing.

%prep
%setup -q

%build
%configure
%make

%install
%make_install

%files
%doc README
%{_bindir}/qqwing
%{_mandir}/man1/qqwing.1.*

%files -n %{libname}
%doc AUTHORS COPYING
%{_libdir}/libqqwing.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/libqqwing.so
%{_libdir}/pkgconfig/qqwing.pc

