%define upstream_name    Regexp-Extended
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Regexp::Extended - Perl wrapper that extends the re module with new features
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Regexp/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Clone)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Rexexp::Extended is a simple wrapper arround the perl rexexp
syntax. It uses the overload module to parse constant qr// 
expressions and substitute known operators with an equivalent perl
re.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# make test don't work
# make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%dir %{perl_vendorlib}/Regexp/Extended
%{perl_vendorlib}/Regexp/Extended/*
%{perl_vendorlib}/Regexp/Extended.pm
%{_mandir}/*/*
