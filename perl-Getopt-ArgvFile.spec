%include	/usr/lib/rpm/macros.perl
Summary:	Getopt-ArgvFile perl module
Summary(pl):	Modu³ perla Getopt-ArgvFile
Name:		perl-Getopt-ArgvFile
Version:	1.01
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Getopt/Getopt-ArgvFile-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt-ArgvFile interpolates script options from files into @ARGV.

%description -l pl
Getopt-ArgvFile s³u¿y do interpolacji opcji skryptu z pliku do @ARGV.

%prep
%setup -q -n Getopt-ArgvFile-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Getopt/ArgvFile.pm
%{_mandir}/man3/*
