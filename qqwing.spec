%define major   2
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:           qqwing
Version:        1.3.3
Release:        1
Summary:        Command-line Sudoku solver and generator

License:        GPLv2+
Group:		Games/Puzzles
URL:            http://qqwing.com/
Source0:        http://qqwing.com/qqwing-%{version}.tar.gz
Requires:       %{libname} = %{EVRD}

%description
QQwing is a command-line Sudoku solver and generator.

%package -n %{libname}
Summary:        Library for Sudoku solving and generation
Group:		System/Libraries

%description -n %{libname}
libqqwing is a C++ library for solving and generating Sudoku puzzles.

%package -n %{devname}
Summary:        Development files for libqqwing
Group:		Development/C++
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use libqqwing.

%prep
%setup -q

%build
%configure2_5x \
	 --disable-static

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make


%install
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

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

