Summary:	Generic logging layer
Summary(pl.UTF-8):	Podstawowa warstwa logująca
Name:		vanessa_logger
Version:	0.0.7
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.vergenet.net/linux/vanessa/download/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a3245db1a18169404affecc2422c64a6
URL:		http://www.vergenet.net/linux/vanessa/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generic logging layer that may be used to log to one or more of
syslog, an open file handle or a file name. Though due to to
limitations in the implementation of syslog opening multiple syslog
loggers doesn't make sense. Includes the ability to limit which
messages will be logged based on priorities.

%description -l pl.UTF-8
Wspólna warstwa logująca, która może być użyta do logowania do jednego
lub więcej spośród: sysloga, uchwytu otwartego pliku lub nazwy pliku;
ale z powodu ograniczenia implementacji sysloga otwieranie wielu
loggerów nie ma sensu. Zawiera także możliwość limitowania, które
komunikaty będą logowane, na podstawie priorytetów.

%package devel
Summary:	Headers for vanessa_logger development
Summary(pl.UTF-8):	Pliki nagłówkowe vanessa_logger
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers required to develop against vanessa_logger.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do tworzenia programów używających
vanessa_logger.

%package static
Summary:	Static libraries for vanessa_logger development
Summary(pl.UTF-8):	Biblioteki statyczne vanessa_logger
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries to develop against vanessa_logger.

%description static -l pl.UTF-8
Biblioteki statyczne vanessa_logger.

%package sample
Summary:	Example programme that demonstrates vanessa_logger
Summary(pl.UTF-8):	Przykładowy program demonstracyjny do vanessa_logger
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description sample
Sample programme with source that demonstrates various features of
vanessa_logger.

%description sample -l pl.UTF-8
Przykładowy program (ze źródłami), który demonstruje różne możliwości
vanessa_logger.

%prep
%setup -q

%build
%{__autoconf}
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
