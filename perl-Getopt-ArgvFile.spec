#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	ArgvFile
Summary:	Getopt::ArgvFile - interpolates script options from files into @ARGV
Summary(pl):	Getopt::ArgvFile - interpolacja opcji skryptu z pliku do @ARGV
Name:		perl-Getopt-ArgvFile
Version:	1.01
Release:	10
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0959872e4aabfc5b8e1a5caf3526b4c2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Getopt::ArgvFile Perl module simply interpolates option file hints
in @ARGV by the contents of the pointed files. This enables option
reading from files instead of or additional to the usual reading from
the command line.

%description -l pl
Modu³ Perla Getopt::ArgvFile s³u¿y do interpolacji opcji skryptu z
pliku do @ARGV poprzez zawarto¶æ wskazywanych plików. W³±cza to odczyt
opcji z pliku zamiast lub oprócz zwyk³ego ich odczytu z linii
polecenia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Getopt/ArgvFile.pm
%{_mandir}/man3/*
