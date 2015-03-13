Name:           qqwing
Version:        1.3.3
Release:        1%{?dist}
Summary:        Command-line Sudoku solver and generator

License:        GPLv2+
URL:            http://qqwing.com/
Source0:        http://qqwing.com/qqwing-%{version}.tar.gz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
QQwing is a command-line Sudoku solver and generator.

%package        libs
Summary:        Library for Sudoku solving and generation

%description    libs
libqqwing is a C++ library for solving and generating Sudoku puzzles.

%package        devel
Summary:        Development files for libqqwing
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use libqqwing.

%prep
%setup -q

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files
%doc README
%{_bindir}/qqwing
%{_mandir}/man1/qqwing.1.*

%files libs
%doc AUTHORS COPYING
%{_libdir}/libqqwing.so.*

%files devel
%{_includedir}/*
%{_libdir}/libqqwing.so
%{_libdir}/pkgconfig/qqwing.pc

%changelog
* Thu Nov 20 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.3.3-1
- Update to 1.3.3

* Sun Sep 21 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.3.1-1
- Update to 1.3.1 and drop soname patch.

* Sun Sep 21 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.3.0-2
- Revert soname bump.

* Sat Sep 20 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.3.0-1
- Update to 1.3.0.
- Update URLs.

* Sat Aug 23 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.2.0-2
- Really update to 1.2.0. Much learning.

* Sat Aug 23 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.2.0-1
- Update to 1.2.0

* Tue Aug 19 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.1.3-1
- Trivial spec cleanups

* Fri Aug 15 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.1.3-1
- Switch the base package from libqqwing to qqwing
- Update to 1.1.3

* Sat Aug  2 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.1.2-1
- New package
