Summary:	Generic logging layer
Summary(pl):	Podstawowa warstwa loguj±ca
Name:		vanessa_logger
Version:	0.0.2
Release:	3
License:	LGPL
Group:		Libraries
Source0:	ftp://vergenet.net/pub/vanessa_logger/vanessa_logger/%{name}-%{version}.tar.gz
URL:		http://vanessa.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generic logging layer that may be used to log to one or more of
syslog, an open file handle or a file name. Though due to to
limitations in the implementation of syslog opening multiple syslog
loggers doesn't make sense. Includes the ability to limit which
messages will be logged based on priorities.

%description -l pl
Wspólna warstwa loguj±ca, która mo¿e byæ u¿yta do logowania do jednego
lub wiêcej spo¶ród: sysloga, uchwytu otwartego pliku lub nazwy pliku;
ale z powodu ograniczenia implementacji sysloga otwieranie wielu
loggerów nie ma sensu. Zawiera tak¿e mo¿liwo¶æ limitowania, które
komunikaty bêd± logowane, na podstawie priorytetów.

%package devel
Summary:	Headers for vanessa_logger development
Summary(pl):	Pliki nag³ówkowe vanessa_logger
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Headers required to develop against vanessa_logger.

%description devel -l pl
Pliki nag³ówkowe potrzebne do tworzenia programów u¿ywaj±cych
vanessa_logger.

%package static
Summary:	Static libraries for vanessa_logger development
Summary(pl):	Biblioteki statyczne vanessa_logger
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries to develop against vanessa_logger.

%description static -l pl
Biblioteki statyczne vanessa_logger.

%package sample
Summary:	Example programme that demonstrates vanessa_logger
Summary(pl):	Przyk³adowy program demonstracyjny do vanessa_logger
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description sample
Sample programme with source that demonstrates various features of
vanessa_logger.

%description sample -l pl
Przyk³adowy program (ze ¼ród³ami), który demonstruje ró¿ne mo¿liwo¶ci
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
CFLAGS="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_prefix}/{lib,bin,doc}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README ChangeLog NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%attr(644,root,root) %{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files sample
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/vanessa_logger_sample.*
%doc sample/*.c sample/*.h
