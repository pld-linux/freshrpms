Summary:	Fetch RPM packages from FTP servers which are newer than the ones installed on your system
Summary(pl):	¦ci±ga pakiety nowe pakiet RPM z serwerów FTP
Name:		freshrpms
Version:	0.7.4
Release:	5
License:	Distributable
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.cs.tu-berlin.de/pub/local/flp/lutzeb/software/freshrpms/%{name}.tar.gz
Requires:	perl-libnet
Requires:	perl >= 5.004
Buildarch:	noarch
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

%description -l pl
freshrpms jest skryptem w jêzyku Perl, ¶ci±gaj±cym z serwerów FTP
pakiety RPM, których numery wersji s± wy¿sze ni¿ tych zainstalowanych
w Twoim systemie. freshrpms nie instaluje samodzielnie ¿adnych
pakietów, ale tylko wykorzystuje mened¿era pakietów, aby sprawdziæ
jakie pakiety masz zainstalowane. freshrpms do wykonania swojego
zadzania u¿ywa pliku konfiguracyjnego, który definiuje u¿ywane serwery
FTP, ¶cie¿ki poszukiwañ, lokalne katalogi na nowe pakiety oraz
archiwum. Mo¿e tak¿e przenosiæ stare pakiety do archiwum.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1,etc}

chmod u+w .

install freshrpms $RPM_BUILD_ROOT%{_bindir}/freshrpms
install freshrpms.conf $RPM_BUILD_ROOT%{_sysconfdir}/freshrpms.conf

install freshrpms.1 $RPM_BUILD_ROOT%{_mandir}/man1/

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config %{_sysconfdir}/freshrpms.conf
%attr(755,root,root) %{_bindir}/freshrpms
%{_mandir}/man1/freshrpms.1*
