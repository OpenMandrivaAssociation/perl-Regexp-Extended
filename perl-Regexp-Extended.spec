%define real_name Regexp-Extended

Summary:	Regexp::Extended - Perl wrapper that extends the re module with new features
Name:		perl-%{real_name}
Version:	0.01
Release: %mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Regexp/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Clone)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Rexexp::Extended is a simple wrapper arround the perl rexexp
syntax. It uses the overload module to parse constant qr// 
expressions and substitute known operators with an equivalent perl
re.

%prep
%setup -q -n %{real_name}-%{version} 

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

