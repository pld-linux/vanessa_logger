Summary:	Generic logging layer
Summary(pl):	Podstawowa warstwa loguj±ca
Name:		vanessa_logger
Version:	0.0.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.vergenet.net/linux/vanessa/download/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	562d3eeeedcbbb017a500d91e95cef00
URL:		http://www.vergenet.net/linux/vanessa/
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
Requires:	%{name} = %{version}-%{release}

%description devel
Headers required to develop against vanessa_logger.

%description devel -l pl
Pliki nag³ówkowe potrzebne do tworzenia programów u¿ywaj±cych
vanessa_logger.

%package static
Summary:	Static libraries for vanessa_logger development
Summary(pl):	Biblioteki statyczne vanessa_logger
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries to develop against vanessa_logger.

%description static -l pl
Biblioteki statyczne vanessa_logger.

%package sample
Summary:	Example programme that demonstrates vanessa_logger
Summary(pl):	Przyk³adowy program demonstracyjny do vanessa_logger
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description sample
Sample programme with source that demonstrates various features of
vanessa_logger.

%description sample -l pl
Przyk³adowy program (ze ¼ród³ami), który demonstruje ró¿ne mo¿liwo¶ci
vanessa_logger.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files sample
%defattr(644,root,root,755)
%doc sample/*.c sample/*.h
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/vanessa_logger_sample.1*
