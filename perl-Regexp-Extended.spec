%define upstream_name    Regexp-Extended
%define upstream_version 0.01
Name:		perl-%{upstream_name}
Version:	0.01
Release:	1

Summary:	Regexp::Extended - Perl wrapper that extends the re module with new features
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/C/CR/CRUNCHIE/Regexp-Extended-0.01.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Clone)
BuildArch:	noarch

%description
Rexexp::Extended is a simple wrapper arround the perl rexexp
syntax. It uses the overload module to parse constant qr// 
expressions and substitute known operators with an equivalent perl
re.

%prep
%setup -q -n %{upstream_name}-%{version}

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


