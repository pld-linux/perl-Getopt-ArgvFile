%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	ArgvFile
Summary:	Getopt::ArgvFile perl module
Summary(pl):	Modu³ perla Getopt::ArgvFile
Name:		perl-Getopt-ArgvFile
Version:	1.01
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt::ArgvFile interpolates script options from files into @ARGV.

%description -l pl
Getopt::ArgvFile s³u¿y do interpolacji opcji skryptu z pliku do @ARGV.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Getopt/ArgvFile.pm
%{_mandir}/man3/*
