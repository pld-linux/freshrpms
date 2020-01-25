Summary:	Fetch RPM packages from FTP servers which are newer than the ones installed on your system
Summary(pl.UTF-8):	Ściąga nowe pakiety RPM z serwerów FTP
Name:		freshrpms
Version:	0.7.4
Release:	7
License:	distributable
Group:		Applications/System
Source0:	ftp://ftp.cs.tu-berlin.de/pub/local/flp/lutzeb/software/freshrpms/%{name}.tar.gz
# Source0-md5:	afce815b87a5e0b758932d94f634525f
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
freshrpms is a Perl5 script which fetches RPM packages from FTP
servers which version numbers are higher than the ones installed on
your system. freshrpms does not install any RPMs by itself but makes
use of the package manager program to determine which RPM packages are
currently installed. freshrpms uses a configuration file to accomplish
its task which defines multiple FTP servers, directories to look for
RPMs, local download directories and local archive directories for
installed RPMs. It can also garbage collect local archived RPMs which
are older than the currenly installed ones.

%description -l pl.UTF-8
freshrpms jest skryptem w języku Perl, ściągającym z serwerów FTP
pakiety RPM, których numery wersji są wyższe niż tych zainstalowanych
w Twoim systemie. freshrpms nie instaluje samodzielnie żadnych
pakietów, ale tylko wykorzystuje zarządcę pakietów, aby sprawdzić
jakie pakiety masz zainstalowane. freshrpms do wykonania swojego
zadania używa pliku konfiguracyjnego, który definiuje używane serwery
FTP, ścieżki poszukiwań, lokalne katalogi na nowe pakiety oraz
archiwum. Może także przenosić stare pakiety do archiwum.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

chmod u+w .

install freshrpms $RPM_BUILD_ROOT%{_bindir}/freshrpms
install freshrpms.conf $RPM_BUILD_ROOT%{_sysconfdir}/freshrpms.conf
install freshrpms.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/freshrpms.conf
%attr(755,root,root) %{_bindir}/freshrpms
%{_mandir}/man1/freshrpms.1*
