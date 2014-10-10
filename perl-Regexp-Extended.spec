%define upstream_name    Regexp-Extended
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Regexp::Extended - Perl wrapper that extends the re module with new features
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Regexp/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Clone)
BuildArch:	noarch

%description
Rexexp::Extended is a simple wrapper arround the perl rexexp
syntax. It uses the overload module to parse constant qr// 
expressions and substitute known operators with an equivalent perl
re.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# make test don't work
# make test

%install
%makeinstall_std

%files
%doc README
%dir %{perl_vendorlib}/Regexp/Extended
%{perl_vendorlib}/Regexp/Extended/*
%{perl_vendorlib}/Regexp/Extended.pm
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 404357
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.01-6mdv2009.0
+ Revision: 258324
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.01-5mdv2009.0
+ Revision: 246393
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.01-3mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.01-3mdv2008.0
+ Revision: 25101
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-2mdk
- Fix According to perl Policy
	- Source URL
	- BuildRequires
- use mkrel

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdk
- initial Mandriva package

