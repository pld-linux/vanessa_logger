Summary:	Generic logging layer
Summary(pl):	Podstawowa warstwa loguj±ca
Name:		vanessa_logger
Version:	0.0.2
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	ftp://vergenet.net/pub/vanessa_logger/vanessa_logger/%{name}-%{version}.tar.gz
URL:		http://vanessa.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Generic logging layer that may be used to log to one or more of syslog, an
open file handle or a file name. Though due to to limitations in the
implementation of syslog opening multiple syslog loggers doesn't makes
sense. Includes the ability to limit which messages will be logged based on
priorities.

%package devel
Summary:	Headers and static libraries for development
Group:		Development/Libraries
Requires:	%{name}-%{version}

%description devel
Headers and static libraries required to develop against vanessa_logger.

%package sample
Summary:	Example programme that demonstrates vanessa_logger.
Group:		Development/Libraries
Requires:	%{name}-devel-%{version}

%description sample
Sample programme with source that demonstrates various features of
vanessa_logger.


%prep
%setup -q

%build
sed -e s/AC_PROG_RANLIB/AC_PROG_LIBTOOL/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in

rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
CFLAGS="${RPM_OPT_FLAGS}"
%{__make}


%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/{etc,%{prefix}/{lib,bin,doc}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README ChangeLog NEWS TODO

%clean
rm -rf $RPM_BUILD_DIR/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root,755)
%attr(755,root,root) %{_libdir}/*.so*

%files devel
%attr(755,root,root) %{_libdir}/*.*a
%attr(644,root,root) %{_includedir}/*.h
%doc *.gz

%files sample
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/vanessa_logger_sample.*
%doc sample/*.c sample/*.h

%changelog
* Thu Apr 26 2001 Horms <horms@vergenet.net>
  Updated to "work" with Red Hat 7

* Sat Sep 15 2000 Horms <horms@vergenet.net>
- created for version 0.0.0
